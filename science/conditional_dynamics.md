# Exact conditional dynamics

The [model](model.md) has $`L=2N`$ spins, homogeneous independent flips and ideal global checks of the balanced charge sector. This page derives the retained channel and the attenuation of its density observables. No hydrodynamic approximation is used.

## One interval and its success probability

Write $`p=(1-e^{-2\gamma\Delta})/2`$ for an interval of duration $`\Delta`$, and let $`\mathcal E_p`$ be the product bit-flip channel,

```math
\mathcal E_p
 =\bigotimes_{j=1}^{2N}
 \bigl((1-p)\operatorname{id}+p\,\operatorname{Ad}_{X_j}\bigr).
```

Starting from a basis configuration with $`N`$ occupied sites, let $`A`$ count flips of initially occupied sites and $`B`$ flips of initially empty sites. Then $`A,B`$ are independent $`\operatorname{Bin}(N,p)`$ variables and the final charge is $`N-A+B`$. Returning to charge $`N`$ therefore has probability

```math
P_N(p)
 =\Pr(A=B)
 =\sum_{a=0}^{N}\binom Na^2
    p^{2a}(1-p)^{2N-2a}.
```

It depends on the input charge, not the occupied positions. For an arbitrary quantum input $`\rho=\Pi_N\rho\Pi_N`$, the charge measurement depends only on its computational-basis diagonal. Thus the same probability holds for every such density operator:

```math
\operatorname{tr}\!\left[\Pi_N\mathcal E_p(\rho)\right]=P_N(p).
```

The retained normalized map is consequently a linear channel on the balanced sector:

```math
\mathcal K_p(\rho)
 =\frac{\Pi_N\mathcal E_p(\rho)\Pi_N}{P_N(p)}.
```

It is completely positive and trace preserving on that input sector. Input-independent success is essential: normalization by a state-dependent probability would not define this linear channel.

On diagonal observables or diagonal states, $`\mathcal K_p`$ is the Markov kernel

```math
K_p(x,y)
 =\frac{p^{d_H(x,y)}(1-p)^{2N-d_H(x,y)}}{P_N(p)},
 \qquad x,y\in\Omega_N.
```

Here $`d_H`$ is Hamming distance. Each row sums to one by the preceding calculation. The kernel is symmetric, so it is reversible for the uniform measure $`\mu_N(x)=\binom{2N}{N}^{-1}`$. We use the function convention

```math
(K_pf)(x)=\sum_{y\in\Omega_N}K_p(x,y)f(y).
```

Symmetry means the same kernel can also evolve densities with respect to $`\mu_N`$. The corresponding quantum channel preserves the uniform sector state $`\mu_N=\Pi_N/\binom{2N}{N}`$: applying the product noise to $`\Pi_N`$ and then projecting back gives $`P_N(p)\Pi_N`$.

## A positive moment formula

Define $`P_M(p)`$ by the same balanced-return formula for each integer $`M\geq0`$, with $`P_0(p)=1`$. Set

```math
q=p(1-p),\qquad
B_p(z)=(p+(1-p)z)((1-p)+pz).
```

The coefficient of balanced final occupation is

```math
P_M(p)=[z^M]B_p(z)^M.
```

Since

```math
z^{-1}B_p(z)=1-2q+q(z+z^{-1}),
```

Fourier coefficient extraction gives

```math
P_M(p)
 =\frac1{2\pi}\int_{-\pi}^{\pi}
   \left[1-4q\sin^2\!\left(\frac\phi2\right)\right]^M\,d\phi.
```

For $`0\leq p\leq1/2`$, the bracket lies in $`[0,1]`$. Thus $`P_M`$ is a moment of a nonnegative random variable bounded by one. In particular, $`P_M`$ decreases with $`M`$, and $`\log P_M`$ is convex in $`M`$. The latter is the standard log-convexity of moments, equivalently Hölder's inequality. It supplies the key inequality in [Cadence and acceptance](cadence_tradeoff.md).

## Density attenuation

For two sites $`a,b`$, define $`f(x)=x_a-x_b`$. An initially equal pair, $`00`$ or $`11`$, gives zero conditional difference by exchange symmetry. For an initially opposite pair $`10`$,

```math
\begin{aligned}
\mathbb E\!\left[(Y_a-Y_b)z^{Y_a+Y_b}\mid X_aX_b=10\right]
&=(1-p)z((1-p)+pz)\\
&\quad-pz(p+(1-p)z)\\
&=(1-2p)z.
\end{aligned}
```

If the selected pair is initially opposite, the remaining sites contain $`N-1`$ occupations and $`N-1`$ vacancies. Extracting balanced final charge and dividing by $`P_N`$ gives

```math
K_p(x_a-x_b)=\lambda_1(p)(x_a-x_b),\qquad
\lambda_1(p)
 =(1-2p)\frac{P_{N-1}(p)}{P_N(p)}.
```

Every coefficient vector with zero sum is a linear combination of pair differences. Hence for every linear density mode

```math
f(x)=\sum_jc_j\left(x_j-\frac12\right),
\qquad \sum_jc_j=0,
```

the exact relation is $`K_pf=\lambda_1(p)f`$. Equivalently, on the diagonal spin observable,

```math
\mathcal K_p^\dagger(f)=\lambda_1(p)f.
```

