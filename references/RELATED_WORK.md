# Prior work and the contribution retained here

The addition is the exact finite-size relation

```math
A_r\le e^{-2r\gamma T}P^{-r/N}
```

for every allowed global-charge-check cadence in the half-filled random-SWAP model, and its retained-record information comparison with an explicit same-time raw estimator for $`N\ge2`$. Exponential postselection overhead, first-order detection, undetectable errors and the sampling penalty of discarded attempts are established ideas.

## Transport coefficients and noise

**Hansveer Singh, Pieter W. Claeys, Sarang Gopalakrishnan and Anushya Chandran**, *Zero noise extrapolation of transport coefficients*, [arXiv:2611.05481v1](https://arxiv.org/abs/2611.05481v1), 3 November 2026.

Their interacting spin-chain and fracton examples extract transport coefficients from noisy linear response. The two-rate ansatz separates uniform charge decay from wavevector-dependent transport; hydrodynamic tails can make the noise dependence nonanalytic. Those mechanisms and the two-rate fitting idea are inherited.

Here the ideal dynamics are random-SWAP/SSEP and the question concerns repeated charge postselection at one noise strength. The conditional kernel and every-cadence bound are derived explicitly. This does not refute two-rate inference or establish the same theorem for Heisenberg dynamics.

**Inspection:** versioned abstract and HTML introduction, density-wave setup, Sec. III, stationary-state discussion and conclusions; especially Eqs. (1), (17) and the repeated-preparation discussion.

## Dynamical postselection and symmetry expansion

**Edoardo Ballini, Julius Mildenberger, Matteo M. Wauters and Philipp Hauke**, *Symmetry verification for noisy quantum simulations of non-Abelian lattice gauge theories*, [Quantum **9**, 1802 (2025)](https://doi.org/10.22331/q-2025-07-22-1802); [arXiv:2412.07844v3](https://arxiv.org/abs/2412.07844v3), 15 July 2025.

They develop dynamical postselection and postprocessed verification for non-Abelian lattice gauge theories. Their introduction explicitly states exponential overhead and distinguishes the methods' mid-circuit measurement requirements. Repeated verification, its Zeno mechanism and generic exponential overhead are not discoveries here.

The present scalar global charge differs from extensive local Gauss-law constraints. Its added conclusion is an attenuation–acceptance relation and retained-bitstring information comparison uniform over allowed check times.

**Inspection:** versioned metadata, abstract and complete introduction, including the overhead statement; no full gauge-theory proof audit.

**Zhenyu Cai**, *Quantum Error Mitigation using Symmetry Expansion*, [Quantum **5**, 548 (2021)](https://doi.org/10.22331/q-2021-09-21-548); [arXiv:2101.03151v3](https://arxiv.org/abs/2101.03151v3).

The broad bias–sampling tradeoff and detectable/undetectable distinction belong to this established framework. This source does not supply the dynamic all-cadence inequality. **Inspection:** publisher abstract, summary and bibliographic record.

## Finite-shot symmetry verification

**Vicenzo Scavino Alfaro**, *Finite-Shot Operating Windows for Virtual Distillation and Symmetry Verification*, [arXiv:2606.15464](https://arxiv.org/abs/2606.15464) and the [author's source repository](https://github.com/vicenzoscavino1999/finite-shot-vd-sv/blob/main/paper/main.tex).

The inspected author source derives projected first-order bias, acceptance-dependent variance, Bernoulli postselection quotient cancellation and restricted fixed-transcript inference bounds. These already explain why reduced bias alone cannot establish a finite-budget benefit. Accepted-transcript information accounting is also inherited.

The remaining dynamical question is which acceptance and retained state a sequence of checks produces. The exact kernel, harmonic attenuation and all-cadence law answer it before comparing estimators.

**Inspection and version boundary:** the author's `paper/main.tex` was read at blob `9a6423d270c7e329748f008ce481786f3ddbff00`, especially the symmetry-verification and restricted-inference sections. It has the title above, an anonymous author line and a 29 May 2026 date. The canonical arXiv index identifies Scavino Alfaro but exposes an earlier “Certified” title. Direct v3 retrieval was unavailable; equivalence of this snapshot to v3 is not asserted. No fixed-Hamming-weight-specific theorem is attributed from this snapshot.

## Channel verification and correction

**Kento Tsubouchi, Yosuke Mitsuhashi, Ryuji Takagi and Nobuyuki Yoshioka**, *Symmetric channel verification for purifying noisy quantum channels*, [PRX Quantum **6**, 040310 (2025)](https://doi.org/10.1103/jcd6-lft3); [arXiv:2503.13114v3](https://arxiv.org/abs/2503.13114v3), 20 October 2025.

They coherently verify channel symmetry and include virtual verification and feedback correction. These operations are stronger than measuring total charge and rejecting failures. Their correction result is not constrained by a bound excluding correcting feedback.

The [coherent encoding](../science/controls_and_limits.md#a-coherent-encoding-preserves-an-amplitude-at-every-size) here makes the boundary concrete: it protects an amplitude but does not implement unknown unencoded transport.

**Inspection:** versioned metadata, introduction, setup and Sec. V's correction discussion/Theorem 2; no reproduction of the full channel-purification analysis.

## Postselected metrology

**David R. M. Arvidsson-Shukur, Nicole Yunger Halpern, Hugo V. Lepage, Aleksander A. Lasek, Crispin H. W. Barnes and Seth Lloyd**, *Quantum advantage in postselected metrology*, [Nature Communications **11**, 3775 (2020)](https://doi.org/10.1038/s41467-020-17559-w); [arXiv:1903.02563v3](https://arxiv.org/abs/1903.02563v3), 25 September 2020.

This paper relates postselected information-to-cost advantages to noncommutativity and gives a classical-commuting limit for its optimized prepare–measure task. Here the unknown is an initial distribution amplitude and repeated checks intervene during noisy dynamics. The fixed raw comparator and attempt convention differ. That theorem alone does not imply the present all-cadence result; the two-site exception prevents a blanket commuting-process slogan.

**Inspection:** canonical arXiv metadata/abstract and publisher-indexed abstract/classical-limit statement. Direct full text was unavailable in this review.

## Comparison scope

These sources support the attribution and model differences; they do not establish exhaustive priority or replace this repository's proofs. The result is an analytical benchmark for verification, with no claim of quantum computational advantage over classical simulation.

[Scientific account](../science/README.md) · [Controls and limits](../science/controls_and_limits.md) · [BibTeX](references.bib)

