# Finite-sample inference from verified and raw responses

The local information comparison can be made into an explicit finite-sample statement without assuming that an estimator is unbiased. This section uses the same fixed late-readout amplitude experiment as [the information account](information.md).

## Parameters, records and risk

Fix finite $`L=2N\ge4`$, observation time $`T`$, flip rate $`\gamma`$, and a real SSEP density eigenmode $`f`$ with ideal attenuation $`h=e^{-\omega T}`$. Write
```math
s=e^{-2\gamma T},\qquad
V=\mathbb E_{\mu_N}f^2,\qquad
S=s^2h^2V>0.
```
For $`F=\max_{\Omega_N}|f|`$ and fixed $`0<\beta<1`$, the source family is
```math
\Pr_u(X=x)=\mu_N(x)[1+u f(x)],\qquad
|u|\le u_*:=\frac{\beta}{F}.
```

The budget $`m\ge1`$ counts initialized attempts. Each attempt uses a fresh source state. A checked protocol may choose any allowed finite charge-check schedule ending in a final check at $`T`$, randomize it and retain its label. It may also choose the next attempt's schedule using earlier permitted records. Within an attempt, it has no correcting feedback or microscopic information before the final readout. A rejected attempt returns its charge-only failure record, not its microscopic configuration. No input preparation label, purification or initial microscopic measurement is supplied.

The unknown source amplitude is the only parameter varied in the following minimax risk:
```math
\mathcal R_m(\mathcal P)
:=\inf_{\widehat u}
\sup_{|u|\le u_*}
\mathbb E_u[(\widehat u-u)^2].
```
Here $`\mathcal P`$ denotes a fixed admissible $`m`$-attempt checked protocol, including its schedule policy. The infimum is over every estimator of its complete permitted transcript, with arbitrary estimator bias and classical randomization.

All lower bounds below are uniform over $`\mathcal P`$. The raw upper bound uses a separately specified experiment with no checks.

## A finite two-point distinguishability bound

Consider two source amplitudes $`u=+v`$ and $`u=-v`$, where $`0<v\le u_*`$. For one fixed schedule, put $`b=hA`$. Its successful bitstring distribution is
```math
q_{\pm v}(y)=\mu_N(y)[1\pm v b f(y)],
```
with success probability $`P`$ independent of the sign. All charge-only failure outcomes have the same probability in the two hypotheses. Thus the relative entropy of the entire one-attempt transcript is exactly
```math
D_{\mathrm{KL}}(\mathsf P_{+v}\Vert\mathsf P_{-v})
=P\,\mathbb E_{\mu_N}
\left[(1+a)\log\frac{1+a}{1-a}\right],
\qquad a=v b f.
```
Complementation makes the distribution of $`a`$ symmetric. The expectation of the odd logarithm is consequently zero, leaving
```math
D_{\mathrm{KL}}(\mathsf P_{+v}\Vert\mathsf P_{-v})
=P\,\mathbb E_{\mu_N}
\left[a\log\frac{1+a}{1-a}\right].
```
For $`|a|\le\beta<1`$,
```math
0\le a\log\frac{1+a}{1-a}
=2a\operatorname{atanh}a
\le\frac{2a^2}{1-\beta^2}.
```
The cadence bound $`PA^2\le s^2`$ therefore gives
```math
\boxed{\;
D_{\mathrm{KL}}(\mathsf P_{+v}\Vert\mathsf P_{-v})
\le\frac{2v^2S}{1-\beta^2}.
\;}
```

If a random schedule label is retained, relative entropy is averaged conditional on that label. The same bound applies to every schedule, so it survives this averaging. If schedules are chosen adaptively between attempts, condition on the previous transcript: the policy for choosing the next schedule is the same rule under both hypotheses, and each conditional one-attempt divergence obeys the displayed bound. The relative-entropy chain rule then yields
```math
D_{\mathrm{KL}}(\mathsf P_{+v}^{(m)}\Vert
\mathsf P_{-v}^{(m)})
\le\frac{2m v^2S}{1-\beta^2}.
```
This handles the retained labels directly. Replacing them by one averaged attenuation would describe a less informative experiment and is not needed.

## Uniform minimax mean squared error

For every admissible checked protocol and every $`m\ge1`$,
```math
\boxed{\;
\mathcal R_m(\mathcal P)
\ge\frac14
\min\left\{
u_*^2,\,
\frac{1-\beta^2}{4mS}
\right\}.
\;}
```

