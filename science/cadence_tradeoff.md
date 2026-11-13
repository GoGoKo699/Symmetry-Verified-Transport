# Cadence, accepted signal and sampling cost

Global verification improves a retained density signal by rejecting noise histories. The exact price is extensive in the number of occupied sites. This page proves that statement for every allowed cadence in the [model](model.md), including randomized schedules.

## The gain-versus-acceptance theorem

Let $`L=2N`$, $`1\leq r\leq N`$, and let a finite schedule have intervals $`\Delta_i`$ summing to $`T`$. Define

```math
p_i=\frac{1-e^{-2\gamma\Delta_i}}2,\qquad
P=\prod_iP_N(p_i),\qquad
A_r=\prod_i
 \left(e^{-2r\gamma\Delta_i}
       \frac{P_{N-r}(p_i)}{P_N(p_i)}\right).
```

Here $`P`$ is the probability that all checks pass. On the degree-$`r`$ difference space, $`A_r`$ is the retained noise attenuation relative to the given ideal transport, as established in [Conditional dynamics](conditional_dynamics.md).

**Theorem.** Every such schedule obeys

```math
A_r\leq e^{-2r\gamma T}P^{-r/N}.
```

The statement is exact at finite $`N,T`$. It does not require equally spaced checks or a long-time approximation.

**Proof.** Fix one interval and suppress its $`p`$ argument. The positive moment representation is

```math
P_M=\mathbb E[W^M],\qquad
W=1-4p(1-p)\sin^2(\Phi/2)\in[0,1],
\qquad \Phi\sim\operatorname{Unif}[-\pi,\pi].
```

Hölder's inequality gives log-convexity of these moments. Applying it between exponents zero and $`N`$ yields

```math
P_{N-r}
 \leq P_N^{\,1-r/N}P_0^{\,r/N}
 =P_N^{\,1-r/N}.
```

This includes $`r=N`$, when $`P_0=1`$. Hence

```math
\lambda_r(p)
 =e^{-2r\gamma\Delta}\frac{P_{N-r}(p)}{P_N(p)}
 \leq e^{-2r\gamma\Delta}P_N(p)^{-r/N}.
```

Multiplying over intervals proves the theorem. Hölder's inequality is the standard log-convexity-of-moments argument; its application here uses the exact balanced-return moment identity.

Because $`W\in[0,1]`$, one also has $`P_{N-r}\geq P_N`$. Therefore

```math
e^{-2r\gamma T}\leq A_r\leq1.
```

The upper bound follows from Markov-channel contraction and the exact nonnegative eigenvalues. Postselection improves retained attenuation, but acceptance constrains the improvement.

## What the theorem prices

Relative to the unverified factor $`e^{-2r\gamma T}`$, define

```math
G_r=\frac{A_r}{e^{-2r\gamma T}}\geq1.
```

Then

```math
\frac1P\geq G_r^{\,N/r}.
```

A fixed gain $`G_1>1`$ in a linear density mode requires at least $`G_1^N`$ initialized attempts per accepted output. Charging only accepted outputs would omit this factor.

Equivalently, requiring $`A_r\geq a`$ with $`0<a\leq1`$ forces

```math
P\leq a^{-N/r}e^{-2N\gamma T}.
```

If the right-hand side exceeds one, this rearrangement is uninformative. The finite inequality is authoritative; an exponential-cost conclusion requires a regime in which its exponent is negative and large.

For example, if $`N\to\infty`$ and $`\log(1/P)=o(N)`$, then

```math
1\leq G_r\leq
 \exp\!\left(\frac rN\log\frac1P\right).
```

At each fixed degree $`r`$, this tends to one. Polynomial attempt overhead is a special case: global verification then leaves the leading density attenuation unchanged.

## Randomized schedules

Let $`R`$ be an externally randomized schedule, independent of the input parameter, with every realization having total duration $`T`$. Write $`P_R,A_{r,R}`$ for its pass probability and attenuation, and let $`\overline P=\mathbb E[P_R]`$.

If the schedule label is discarded, the normalized accepted map has degree-$`r`$ attenuation

```math
\overline A_r
 =\frac{\mathbb E[P_RA_{r,R}]}{\mathbb E[P_R]}.
```

For every realized schedule,

```math
P_RA_{r,R}
 \leq e^{-2r\gamma T}P_R^{\,1-r/N}.
```

The function $`x^{1-r/N}`$ is concave on positive $`x`$. Jensen's inequality gives

```math
\overline A_r
 \leq e^{-2r\gamma T}\overline P^{-r/N}.
```

For $`r=N`$, the numerator bound uses $`P_R^0=1`$ and gives the same conclusion directly.

If the schedule label is retained, the labeled experiment need not be replaced by its averaged attenuation. The deterministic inequality holds for every label. A per-attempt information inequality proved separately for each schedule can therefore be averaged with the actual schedule probabilities.

## The noiseless retained endpoint is attained as a limit

The complete-restoration endpoint is exact. Fix $`N,r,T,\gamma`$ and use $`m`$ equally spaced checks with $`\Delta=T/m`$. Expanding the exact finite sums at small $`p`$ gives