It holds for the expectation of $`f`$ in every quantum input supported on the balanced sector.

## Higher-degree difference spaces

The argument also gives exact higher-degree identities. For $`1\leq r\leq N`$, let

```math
f_r(x)=\prod_{a=1}^{r}(x_{2a-1}-x_{2a}).
```

Let $`\mathcal H_r`$ denote the real linear span of its coordinate permutations. These are degree-$`r`$ difference spaces on the balanced slice. Only this explicit span is needed here; no completeness or irreducible-decomposition theorem is assumed.

If any selected input pair is equal, its generating-function difference vanishes. Otherwise the $`r`$ selected pairs contribute $`(1-2p)^rz^rf_r(x)`$, and the remaining sites contain $`N-r`$ occupations and $`N-r`$ vacancies. Therefore

```math
K_p f_r=\lambda_r(p)f_r,\qquad
\lambda_r(p)
 =(1-2p)^r\frac{P_{N-r}(p)}{P_N(p)}.
```

The kernel commutes with coordinate permutations, so

```math
K_p f=\lambda_r(p)f
\qquad\text{for every }f\in\mathcal H_r.
```

For $`r=1`$, $`\mathcal H_1`$ is exactly the linear zero-sum density space used above.

Every site permutation preserves $`\mathcal H_r`$ by definition. The stochastic-SWAP generator and its semigroup therefore preserve it as well. Ideal SSEP evolution need not act as one scalar on all of $`\mathcal H_r`$; the retained noise acts as a scalar and commutes with that ideal evolution.

For example, with $`\mathcal T_t^\dagger=e^{t\mathcal L_{\mathrm{tr}}^\dagger}`$,

```math
\mathcal K_p^\dagger\mathcal T_t^\dagger f
 =\lambda_r(p)\mathcal T_t^\dagger f,
 \qquad f\in\mathcal H_r.
```

A Fourier density mode is the particular $`r=1`$ case in which ideal evolution is also scalar.

The harmonic structure of the Johnson scheme is standard background. The generating-function proof establishes every identity used here directly; no conclusion is transferred from a differently defined slice-noise operator.

## Several intervals

Let $`\Delta_i`$ be an allowed schedule, $`p_i=p(\Delta_i)`$, and $`T=\sum_i\Delta_i`$. Permutation covariance of $`\mathcal E_{p_i}`$ and commutation of the projectors with permutations imply that $`\mathcal K_{p_i}`$ commutes with the ideal transport channel. Every accepted input returns to the balanced sector.

The probability of passing all checks is

```math
P=\prod_{i=1}^{m}P_N(p_i),
```

independent of the initial balanced-sector state. The normalized accepted channel is

```math
\mathcal C_{\mathrm{acc}}
 =e^{T\mathcal L_{\mathrm{tr}}}
   \mathcal K_{p_m}\cdots\mathcal K_{p_1}.
```

On each specified difference space, its adjoint satisfies

```math
\mathcal C_{\mathrm{acc}}^\dagger f
 =A_r e^{T\mathcal L_{\mathrm{tr}}^\dagger}f,\qquad
A_r=\prod_{i=1}^{m}\lambda_r(p_i),
\qquad f\in\mathcal H_r.
```

Thus $`A_r`$ is an exact noise attenuation relative to the given ideal transport. It is not an effective diffusion coefficient.

## Why the global failure record carries no input information

For one interval, not only the pass probability but the entire total-charge law is independent of the balanced input:

```math
\Pr(Q_{\mathrm{out}}=q_{\mathrm{out}})
 =\Pr(N-A+B=q_{\mathrm{out}}),
 \qquad A,B\overset{\mathrm{ind}}{\sim}\operatorname{Bin}(N,p).
```

After every successful check, the normalized state is again supported on the balanced sector. The probability that the first failure is at check $`i`$ and has charge $`q_{\mathrm{out}}\ne N`$ is therefore

```math
\left(\prod_{j<i}P_N(p_j)\right)
\Pr\!\left(N-A_i+B_i=q_{\mathrm{out}}\right).
```

This expression contains no input-state parameter. It proves input independence of the first-failure time, accepted/rejected flag and recorded global charge.

If the schedule is randomized independently of the input, conditioning on its label gives the same statement for each schedule. Including the label and permitted failure record does not add information about the input amplitude. A microscopic measurement on a rejected register could add information, but is outside the observation contract.

## Checks and boundaries

At $`p=0`$, $`P_M=1`$ and $`\lambda_r=1`$. At finite $`\gamma\Delta`$, every $`P_M`$ is positive. As $`p\to1/2`$, the density eigenvalues vanish. For $`N=r=1`$,

```math
P_1(p)=\frac{1+s^2}{2},\qquad
\lambda_1(p)=\frac{2s}{1+s^2}
 =\operatorname{sech}(2\gamma\Delta),
\qquad s=e^{-2\gamma\Delta}.
```

The two-site case is an exact boundary check. The no-benefit information comparison requires $`N\geq2`$; the all-cadence attenuation inequality itself includes $`N=1`$.

All calculations concern the exact specified channels. Global symmetry projection, slice harmonics and log-convex moments are inherited mathematical machinery; broader symmetry-verification results are discussed in [Related work](../references/RELATED_WORK.md).

