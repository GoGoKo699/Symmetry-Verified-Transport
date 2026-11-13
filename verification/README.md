# Reproduce the finite checks

The checks reconstruct the monitored experiment from its full stochastic
generator, including rejected attempts. They test the exact formulas and the
model boundaries on small systems. The analytical proofs establish the
statements for arbitrary size and every allowed finite schedule.

From the repository root, with Python 3.12:

```bash
python -m pip install -r verification/requirements.txt
python verification/checks.py
```

To save a new complete result record:

```bash
python verification/checks.py --output verification/new_results.json
```

The saved [reference results](reference_results.json) were produced with Python
3.12.14, NumPy 2.3.5 and SciPy 1.17.0. The latter two versions are pinned in
[requirements.txt](requirements.txt). Successful execution prints
`"status": "passed"`; failed assertions terminate with an error. Floating-point
results need not be identical in their last digits across numerical libraries.

## What is constructed independently

For $`L=2N`$ sites, the program enumerates all $`2^L`$ bitstrings. It constructs
each nearest-neighbor SWAP permutation and each single-site flip explicitly,
then adds their continuous-time generators. Columns act on probability
vectors. In this convention, a SWAP on each ring bond has rate $`J`$ and each
site flips at rate $`\gamma`$.

```math
Q=J\sum_{\langle j,k\rangle}(S_{jk}-I)
  +\gamma\sum_j(X_j-I).
```

SciPy exponentiates this full generator. Each charge check then removes the
probability outside the balanced sector, without renormalizing. Products of
these unnormalized maps retain the cost of every failed attempt. This route
does not build the monitored dynamics from the claimed conditional-eigenvalue
formula.

| Check | Construction and comparison |
|---|---|
| Interval factorization | Compare the exponential of the combined generator with separately exponentiated SWAP and flip generators; check their commutator. |
| Conditional kernel | Restrict the exponentiated full flip generator to balanced inputs and outputs; compare all matrix entries and all input pass probabilities with the stated kernel. |
| Harmonic attenuation | Apply those matrices to degree-$`r`$ products for $`1\le r\le N`$. For complete schedules, compare the full monitored map with the independently exponentiated ideal transport map times the claimed attenuation. |
| Complete outcome information | Propagate the reference probability vector and its exact derivative in the initial amplitude $`u`$. Enumerate every accepted bitstring and every rejected check-index/charge outcome. |
| Raw baseline | Evolve once without checks, keeping every bitstring. Compute the density response and variance directly, then compare the sample-mean information with the checked experiment's entire record. |
| Finite amplitudes and sample counts | Separately propagate actual source laws at $`u=\pm v`$. Compare their full-transcript relative entropy, offzero Fisher information, raw second moment and variance, and finite-sample estimator MSE with the stated formulas. |
| Random schedule labels | Mix three schedules. Calculate the information both with and without the schedule label, and check the accepted-mixture attenuation inequality. |
| Moment inequality | Use exact `Fraction` arithmetic at five rational flip probabilities, including zero and one half. Check adjacent log-convexity and the finite chord inequality through $`N=8`$. |
| Restoration limit | At fixed $`N=2`$, increase the number of equal intervals from one to 64 and check approach toward the stated acceptance and attenuation endpoints. |
| Scope boundaries | Exhibit a finite $`N=1`$ information improvement and construct the coherent complement-pair encoding that escapes a claim allowing arbitrary coherent encoding and recovery. |

For the information checks the initial law is $`\mu_N(1+u f)`$, where $`f`$ is
the real longest-wavelength Fourier density mode. The initial comparisons use
$`u=0`$. Additional finite-amplitude checks use margins $`\beta=0.2,0.75`$,
$`u_* = \beta/\max_{\Omega_N}|f|`$, and $`v=u_*/4,u_*`$, for $`N=2,3`$ and both
a final-only and an unequal four-interval schedule. Actual probability vectors
at $`+v`$ and $`-v`$ are propagated separately, alongside the exact derivative
used for Fisher information. Finite differences and Monte Carlo sampling are
not used. The [information proof](../science/information.md) and
[finite-sample proof](../science/finite_sample.md) state the full quantifiers.

## Observed results

The full-generator comparisons use $`N=2,3`$. The schedule checks include one
final check, an unequal four-interval schedule, and eight equal intervals. The
largest absolute residual among the generator, kernel, harmonic, information,
variance, finite-sample MSE and coherent-channel comparisons was
$`7.11\times10^{-15}`$. The
acceptance threshold used by the script is $`2\times10^{-10}`$.