```math
\begin{aligned}
\log P_N(p)
 &=-2Np+(N^2-N)p^2+O_N(p^3),\\
\log\lambda_r(p)
 &=-r(2N+1-r)p^2+O_{N,r}(p^3).
\end{aligned}
```

For the first expansion, the terms with zero and one opposite-direction flip pair give

```math
P_N(p)=1-2Np+(3N^2-N)p^2+O_N(p^3).
```

Substituting this logarithmic expansion for $`P_N`$ and $`P_{N-r}`$ into the exact eigenvalue formula gives the second expansion.

Also $`p(\Delta)=\gamma\Delta+O((\gamma\Delta)^2)`$. Thus

```math
\lim_{m\to\infty}P_N(p(T/m))^m=e^{-2N\gamma T},
\qquad
\lim_{m\to\infty}\lambda_r(p(T/m))^m=1.
```

The accepted density dynamics become ideal, while acceptance tends to the probability of no physical flip during a duration-$`T`$ run. The theorem is saturated at this limiting endpoint:

```math
1=e^{-2r\gamma T}
 \left(e^{-2N\gamma T}\right)^{-r/N}.
```

These expansions take the frequent-check limit at fixed $`N,r,T,\gamma`$. They are not a uniform assertion about arbitrary simultaneous growth of size, duration and check number. The exact theorem remains valid in such a joint regime without an expansion.

Endpoint saturation does not assert that the upper bound is attained for every intermediate acceptance target or every finite number of checks.

## A single final check

One final check can have a much larger pass rate. The moment formula gives universal constants $`c,C>0`$ such that

```math
\frac{c}{\sqrt{1+Mp(1-p)}}
 \leq P_M(p)
 \leq\frac{C}{\sqrt{1+Mp(1-p)}},
 \qquad M\geq0,\quad 0\leq p\leq\frac12.
```

An elementary proof bounds the Fourier integral. On $`[-\pi,\pi]`$,

```math
\sin^2(\phi/2)\geq\frac{\phi^2}{\pi^2},
```

so the integrand is bounded above by $`\exp[-4Mp(1-p)\phi^2/\pi^2]`$. For the lower bound, restrict to $`|\phi|\leq(1+Mp(1-p))^{-1/2}`$, use $`\sin^2(\phi/2)\leq\phi^2/4`$, and bound the resulting power below by a positive constant. Together with $`P_M\leq1`$, these estimates give the stated comparison.

At fixed $`0<p<1/2`$, the integrand has a unique maximum on the integration circle, with local form $`1-p(1-p)\phi^2+O(\phi^4)`$. Laplace's method gives

```math
P_M(p)\sim\frac1{\sqrt{4\pi Mp(1-p)}},
\qquad M\to\infty.
```

Consequently,

```math
\frac{\lambda_1(p)}{1-2p}
 =\frac{P_{N-1}(p)}{P_N(p)}\longrightarrow1.
```

A final check can accept a polynomial fraction of runs while leaving local density attenuation asymptotically unchanged. Exact charge in retained records does not imply restoration of the local mode.

## Hydrodynamic observation times

For the longest nonzero Fourier mode on the periodic chain, ideal decay has rate $`\Theta(D/L^2)`$. A time $`T=\Theta(L^2/D)`$ leaves an order-one fraction of that ideal mode.

If $`\gamma`$ is fixed and one requires $`A_1\geq a>0`$, the exact inequality gives

```math
\log\frac1P
 \geq2N\gamma T+N\log a
 =\Omega(\gamma L^3/D).
```

The final statement is for growing size with $`\gamma T\to\infty`$ and fixed $`a`$. It does not apply unchanged when $`\gamma`$ decreases so rapidly that the exact right-hand side is nonpositive.

Frequent checks can restore the accepted hydrodynamic signal, but pay an exponential number of initializations in this regime. A final check may be inexpensive, but does not remove the leading local damping. Preserving a physical density signal and inferring a transport parameter are distinct tasks. Calibrated rescaling, two-rate fits, shorter times and other observables are separate strategies; the theorem does not exclude them.

## Coherent controls change the model

Additional sector-preserving coherent encoding can move a density amplitude into a protected global-complement coherence. The explicit construction and its limits are given in [Controls and limits](controls_and_limits.md#a-coherent-encoding-preserves-an-amplitude-at-every-size). It protects an amplitude family; it does not reproduce unknown unencoded SSEP transport. The cadence theorem therefore keeps the control class in [the model](model.md) fixed.

## Interpretation and attribution

Symmetry verification, dynamical postselection, undetected errors and exponential selection overhead are established ideas. Hölder's inequality and the harmonic structure of fixed-charge configurations are standard tools. The result here is the exact finite-size gain-versus-acceptance law across every permitted cadence, with an explicit observation and resource contract. The matched information comparison uses that law rather than treating accepted bias reduction alone as a performance guarantee.

See [Related work](../references/RELATED_WORK.md) for comparisons with symmetry verification, channel-level correction and noise extrapolation of transport coefficients.

