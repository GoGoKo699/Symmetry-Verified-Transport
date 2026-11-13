# From Watrous to symmetry-verified transport

Imagine four positions containing two particles. Random exchanges move the particles without changing their number. Noise can remove one particle and insert another elsewhere. A number check accepts that history, although the spatial pattern has changed. The project asks how much repeated number checking can restore that pattern, and how many initialized runs this restoration consumes.

## The selected source and a short reading route

The single anchor is **John Watrous, _The Theory of Quantum Information_ (Cambridge University Press, 2018)**, [publisher DOI](https://doi.org/10.1017/9781316848142). The [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/) supplies personal-use manuscript links. Section numbers and printed page numbers below follow that manuscript's standard layout; the manuscript itself is not redistributed here.

| Anchor section | Use in this project |
|---|---|
| §1.2.2, pp. 47–52 | Probability distributions, expectations and independent random outcomes. |
| §§2.1.1–2.1.2, pp. 58–66 | A spin register, a classical occupation law and its diagonal density operator. |
| §§2.2.1–2.2.2, pp. 72–90 | Channels, complete positivity, trace preservation and Kraus descriptions; see Theorem 2.22. |
| §§2.3.1–2.3.2, pp. 100–112 | Measurement outcomes; especially nondestructive measurements and instruments on pp. 111–112, Eqs. (2.257)–(2.262). |
| §3.1.1, pp. 125–131 | Binary discrimination and the Holevo–Helstrom theorem, Theorem 3.4. |
| §§5.1.1–5.1.2, pp. 250–264 | Classical relative entropy and Pinsker's inequality, Theorem 5.15 on p. 263. |

Start with the state/channel/measurement entries for the physical experiment. Use discrimination and relative entropy when reaching the finite-sample argument. The local derivations below explain the connection as those concepts become necessary.

## Translate the notation and assumptions

| Book language | Project language and meaning |
|---|---|
| A register with a classical state set | The spin chain has occupation strings $`x\in\{0,1\}^{2N}`$. The allowed initial strings lie in $`\Omega_N=\{x:\sum_jx_j=N\}`$. |
| Standard basis vectors $`e_x`$ | The repository writes $`|x\rangle`$; $`e_xe_x^*`$ becomes $`|x\rangle\langle x|`$. |
| A state $`\rho\in\mathrm D(\mathcal X)`$ | A probability law $`q(x)`$ becomes $`\rho=\sum_xq(x)|x\rangle\langle x|`$. The channel identities also cover coherent balanced-sector states. |
| A channel $`\Phi`$ and adjoint $`\Phi^*`$ | The noise channel is $`\mathcal E_p`$; the repository uses $`\dagger`$ for an adjoint acting on observables. |
| Instrument branches $`\Phi_a`$ | The charge-$`q`$ branch is $`\rho\mapsto\Pi_q\rho\Pi_q`$. Its trace is the outcome probability. |
| A measurement often denoted $`\mu`$ | Here $`\mu_N`$ instead means the uniform half-filled state or law; charge projectors are $`\Pi_q`$. |
| Relative entropy $`D(p\Vert q)`$ with base-two logarithms | Project $`D_{\rm KL}`$ uses natural logarithms: $`D_{\rm KL}=(\ln2)D_{\rm book}`$. The separate symbol $`D`$ in the transport generator is an exchange rate. |

The book's usual measurement definition destroys the measured register. Its instrument formulation describes the nondestructive checks needed here. Retaining the outcome and retaining the postmeasurement spin state are distinct parts of the experiment.

## A check produces a branch, not a free replacement state

For one noisy interval, the accepted unnormalized output is

```math
\mathcal L_p(\rho)=\Pi_N\mathcal E_p(\rho)\Pi_N.
```

Its trace $`P_N(p)`$ is the chance that this initialized run passes. The retained state is $`\mathcal L_p(\rho)/P_N(p)`$. This normalization describes a selection event; failed initializations remain part of its cost.

For the present homogeneous flip noise, $`P_N(p)`$ is the same for every initial state supported on $`\Omega_N`$. Thus

```math
\mathcal K_p=\mathcal L_p/P_N(p)
```

is a linear, trace-preserving channel on that sector. A generally state-dependent normalization would not have this property. [Conditional dynamics](../science/conditional_dynamics.md) proves input independence from the charge distribution rather than assuming it.

An entire transcript records the schedule, the charge outcomes, and a final microscopic bitstring only on the all-pass branch. This record definition matters when comparing information. An initial microscopic measurement, a preparation bitstring retained elsewhere, or microscopic measurements on rejected runs would supply additional data.

## Follow the four-spin experiment

Take $`N=2`$, so six occupation strings have two particles. Choose the spatial mode

```math
f(x)=x_1-x_3,\qquad
\Pr_u(X=x)=\frac{1+u f(x)}6,\qquad x\in\Omega_2.
```

The value of $`f`$ is $`+1`$ on two strings, $`-1`$ on two, and zero on two. Hence its uniform mean is zero and its variance is $`V=2/3`$. Positive $`u`$ makes occupation at position 1 more likely relative to position 3. The source is supplied without revealing its drawn initial string.

Use one final check and choose the total noise so that $`s=e^{-2\gamma T}=1/2`$. Each spin then has net flip probability $`p=(1-s)/2=1/4`$. Passing requires the same number of initially occupied and initially empty spins to flip. Zero, one or two such pairs give

```math
P_2=(1-p)^4+4p^2(1-p)^2+p^4=\frac{59}{128}.
```

The terms with one pair explain the undetected error: one particle disappears while another appears elsewhere, leaving the count unchanged.

The project computes how this selection changes the spatial mode. With $`P_1=(1-p)^2+p^2=5/8`$, its relative retained attenuation is

```math
A_1=s\frac{P_1}{P_2}=\frac{40}{59}.
```

Let $`h=e^{-\omega T}`$ be the attenuation due to ideal exchange alone. The unverified mean is $`u h sV`$; the accepted mean is $`u h A_1V`$. Because $`40/59>1/2`$, each retained run has a stronger spatial response. Only $`59/128`$ of initialized runs remain.

### Count information before discarding failures

For a classical outcome law $`p_u(y)`$, Fisher information is

```math
I(u)=\sum_y\frac{(\partial_u p_u(y))^2}{p_u(y)}.
```

The derivative $`\partial_u p_u(y)`$ is the rate at which an outcome probability changes with $`u`$. Fisher information measures the local sensitivity of the complete outcome distribution. At zero amplitude, the all-pass probability and charge-only failure record carry no $`u`$ information. The full accepted bitstring therefore gives $`I_{\rm check}(0)=P_2h^2A_1^2V`$ per initialized attempt.

The raw experiment retains every final bitstring. Its simple sample mean of $`f`$ has variance coefficient $`a_2=(3+s^2)/4=13/16`$. The reciprocal asymptotic variance it achieves is $`J_{\rm raw}(0)=s^2h^2V/a_2`$.

| Same-time experiment | Retained relative amplitude | Information measure divided by $`h^2V`$ |
|---|---:|---:|
| Final charge check | $`40/59`$ | Full checked-record Fisher information $`25/118\approx0.212`$ |
| Raw readout, keep every run | $`1/2`$ | Achieved sample-mean inverse variance $`4/13\approx0.308`$ |

The second entry is an attainable estimator performance, not an asserted formula for the entire raw bitstring's Fisher information. Even this simple raw estimator beats the checked record's local information in this example. [The complete example](../science/worked_example.md) gives its canonical calculation.

## Why another check schedule cannot remove the price

The book supplies channels and instruments; the following dynamical structure is derived in the project. Stochastic SWAP transport consists of random site permutations. Homogeneous independent flips commute with those permutations, and total-charge projection does too. Accepted intervals therefore compose as charge-conditioned noise beside the same ideal transport.

For every interval the return probabilities have a positive moment representation

```math
P_M(p)=\mathbb E[W^M],\qquad
W=1-4p(1-p)\sin^2(\Phi/2)\in[0,1],
```

where $`\Phi`$ is uniform on the circle. Hölder's inequality gives $`P_{N-1}\le P_N^{1-1/N}`$. Combining this with $`\lambda_1=e^{-2\gamma\Delta}P_{N-1}/P_N`$ and multiplying over intervals yields

```math
A_1\le e^{-2\gamma T}P^{-1/N}.
```

Thus a retained gain $`G=A_1/e^{-2\gamma T}`$ costs at least $`G^N`$ attempts per accepted run. This statement holds for every finite cadence. Independently randomized schedules satisfy it after the correct acceptance weighting; keeping their labels also satisfies the schedulewise information bound.

For $`N\ge2`$, the same inequality implies $`PA_1^2\le s^2`$. It is this model-specific fact, rather than normalization alone, that produces the full checked-record comparison. See [Cadence](../science/cadence_tradeoff.md) and [Information](../science/information.md). Higher-degree difference modes have their own exact noise factors; their ideal SSEP evolution is generally not a single scalar Fourier rate.

## From local sensitivity to finite-sample inference

Watrous's binary-discrimination theorem connects distinguishability with testing. For classical distributions, the relevant distance is $`\operatorname{TV}(p,q)=\frac12\sum_y|p(y)-q(y)|`$. With equal priors, the smallest testing error is $`(1-\operatorname{TV})/2`$.

The book's classical Pinsker theorem becomes $`\operatorname{TV}^2\le D_{\rm KL}/2`$ after converting its base-two entropy to natural logarithms. The project's likelihood calculation bounds the divergence between two amplitudes $`+v`$ and $`-v`$ by

```math
D_{\rm KL}(\mathsf P_{+v}^{(m)}\Vert\mathsf P_{-v}^{(m)})
\le\frac{2m v^2 S}{1-\beta^2},\qquad
S=s^2h^2V.
```

Here $`m`$ counts all initialized attempts. The source interval is $`|u|\le u_*:=\beta/F`$, where $`F=\max_{\Omega_N}|f|`$ and $`0<\beta<1`$. This margin keeps likelihoods positive. It can shrink with size for an unnormalized Fourier sum.

The proof expands conditional transcript probabilities, so it also handles schedules chosen from earlier attempts' records. Small divergence means the two amplitudes remain hard to tell apart. Any accurate estimate would determine their sign, which turns the testing bound into the minimax risk bound

```math
\mathcal R_m\ge\frac14\min\left\{u_*^2,
\frac{1-\beta^2}{4mS}\right\}.
```

Here $`\mathcal R_m`$ is the smallest worst-case mean squared error over the declared interval, optimized over all estimators of the permitted record. This covers biased estimators. The explicitly constructed raw estimator has worst-case MSE at most $`\min\{u_*^2,a_N(s)/(mS)\}`$. The comparison is within fixed $`\beta`$-dependent constants; exact local information dominance is stated at $`u=0`$. [Finite-sample inference](../science/finite_sample.md) supplies the full argument and quantifiers.

## What the project supplies beyond the anchor

| Locally supplied step | Authoritative source |
|---|---|
| Stochastic SWAP generator, flip-rate convention and late-readout contract | [Model](../science/model.md) |
| Balanced-return polynomial, conditional kernel and harmonic eigenvalues | [Conditional dynamics](../science/conditional_dynamics.md) |
| Positive moments, Hölder application, random schedules and limiting cadence | [Cadence and acceptance](../science/cadence_tradeoff.md) |
| Fisher sensitivity, raw variance, likelihood calculation and adaptive classical KL chain rule | [Information](../science/information.md) and [finite samples](../science/finite_sample.md) |
| Testing-to-MSE reduction, shrinking interval and explicit estimator | [Finite samples](../science/finite_sample.md) |

These project derivations are not attributed to the textbook. The book is not used as a source for an SSEP theorem, the all-cadence inequality, or the adaptive statistical result.

## Integrate the conclusion and its boundaries

The [30-milestone map](milestones.md) uses M01–M12 for the background experiment and M13–M30 for the argument's components and synthesis. The four-spin example connects the two phases: the same $`P,A_1,h,V`$ enter both the physical visibility and the initialized-attempt information comparison.

For growing $`L`$, fixed positive $`D,\gamma`$ and a longest-wavelength observation time $`T=\Theta(L^2/D)`$, restoring any fixed positive fraction of the ideal density signal requires $`P^{-1}=\exp[\Omega(\gamma L^3/D)]`$. Inferring a small amplitude from a calibrated, attenuated raw signal has a different sampling dependence. The result does not globally optimize estimation of an unknown diffusion constant.

The information comparison requires $`N\ge2`$. Two sites provide a genuine exception, and extra coherent encoding can protect an amplitude outside the diagonal-density experiment. [Controls and limits](../science/controls_and_limits.md) gives both constructions and explains why neither reproduces arbitrary unknown unencoded transport. Generic charge-conserving Hamiltonians also need their own commutation analysis.

[Learning route](README.md) · [Milestones](milestones.md) · [Scientific overview](../science/README.md) · [Attribution](../references/RELATED_WORK.md)