The following entries use $`J=0.43`$, $`\gamma=0.37`$ and total time $`T=1`$.
Information is per initialized attempt, with the same unnormalized density
mode throughout each row's comparison.

| $`N`$ | Check schedule | Acceptance | Retained density attenuation | Checked full-record information | Raw density-moment information |
|---:|---|---:|---:|---:|---:|
| 2 | Final check only | 0.451342 | 0.648869 | 0.0226851 | 0.0336776 |
| 2 | Eight equal intervals | 0.252161 | 0.934135 | 0.0262675 | 0.0336776 |
| 3 | Final check only | 0.368584 | 0.584239 | 0.0479145 | 0.0995037 |
| 3 | Eight equal intervals | 0.133184 | 0.903333 | 0.0413901 | 0.0995037 |

All rejected charge/failure-time derivatives vanish to numerical precision;
the largest magnitude in these schedule tests was $`3.82\times10^{-17}`$.
The randomized-schedule example gives information 0.0443650 with its label and
0.0440353 without it, compared with 0.0995037 for the raw density moment.
Keeping the label helps within this mixture but does not overturn the raw
baseline comparison.

The finite-amplitude checks directly calculate the relative entropy of every
permitted transcript atom. Their ratios to
$`2v^2s^2h^2V/(1-\beta^2)`$ lie between 0.2119 and 0.8839. For example, at
$`N=3`$, $`\beta=0.75`$ and $`v=u_*=0.375`$, the unequal schedule gives relative
entropy 0.0121374, below its bound 0.0557324. The independently drawn schedule
label is also included in a joint label/outcome distribution; its direct
relative entropy agrees with the conditional average to within
$`3.26\times10^{-18}`$.

At both signs of each tested nonzero amplitude, the raw second moment agrees
with its zero-amplitude value. The script verifies the exact variance and MSE
formulas. For one and two attempts it enumerates the estimator outputs and
their joint probabilities directly; for seven attempts it uses exact iid
moments. The largest MSE identity residual was $`7.11\times10^{-15}`$. These
finite calculations complement the proof for arbitrary sample counts; they do
not establish the minimax lower bound or every adaptive schedule policy.

At fixed $`N=2`$, $`\gamma=0.31`$ and $`T=0.8`$, 64 equally spaced checks give
attenuation 0.996164 and acceptance 0.372979. The limiting acceptance is
$`e^{-2N\gamma T}=0.370834`$. This finite sequence illustrates the fixed-size
limit; it does not test an interchange of size and cadence limits.

## Why the boundaries are tested

The no-improvement information statement requires $`N\ge2`$. At $`N=1`$,
$`\gamma T=1`$ and eight equal intervals, the checked information is 0.105670,
whereas the raw density-moment information is 0.0359724. The script requires
this strict reversal, so deleting the size condition would fail a concrete
example. The SWAP rate is zero in this boundary test, avoiding a convention
about parallel bonds in a two-site periodic chain.

The coherent-control example uses an additional operation excluded from the
monitored density experiment. Within each balanced sector, the program builds
a Hadamard on every complementary pair of bitstrings. It verifies that this
unitary maps a first-site density operator to the global complement operator.
It then constructs every projected quantum bit-flip Kraus operator and applies
the resulting channel to off-diagonal density matrices. The encoded amplitude
survives conditioning, and decoding recovers the original state, with residual
below $`3.34\times10^{-16}`$ for $`N=1,2`$.

This is a finite counterexample to extending the density-only theorem to
arbitrary coherent encoding and recovery. It does not demonstrate efficient
geometric synthesis, an unknown-state quantum memory, or free implementation
of the extra unitary.

## Limits of the evidence

These are deterministic small-system calculations and exact rational finite
checks. They do not certify universal inequalities, asymptotic exponents,
optimal cadence, global estimation risk, novelty, hardware performance or a
practical quantum advantage. The dense full-generator implementation is used
for verification and has exponential memory cost in the number of sites.

The Fisher-information and finite-sample calculations concern the specified
affine initial density-wave family at the stated finite grid of amplitudes.
They are not quantum-Fisher-information bounds, universal transport-parameter
bounds, or analyses of unrestricted microscopic readout on rejected runs. The
script includes the rejected total-charge record that the model permits;
measuring additional rejected microscopic configurations would define a
different experiment. General adaptive-across-attempts lower bounds rely on
the analytical relative-entropy chain-rule argument.