To prove it, choose
```math
v^2=\min\left\{
u_*^2,\,
\frac{1-\beta^2}{4mS}
\right\}.
```
The preceding divergence is at most $`1/2`$. Pinsker's inequality gives total variation distance at most $`1/2`$. Threshold any estimator at zero to test the two hypotheses $`\pm v`$. On a wrong-sign decision, its squared estimation error is at least $`v^2`$. The equal-prior testing error is at least $`(1-\operatorname{TV})/2`$, so
```math
\sup_{u\in\{-v,+v\}}
\mathbb E_u[(\widehat u-u)^2]
\ge\frac{v^2}{2}(1-\operatorname{TV})
\ge\frac{v^2}{4}.
```
The two hypotheses lie inside the declared interval. This proves the bound for biased as well as unbiased estimators.

A related bounded-error statement follows directly. If a test of $`\pm v`$ has worst-case error at most $`\delta<1/2`$, then $`\operatorname{TV}\ge1-2\delta`$. Combining this with Pinsker and the same divergence bound requires
```math
m\ge
\frac{(1-\beta^2)(1-2\delta)^2}{v^2S}.
```
This is a finite two-point bound at the stated constant confidence, not an asymptotic Cramér–Rao claim.

## An explicit raw upper bound

For the experiment with no checks, define
```math
a_N(s)=\frac{2N-1+s^2}{2N}.
```
The estimator
```math
\widehat u_{\mathrm{raw}}
=\frac{1}{mshV}\sum_{a=1}^m f(Y_a)
```
has, exactly for every $`|u|\le u_*`$,
```math
\mathbb E_u\widehat u_{\mathrm{raw}}=u,\qquad
\mathbb E_u(\widehat u_{\mathrm{raw}}-u)^2
=\frac{a_N(s)}{mS}-\frac{u^2}{m}
\le\frac{a_N(s)}{mS}.
```
Clipping the estimate to $`[-u_*,u_*]`$ cannot increase squared error. The constant estimator zero instead has worst-case risk $`u_*^2`$. Choose between these two estimators using the known values of $`m,S,a_N,u_*`$. The resulting raw estimator satisfies
```math
\boxed{\;
\sup_{|u|\le u_*}
\mathbb E_u[(\widehat u_{\mathrm{raw,clip}}-u)^2]
\le
\min\left\{u_*^2,\frac{a_N(s)}{mS}\right\}.
\;}
```
Here the notation includes using zero when its displayed guarantee is smaller. Every raw attempt is retained. The second-moment calculation, rather than a Cramér–Rao bound, proves this finite-sample upper guarantee.

## What is matched

For a target MSE $`\epsilon^2<u_*^2/4`$, every checked protocol needs
```math
m\ge\frac{1-\beta^2}{16S\epsilon^2},
```
whereas the raw estimator is sufficient whenever
```math
m\ge\frac{a_N(s)}{S\epsilon^2}.
```
Thus the raw baseline matches the checked experiment's unavoidable dependence on
```math
\frac{1}{S\epsilon^2}
=\frac{\exp(4\gamma T+2\omega T)}{V\epsilon^2},
```
up to constants depending only on the fixed weak-wave margin $`\beta`$.

This is a lower bound for all permitted checked experiments and a matching order achieved by the explicit unverified baseline. It does not assert the exact finite-sample optimum of each checked cadence, or the exact minimax risk of the complete raw bitstring experiment.

At a diffusive horizon $`T=\Theta(L^2/D)`$ for a longest-wavelength mode, $`h`$ stays bounded away from zero and one by constants determined by the chosen horizon. The sampling exponent of the raw inference baseline is then $`4\gamma T=\Theta(\gamma L^2/D)`$. In contrast, restoring an order-one accepted visibility requires acceptance overhead with exponent $`2N\gamma T=\Theta(\gamma L^3/D)`$. This compares inference from an attenuated response with physical restoration of that response; the tasks have different resource demands.

The amplitude interval and accuracy must remain explicit when $`L`$ varies. For the usual unnormalized Fourier sum, $`F`$ grows with $`L`$, so this exact affine source family allows a shrinking interval $`u_*`$. Its effects are retained in $`u_*,V,\epsilon`$. No fixed nonzero macroscopic density modulation is inferred from a formal linear-response family.

## Statistical ingredients and limits

The two-point reduction, the relative-entropy chain rule and Pinsker's inequality are standard statistical tools. Fixed-transcript lower bounds and acceptance-weighted information are also used in [Scavino Alfaro, arXiv:2606.15464](https://arxiv.org/abs/2606.15464). The new model-specific input is the all-cadence inequality $`PA^2\le s^2`$, which controls the full accepted density-response likelihood.

The result does not forbid estimating the initial amplitude by measuring it immediately, retaining preparation labels, changing the physical encoding, collecting rejected microscopic outcomes, or using a different experimental time. Those operations supply a different experiment. Nor is the amplitude minimax theorem a global minimax theorem for an unknown diffusion constant. The information account states the narrower transport-parameter consequence actually derived from this likelihood.

