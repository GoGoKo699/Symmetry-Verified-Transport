# Scientific overview

A density wave contains spatial information: some sites are a little more occupied than others. Exchange moves that information diffusively while preserving the total number of particles. Independent flips violate that conservation law. A global number measurement rejects runs with an incorrect final charge, but it cannot identify a particle that was removed at one location and inserted elsewhere.

The question is how far repeated global checks can repair this loss once every rejected attempt is counted. The answer follows from an exact conditional noise kernel rather than a small-noise approximation.

## Connected argument

1. The [model](model.md) defines a fixed late-readout experiment on a half-filled spin chain. Stochastic SWAP transport and homogeneous independent flips commute. Global checks therefore reduce to composing charge-conditioned flip kernels alongside the given ideal transport.
2. The [conditional-dynamics chapter](conditional_dynamics.md) computes their pass probability and harmonic eigenvalues. Linear spatial density modes lie in the first harmonic sector.
3. The [cadence theorem](cadence_tradeoff.md) represents pass probabilities as moments of a nonnegative random variable. Log-moment convexity gives a bound that holds separately for every time interval and therefore for every finite schedule. Random schedule labels are treated explicitly.
4. The [information chapter](information.md) grants the checked protocol its complete accepted microscopic output. It compares that record's local information with the attainable variance of a raw density-moment estimator at the same time.
5. The [finite-sample chapter](finite_sample.md) uses two-point testing to constrain every estimator, including biased ones, and gives a clipped raw estimator with matching noise and time dependence. Its permitted amplitude interval is part of the statistical task and can depend on chain size.
6. The [four-spin example](worked_example.md) shows explicitly that a stronger conditional signal can coexist with less information per initialized run.
7. The [controls chapter](controls_and_limits.md) explains the two-spin exception and a coherent encoding that changes the conclusion. It also separates retained-signal restoration from unrestricted transport inference.

## What the bound controls

Write $`L=2N`$, use flip rate $`\gamma`$ per site, and let $`P`$ denote all-check acceptance. If $`A_r`$ is the relative noise attenuation in harmonic degree $`r`$, then

```math
A_r\le e^{-2r\gamma T}P^{-r/N},\qquad 1\le r\le N.
```

The density case is $`r=1`$. A fixed retained density visibility at diffusive times costs exponentially many initialized attempts in volume times noise rate times duration. The information comparison additionally requires $`N\ge2`$ and the declared local amplitude experiment. Perfect charges in accepted shots are thus insufficient to infer efficient recovery of the measured spatial response.

## Evidence and attribution

The general statements follow from the kernel calculation, the moment inequality and the statistical argument. The [verification suite](../verification/README.md) independently checks finite generators, complete records and boundary cases. The [related-work account](../references/RELATED_WORK.md) attributes the established symmetry-verification, transport and statistical tools. No hardware runtime advantage or general error-mitigation impossibility is asserted.
