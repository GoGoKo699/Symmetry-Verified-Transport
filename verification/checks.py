#!/usr/bin/env python3
"""Finite, independently constructed checks for symmetry-verified transport.

The main dynamic checks exponentiate the complete classical Markov generator;
they do not create the monitored channel from the claimed eigenvalue formula.
Numerical checks do not establish universal or asymptotic theorems.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from math import comb, cos, exp, log, pi
from pathlib import Path
import platform

import numpy as np
import scipy
from scipy.linalg import expm


TOL = 2e-10


def require_close(actual, expected, label, tolerance=TOL):
    error = float(np.max(np.abs(np.asarray(actual) - np.asarray(expected))))
    if error > tolerance:
        raise AssertionError(f"{label}: absolute error {error:.4g}")
    return error


def pass_polynomial(n, p):
    """Valid for Fraction as well as float inputs; P_0 is exactly one."""
    return sum(comb(n, k) ** 2 * p ** (2 * k)
               * (1 - p) ** (2 * (n - k)) for k in range(n + 1))


class SpinChain:
    """All bitstrings, with site zero the least significant binary digit."""

    def __init__(self, n, swap_rate, flip_rate):
        self.n = n
        self.length = 2 * n
        self.size = 1 << self.length
        self.swap_rate = swap_rate
        self.flip_rate = flip_rate
        labels = np.arange(self.size)
        self.bits = ((labels[:, None] >> np.arange(self.length)) & 1).astype(int)
        self.charge = self.bits.sum(axis=1)
        self.sector = np.flatnonzero(self.charge == n)
        self.uniform = np.zeros(self.size)
        self.uniform[self.sector] = 1 / len(self.sector)
        self.swap_generator = np.zeros((self.size, self.size))
        self.flip_generator = np.zeros((self.size, self.size))
        self.swap_permutations = []
        # N>=2 is the simple periodic nearest-neighbor chain. The N=1 boundary
        # check below sets swap_rate=0, avoiding a two-site bond convention.
        edges = sorted({tuple(sorted((j, (j + 1) % self.length)))
                        for j in range(self.length)})
        for left, right in edges:
            difference = self.bits[:, left] ^ self.bits[:, right]
            target = labels ^ (difference << left) ^ (difference << right)
            permutation = np.zeros((self.size, self.size))
            permutation[target, labels] = 1
            self.swap_permutations.append(permutation)
            self.swap_generator += swap_rate * (permutation - np.eye(self.size))
        for site in range(self.length):
            target = labels ^ (1 << site)
            self.flip_generator[target, labels] += flip_rate
            self.flip_generator[labels, labels] -= flip_rate
        self.generator = self.swap_generator + self.flip_generator
        self.coefficients = np.cos(2 * pi * np.arange(self.length) / self.length)
        self.mode = (self.bits - 0.5) @ self.coefficients
        self.initial_derivative = self.uniform * self.mode
        self.omega = (2 * swap_rate * (1 - cos(2 * pi / self.length))
                      if n >= 2 else 2 * swap_rate)
        self._evolutions = {}

    def evolution(self, interval):
        interval = float(interval)
        if interval not in self._evolutions:
            self._evolutions[interval] = expm(interval * self.generator)
        return self._evolutions[interval]

    def monitored_record(self, intervals):
        """Propagate probability and its exact derivative, retaining all atoms.

        Failure atoms are (check index, measured total charge). Accepted atoms
        are the final microscopic bitstrings. There is no finite differencing.
        """
        probability = self.uniform.copy()
        derivative = self.initial_derivative.copy()
        failure_records = []
        accepted_map = np.eye(len(self.sector))
        for index, interval in enumerate(intervals):
            transition = self.evolution(interval)
            probability = transition @ probability
            derivative = transition @ derivative
            for charge in range(self.length + 1):
                if charge == self.n:
                    continue
                selection = self.charge == charge
                failure_records.append({
                    "check": index + 1,
                    "charge": charge,
                    "probability": float(probability[selection].sum()),
                    "derivative": float(derivative[selection].sum()),
                })
            probability[self.charge != self.n] = 0
            derivative[self.charge != self.n] = 0
            restricted = transition[np.ix_(self.sector, self.sector)]
            accepted_map = restricted @ accepted_map
        accepted = probability[self.sector]
        accepted_derivative = derivative[self.sector]
        acceptance = float(accepted.sum())
        accepted_fi = float(np.sum(accepted_derivative**2 / accepted))
        failure_fi = sum(record["derivative"]**2 / record["probability"]
                         for record in failure_records if record["probability"] > 0)
        total_probability = acceptance + sum(r["probability"] for r in failure_records)
        require_close(total_probability, 1, "all record probabilities sum to one")
        return {
            "accepted": accepted,
            "accepted_derivative": accepted_derivative,
            "accepted_map": accepted_map,
            "acceptance": acceptance,
            "fisher_information": accepted_fi + failure_fi,
            "failure_information": failure_fi,
            "largest_failure_derivative": max(abs(r["derivative"])
                                               for r in failure_records),
            "failure_records": failure_records,
        }

    def raw_record(self, time):
        transition = self.evolution(time)
        probability = transition @ self.uniform
        derivative = transition @ self.initial_derivative
        mean = float(self.mode @ probability)
        variance = float(self.mode**2 @ probability - mean**2)
        response = float(self.mode @ derivative)
        information = response**2 / variance
        return {"variance": variance, "response": response,
                "moment_information": information,
                "full_record_information": float(np.sum(derivative**2 / probability))}

    def transcript_probabilities(self, intervals, amplitude):
        """Direct finite-amplitude propagation, independent of derivative vectors.

        Order: all rejected check-index/charge atoms, then accepted bitstrings.
        This separately constructed vector is used for finite-u KL and FI checks.
        """
        probability = self.uniform * (1 + amplitude*self.mode)
        if probability.min() < -TOL:
            raise ValueError("amplitude does not define a positive initial law")
        failures = []
        for interval in intervals:
            probability = self.evolution(interval) @ probability
            failures.extend(float(probability[self.charge == charge].sum())
                            for charge in range(self.length+1) if charge != self.n)
            probability[self.charge != self.n] = 0
        transcript = np.concatenate([np.array(failures), probability[self.sector]])
        require_close(transcript.sum(), 1, "finite-amplitude transcript normalization")
        return transcript


def check_generators_and_kernels():
    records = []
    for n, swap_rate, flip_rate, interval in [
        (2, 0.7, 0.21, 0.37),
        (3, 0.4, 0.63, 0.71),
    ]:
        chain = SpinChain(n, swap_rate, flip_rate)
        q_swap, q_flip = chain.swap_generator, chain.flip_generator
        stochastic_error = require_close(chain.generator.sum(axis=0), 0,
                                         "generator preserves total probability")
        commutator_error = require_close(q_swap @ q_flip, q_flip @ q_swap,
                                         "independent flips commute with swaps")
        evolution = chain.evolution(interval)
        factorization_error = require_close(
            evolution, expm(interval * q_swap) @ expm(interval * q_flip),
            "full generator factorization")
        flip_transition = expm(interval * q_flip)
        restricted = flip_transition[np.ix_(chain.sector, chain.sector)]
        pass_columns = restricted.sum(axis=0)
        p = (1 - exp(-2 * flip_rate * interval)) / 2
        expected_pass = pass_polynomial(n, p)
        pass_error = require_close(pass_columns, expected_pass,
                                  "pass probability independent of input")
        kernel = restricted / pass_columns[None, :]
        bits = chain.bits[chain.sector]
        hamming = np.sum(bits[:, None] != bits[None, :], axis=2)
        expected_kernel = p**hamming * (1-p)**(2*n-hamming) / expected_pass
        kernel_error = require_close(kernel, expected_kernel,
                                     "exponentiated flip generator versus kernel")
        harmonic_errors = []
        for degree in range(1, n + 1):
            harmonic = np.prod(bits[:, :2*degree:2] - bits[:, 1:2*degree:2], axis=1)
            eigenvalue = ((1-2*p)**degree * pass_polynomial(n-degree, p)
                          / expected_pass)
            harmonic_errors.append(require_close(
                kernel.T @ harmonic, eigenvalue * harmonic,
                f"degree-{degree} harmonic from full kernel"))
        records.append({
            "N": n, "states": chain.size, "balanced_states": len(chain.sector),
            "swap_rate": swap_rate, "flip_rate": flip_rate, "interval": interval,
            "generator_stochasticity_error": stochastic_error,
            "generator_commutation_error": commutator_error,
            "factorization_error": factorization_error,
            "pass_probability_error": pass_error,
            "conditional_kernel_error": kernel_error,
            "harmonic_errors": harmonic_errors,
        })
    return records


def inspect_schedule(chain, intervals):
    record = chain.monitored_record(intervals)
    time = sum(intervals)
    h = exp(-chain.omega * time)
    s = exp(-2 * chain.flip_rate * time)
    sector_mode = chain.mode[chain.sector]
    variance_initial = float(chain.uniform @ chain.mode**2)
    initial_variance_error = require_close(
        variance_initial,
        chain.n/(2*(2*chain.n-1))*float(chain.coefficients@chain.coefficients),
        "balanced-slice mode variance")
    pass_product = 1.0
    attenuation_product = 1.0
    harmonic_logs = []
    full_schedule_harmonic_errors = []
    ideal_transition = expm(time * chain.swap_generator)[np.ix_(chain.sector, chain.sector)]
    sector_bits = chain.bits[chain.sector]
    for degree in range(1, chain.n + 1):
        log_attenuation = 0.0
        log_acceptance = 0.0
        for interval in intervals:
            p = (1-exp(-2*chain.flip_rate*interval))/2
            pn = pass_polynomial(chain.n, p)
            lam = ((1-2*p)**degree * pass_polynomial(chain.n-degree, p) / pn)
            log_attenuation += log(lam)
            log_acceptance += log(pn)
        harmonic_logs.append(log_attenuation + 2*degree*chain.flip_rate*time
                             + degree/chain.n*log_acceptance)
        harmonic = np.prod(sector_bits[:, :2*degree:2]
                           - sector_bits[:, 1:2*degree:2], axis=1)
        full_schedule_harmonic_errors.append(require_close(
            record["accepted_map"].T @ harmonic,
            exp(log_acceptance+log_attenuation) * ideal_transition.T @ harmonic,
            f"degree-{degree} schedule harmonic relative to ideal transport"))
    for interval in intervals:
        p = (1-exp(-2*chain.flip_rate*interval))/2
        pn = pass_polynomial(chain.n, p)
        pass_product *= pn
        attenuation_product *= (1-2*p)*pass_polynomial(chain.n-1, p)/pn
    acceptance_error = require_close(record["acceptance"], pass_product,
                                     "schedule acceptance from full dynamics")
    accepted_density_error = require_close(
        record["accepted"], np.full(len(chain.sector), pass_product/len(chain.sector)),
        "accepted reference distribution is uniform")
    derivative_error = require_close(
        record["accepted_derivative"],
        pass_product*h*attenuation_product*sector_mode/len(chain.sector),
        "accepted mode derivative from full dynamics")
    fi_expected = pass_product * h**2 * attenuation_product**2 * variance_initial
    fi_error = require_close(record["fisher_information"], fi_expected,
                             "complete record Fisher information")
    require_close(record["largest_failure_derivative"], 0,
                  "charge/failure records do not reveal the amplitude")
    if max(harmonic_logs) > TOL:
        raise AssertionError("gain-acceptance inequality violated")
    raw = chain.raw_record(time)
    p_total = (1-s)/2
    raw_variance_expected = (s**2*variance_initial
                             + p_total*(1-p_total)*float(chain.coefficients@chain.coefficients))
    raw_variance_error = require_close(raw["variance"], raw_variance_expected,
                                       "raw variance from full generator")
    raw_response_error = require_close(raw["response"], s*h*variance_initial,
                                       "raw response from full generator")
    if chain.n >= 2 and record["fisher_information"] > raw["moment_information"] + TOL:
        raise AssertionError("monitored record beats raw moment in claimed regime")
    summary = {
        "N": chain.n, "swap_rate": chain.swap_rate, "flip_rate": chain.flip_rate,
        "intervals": list(intervals), "time": time,
        "acceptance": record["acceptance"], "density_attenuation": attenuation_product,
        "initial_mode_variance": variance_initial,
        "checked_full_record_information": record["fisher_information"],
        "raw_moment_information": raw["moment_information"],
        "raw_full_record_information": raw["full_record_information"],
        "raw_variance": raw["variance"],
        "failure_information": record["failure_information"],
        "largest_failure_derivative": record["largest_failure_derivative"],
        "gain_acceptance_log_excess_by_degree": harmonic_logs,
        "full_schedule_harmonic_errors": full_schedule_harmonic_errors,
        "errors": {"acceptance": acceptance_error,
                   "initial_variance": initial_variance_error,
                   "accepted_distribution": accepted_density_error,
                   "mode_derivative": derivative_error, "fisher_information": fi_error,
                   "raw_variance": raw_variance_error, "raw_response": raw_response_error},
    }
    return summary, record


def check_schedules_and_information():
    summaries = []
    for n in [2, 3]:
        chain = SpinChain(n, swap_rate=0.43, flip_rate=0.37)
        for intervals in [[1.0], [0.13, 0.41, 0.09, 0.37], [0.125]*8]:
            summary, _ = inspect_schedule(chain, intervals)
            summaries.append(summary)
    return summaries


def check_random_schedule_labels():
    chain = SpinChain(3, swap_rate=0.43, flip_rate=0.37)
    schedules = [[1.0], [0.2, 0.8], [0.1, 0.3, 0.6]]
    weights = np.array([0.2, 0.3, 0.5])
    inspected = [inspect_schedule(chain, intervals) for intervals in schedules]
    summaries = [entry[0] for entry in inspected]
    records = [entry[1] for entry in inspected]
    probability = sum(w*r["accepted"] for w, r in zip(weights, records))
    derivative = sum(w*r["accepted_derivative"] for w, r in zip(weights, records))
    unlabeled_fi = float(np.sum(derivative**2/probability))
    labeled_fi = float(sum(w*r["fisher_information"] for w, r in zip(weights, records)))
    acceptance = float(probability.sum())
    attenuation = float(sum(w*s["acceptance"]*s["density_attenuation"]
                            for w, s in zip(weights, summaries))/acceptance)
    time = 1.0
    s = exp(-2*chain.flip_rate*time)
    log_excess = log(attenuation/s) + log(acceptance)/chain.n
    raw_information = chain.raw_record(time)["moment_information"]
    if not (unlabeled_fi <= labeled_fi + TOL <= raw_information + 2*TOL):
        raise AssertionError("random-schedule information comparison failed")
    if log_excess > TOL:
        raise AssertionError("unlabeled randomized gain-acceptance bound failed")
    return {"weights": weights.tolist(), "schedules": schedules,
            "overall_acceptance": acceptance, "accepted_mean_attenuation": attenuation,
            "information_with_schedule_label": labeled_fi,
            "information_without_schedule_label": unlabeled_fi,
            "raw_moment_information": raw_information,
            "gain_acceptance_log_excess": log_excess}


def relative_entropy(first, second):
    if np.any(first < 0) or np.any(second <= 0):
        raise AssertionError("KL check received invalid outcome probabilities")
    nonzero = first > 0
    return float(first[nonzero] @ np.log(first[nonzero]/second[nonzero]))


def check_finite_amplitudes():
    """Full finite-u likelihoods, transcript KL, and finite-sample raw risk."""
    summaries = []
    random_label_summaries = []
    schedules = [[1.0], [0.13, 0.41, 0.09, 0.37]]
    for n in [2, 3]:
        chain = SpinChain(n, swap_rate=0.43, flip_rate=0.37)
        time = 1.0
        ideal = exp(-chain.omega*time)
        survival = exp(-2*chain.flip_rate*time)
        initial_variance = float(chain.uniform@chain.mode**2)
        maximum_initial_mode = float(np.max(np.abs(chain.mode[chain.sector])))
        signal = survival**2*ideal**2*initial_variance
        a_n = (2*n-1+survival**2)/(2*n)
        raw_second_moment = a_n*initial_variance
        estimator_scale = survival*ideal*initial_variance
        full_raw_transition = chain.evolution(time)
        for beta in [0.2, 0.75]:
            amplitude_limit = beta/maximum_initial_mode
            for intervals in schedules:
                schedule_summary, derivative_record = inspect_schedule(chain, intervals)
                acceptance = schedule_summary["acceptance"]
                attenuation = schedule_summary["density_attenuation"]
                retained_scale = ideal*attenuation
                failure_count = len(derivative_record["failure_records"])
                transcript_derivative = np.concatenate([
                    np.array([r["derivative"] for r in derivative_record["failure_records"]]),
                    derivative_record["accepted_derivative"],
                ])
                for fraction in [0.25, 1.0]:
                    v = fraction*amplitude_limit
                    plus = chain.transcript_probabilities(intervals, v)
                    minus = chain.transcript_probabilities(intervals, -v)
                    kl = relative_entropy(plus, minus)
                    mode = chain.mode[chain.sector]
                    a = v*retained_scale*mode
                    mu = np.full(len(chain.sector), 1/len(chain.sector))
                    kl_expected = acceptance*float(mu@((1+a)*np.log((1+a)/(1-a))))
                    symmetric_kl = acceptance*float(mu@(a*np.log((1+a)/(1-a))))
                    kl_formula_error = require_close(kl, kl_expected,
                                                      "direct finite transcript KL")
                    odd_term_error = require_close(kl, symmetric_kl,
                                                   "complementation cancels odd KL term")
                    failure_sign_error = require_close(plus[:failure_count], minus[:failure_count],
                                                       "failure probabilities agree at +/-v")
                    kl_bound = 2*v**2*signal/(1-beta**2)
                    if kl > kl_bound + TOL:
                        raise AssertionError("finite transcript KL exceeds cadence bound")
                    offzero = []
                    for u, transcript in [(v, plus), (-v, minus)]:
                        checked_information = float(np.sum(transcript_derivative**2/transcript))
                        checked_expected = (acceptance*retained_scale**2
                                            *float(mu@(mode**2/(1+u*retained_scale*mode))))
                        fisher_error = require_close(checked_information, checked_expected,
                                                     "finite-u full record Fisher information")
                        even_denominator_error = require_close(
                            mu@(mode**2/(1+u*retained_scale*mode)),
                            mu@(mode**2/(1-u**2*retained_scale**2*mode**2)),
                            "finite-u complementary denominator identity")
                        raw_probability = full_raw_transition @ (
                            chain.uniform*(1+u*chain.mode))
                        mean = float(chain.mode@raw_probability)
                        second_moment = float(chain.mode**2@raw_probability)
                        variance = second_moment-mean**2
                        mean_error = require_close(mean, u*estimator_scale,
                                                   "offzero raw expectation")
                        second_moment_error = require_close(second_moment, raw_second_moment,
                                                            "offzero raw second moment is constant")
                        variance_expected = raw_second_moment-u**2*estimator_scale**2
                        variance_error = require_close(variance, variance_expected,
                                                       "offzero raw variance")
                        raw_information = estimator_scale**2/variance
                        if checked_information > signal/(1-beta**2) + TOL:
                            raise AssertionError("finite-u checked FI exceeds uniform bound")
                        if checked_information > raw_information/(1-beta**2) + TOL:
                            raise AssertionError("finite-u checked/raw information factor fails")
                        # Enumerate actual one- and two-attempt estimator outputs.
                        # The m=7 entry uses exact iid moments, without sampling.
                        mse_records = []
                        single_values = chain.mode/estimator_scale
                        for attempts in [1, 2, 7]:
                            if attempts == 1:
                                observed_mse = float(raw_probability@((single_values-u)**2))
                            elif attempts == 2:
                                output = (single_values[:, None]+single_values[None, :])/2
                                joint_probability = np.outer(raw_probability, raw_probability)
                                observed_mse = float(np.sum(joint_probability*(output-u)**2))
                            else:
                                single_mean = float(raw_probability@single_values)
                                single_variance = float(raw_probability@single_values**2-single_mean**2)
                                observed_mse = single_variance/attempts+(single_mean-u)**2
                            expected_mse = a_n/(attempts*signal)-u**2/attempts
                            mse_error = require_close(observed_mse, expected_mse,
                                                      "finite-sample raw estimator MSE")
                            mse_records.append({"attempts": attempts, "mse": observed_mse,
                                                "formula_error": mse_error,
                                                "method": "direct outcome enumeration" if attempts <= 2
                                                          else "exact iid moments"})
                        offzero.append({"amplitude": u,
                                        "checked_full_record_information": checked_information,
                                        "raw_moment_information": raw_information,
                                        "raw_second_moment": second_moment,
                                        "raw_variance": variance,
                                        "mse_checks": mse_records,
                                        "errors": {"fisher_information": fisher_error,
                                                   "complementary_denominator": even_denominator_error,
                                                   "raw_mean": mean_error,
                                                   "raw_second_moment": second_moment_error,
                                                   "raw_variance": variance_error}})
                    summaries.append({"N": n, "beta": beta,
                                      "amplitude_limit": amplitude_limit,
                                      "v": v, "intervals": intervals,
                                      "transcript_KL": kl, "KL_upper_bound": kl_bound,
                                      "KL_to_bound_ratio": kl/kl_bound,
                                      "errors": {"KL_formula": kl_formula_error,
                                                 "odd_term_cancellation": odd_term_error,
                                                 "failure_sign_independence": failure_sign_error},
                                      "offzero_checks": offzero})
            # Retain an independently drawn schedule label and construct the
            # joint label/outcome probabilities, rather than averaging signals.
            random_schedules = [[1.0], [0.2, 0.8], [0.1, 0.3, 0.6]]
            weights = [0.2, 0.3, 0.5]
            v = amplitude_limit
            plus_records = [chain.transcript_probabilities(intervals, v)
                            for intervals in random_schedules]
            minus_records = [chain.transcript_probabilities(intervals, -v)
                             for intervals in random_schedules]
            joint_plus = np.concatenate([weight*record for weight, record
                                         in zip(weights, plus_records)])
            joint_minus = np.concatenate([weight*record for weight, record
                                          in zip(weights, minus_records)])
            labeled_kl = relative_entropy(joint_plus, joint_minus)
            conditional_average = sum(weight*relative_entropy(first, second)
                                      for weight, first, second
                                      in zip(weights, plus_records, minus_records))
            average_error = require_close(labeled_kl, conditional_average,
                                           "retained-label KL chain rule")
            bound = 2*v**2*signal/(1-beta**2)
            if labeled_kl > bound+TOL:
                raise AssertionError("retained-label KL exceeds uniform cadence bound")
            random_label_summaries.append({"N": n, "beta": beta, "v": v,
                                            "weights": weights, "schedules": random_schedules,
                                            "joint_label_outcome_KL": labeled_kl,
                                            "conditional_KL_average": conditional_average,
                                            "KL_upper_bound": bound,
                                            "averaging_error": average_error})
    return {"fixed_schedules": summaries, "random_schedule_labels": random_label_summaries}


def check_exact_moment_inequality():
    rational_probabilities = [Fraction(0), Fraction(1, 10), Fraction(1, 4),
                              Fraction(49, 100), Fraction(1, 2)]
    cases = []
    for p in rational_probabilities:
        values = [pass_polynomial(n, p) for n in range(10)]
        for n in range(1, 9):
            if values[n]**2 > values[n-1]*values[n+1]:
                raise AssertionError("exact adjacent log-convexity failed")
            for degree in range(1, n+1):
                # No floating logarithms, roots, quadrature, or eigenvalues.
                if values[n-degree]**n > values[n]**(n-degree):
                    raise AssertionError("exact chord inequality failed")
        cases.append({"flip_probability": str(p),
                      "P_0_to_P_4": [str(x) for x in values[:5]],
                      "largest_N_tested": 8})
    return cases


def check_zeno_limit_and_n_one_boundary():
    chain = SpinChain(2, swap_rate=0.0, flip_rate=0.31)
    time = 0.8
    values = []
    for count in [1, 2, 4, 8, 16, 32, 64]:
        summary, _ = inspect_schedule(chain, [time/count]*count)
        values.append({"checks": count, "acceptance": summary["acceptance"],
                       "density_attenuation": summary["density_attenuation"]})
    endpoint = exp(-2*chain.n*chain.flip_rate*time)
    if not abs(values[-1]["acceptance"]-endpoint) < abs(values[0]["acceptance"]-endpoint):
        raise AssertionError("finite Zeno acceptance sequence did not approach endpoint")
    if not values[-1]["density_attenuation"] > values[0]["density_attenuation"]:
        raise AssertionError("finite Zeno attenuation did not approach restoration")
    boundary = SpinChain(1, swap_rate=0.0, flip_rate=1.0)
    boundary_summary, _ = inspect_schedule(boundary, [0.125]*8)
    if not (boundary_summary["checked_full_record_information"]
            > boundary_summary["raw_moment_information"]):
        raise AssertionError("N=1 boundary example did not escape N>=2 conclusion")
    return {"fixed_N": 2, "time": time, "flip_rate": chain.flip_rate,
            "fixed_N_acceptance_limit": endpoint, "finite_cadences": values,
            "N_one_counterexample": boundary_summary}


def check_coherent_control_escape():
    """Projected quantum Kraus map, including off-diagonal sector coherences."""
    results = []
    for n in [1, 2]:
        chain = SpinChain(n, swap_rate=0.0, flip_rate=0.4)
        sector = chain.sector
        dimension = len(sector)
        lookup = {int(x): i for i, x in enumerate(sector)}
        full_mask = chain.size - 1
        complement = np.zeros((dimension, dimension))
        z_first = np.diag(1-2*chain.bits[sector, 0]).astype(float)
        encoding = np.zeros((dimension, dimension))
        for x in sector:
            i = lookup[int(x)]
            complement[lookup[int(x)^full_mask], i] = 1
            if chain.bits[x, 0] == 0:
                j = lookup[int(x)^full_mask]
                encoding[np.ix_([i, j], [i, j])] = np.array([[1, 1], [1, -1]])/np.sqrt(2)
        require_close(encoding @ encoding.T, np.eye(dimension), "sector encoding is unitary")
        conjugation_error = require_close(encoding @ z_first @ encoding.T, complement,
                                          "logical Hadamard maps density to complement")
        time = 0.7
        p = (1-exp(-2*chain.flip_rate*time))/2
        kraus = []
        for mask in range(chain.size):
            weight = p**mask.bit_count() * (1-p)**(chain.length-mask.bit_count())
            projected = np.zeros((dimension, dimension))
            for column, x in enumerate(sector):
                target = int(x) ^ mask
                if target in lookup:
                    projected[lookup[target], column] = np.sqrt(weight)
            kraus.append(projected)

        def channel(matrix):
            return sum(k @ matrix @ k.T for k in kraus)

        maximally_mixed = np.eye(dimension)/dimension
        pass_probability = float(np.trace(channel(maximally_mixed)))
        stationary_error = require_close(channel(maximally_mixed),
                                          pass_probability*maximally_mixed,
                                          "projected quantum reference channel")
        coherence_error = require_close(channel(maximally_mixed@complement),
                                         pass_probability*maximally_mixed@complement,
                                         "projected channel preserves complement coherence")
        amplitude = 0.23
        original = maximally_mixed @ (np.eye(dimension)+amplitude*z_first)
        encoded = encoding @ original @ encoding.T
        retained = channel(encoded)/pass_probability
        decoded = encoding.T @ retained @ encoding
        recovery_error = require_close(decoded, original, "coherent encoding and recovery escape")
        # The same fixed operator also commutes with every physical SWAP.
        swap_errors = [require_close(
            s[np.ix_(sector, sector)] @ complement,
            complement @ s[np.ix_(sector, sector)], "complement commutes with SWAP")
            for s in chain.swap_permutations]
        results.append({"N": n, "sector_dimension": dimension,
                        "time": time, "flip_rate": chain.flip_rate,
                        "pass_probability": pass_probability,
                        "encoded_amplitude": amplitude,
                        "errors": {"unitary_conjugation": conjugation_error,
                                   "stationary_state": stationary_error,
                                   "coherence": coherence_error,
                                   "decoded_state": recovery_error,
                                   "swap_commutation": max(swap_errors)}})
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="write the complete finite-check record")
    args = parser.parse_args()
    report = {
        "scope": "Finite checks; analytical proofs own universal and asymptotic claims.",
        "environment": {"python": platform.python_version(), "numpy": np.__version__,
                        "scipy": scipy.__version__},
        "generator_and_kernel_checks": check_generators_and_kernels(),
        "schedule_and_information_checks": check_schedules_and_information(),
        "random_schedule_label_check": check_random_schedule_labels(),
        "finite_amplitude_checks": check_finite_amplitudes(),
        "exact_rational_moment_checks": check_exact_moment_inequality(),
        "zeno_and_boundary_checks": check_zeno_limit_and_n_one_boundary(),
        "coherent_control_escape_checks": check_coherent_control_escape(),
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2, sort_keys=True)+"\n")
    print(json.dumps({"status": "passed", "environment": report["environment"],
                      "sections": [key for key in report if key not in {"scope", "environment"}],
                      "output": str(args.output) if args.output else None}, indent=2))


if __name__ == "__main__":
    main()
