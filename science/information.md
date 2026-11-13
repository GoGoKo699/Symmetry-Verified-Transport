# Information in the retained density response

A fixed charge in the accepted ensemble does not, by itself, mean that the accepted data retain the original density-wave information. The relevant resource is the number of initialized attempts, including failures. This account compares the entire retained microscopic record with a simple estimator that uses every unverified final density measurement.

## The fixed late-readout experiment

Let $`L=2N`$, $`N\ge 2`$, and let $`\mu_N`$ be the uniform distribution on the half-filled slice
```math
\Omega_N=\{x\in\{0,1\}^{2N}:\sum_jx_j=N\}.
```
Choose a nonzero real density mode
```math
f(x)=\sum_{j=1}^{2N}c_j(x_j-\tfrac12),\qquad \sum_jc_j=0,
```
which is an eigenfunction of the ideal SSEP generator with eigenvalue $`-\omega`$. Write
```math
h=e^{-\omega T},\qquad s=e^{-2\gamma T}.
```
For a periodic chain with rate $`D`$ on every nearest-neighbor SWAP, a Fourier mode of wave number $`k`$ has $`\omega=4D\sin^2(k/2)`$.

The unknown parameter is the initial amplitude $`u`$ in the supplied diagonal state
```math
\Pr_u(X=x)=\mu_N(x)[1+u f(x)].
```
Put
```math
F=\max_{x\in\Omega_N}|f(x)|,\qquad
u_*=\frac{\beta}{F},\qquad 0<\beta<1,
```
and restrict $`|u|\le u_*`$. Thus the initial likelihood ratio lies between $`1-\beta`$ and $`1+\beta`$.

Every attempt uses one fresh state from this family. Before the final microscopic readout, only the prescribed nondestructive total-charge checks are available. There is no initial or intermediate microscopic measurement, no retained preparation bitstring or purification, and no protected side record of the input. These restrictions matter: reading the input occupations before storage would estimate an initial amplitude without suffering the storage noise.

Every schedule includes a final charge check at $`T`$. A checked attempt returns its charge-check record and, only when every check passes, its final occupation bitstring. The full microscopic configuration of a rejected attempt is not read out. The schedule can be randomized, and its classical label is retained. Comparisons below concern initialized attempts at the same final time $`T`$; they do not identify attempted-shot count with laboratory runtime.

## Canonical susceptibility

For $`i\ne j`$, the half-filled canonical distribution has
```math
\mathbb E_{\mu_N}x_i=\tfrac12,\quad
\operatorname{Var}_{\mu_N}(x_i)=\tfrac14,\quad
\operatorname{Cov}_{\mu_N}(x_i,x_j)=-\frac{1}{4(2N-1)}.
```
Consequently
```math
V:=\mathbb E_{\mu_N}f^2
=\frac{N}{2(2N-1)}\sum_jc_j^2>0.
```
Global complementation $`x\mapsto\mathbf1-x`$ preserves $`\mu_N`$ and sends $`f\mapsto-f`$. In particular, all odd moments of $`f`$ vanish.

## Exact retained experiment

For a particular schedule $`R`$, let $`P_R`$ be its all-pass probability and $`A_R=A_{1,R}`$ its density-mode attenuation relative to ideal transport. The charge-conditioned noise kernel and the SSEP generator give the exact accepted distribution
```math
\Pr_u(Y=y\mid\mathrm{pass},R)
=\mu_N(y)[1+u h A_R f(y)].
```
All charge-only failure records have probabilities independent of $`u`$. Indeed, for any input configuration with $`N`$ occupied sites, the distribution of the next measured total charge depends only on $`N`$, the interval and the flip rate. The same statement holds after every earlier pass. Thus the failure time, or the actual total charge observed at that failure, contributes no amplitude information.

For a fixed or independently randomized schedule, the classical Fisher information in the complete permitted transcript is therefore
```math
\mathcal I_{\mathrm{check}}(u)
=h^2\,\mathbb E_R\!\left[
P_R A_R^2\,
\mathbb E_{\mu_N}\frac{f^2}{1+u h A_R f}
\right].
```
This expression includes the complete accepted bitstring and the schedule label. It is not restricted to an estimator of one measured moment.

Complementation gives the useful identity
```math
\mathbb E_{\mu_N}\frac{f^2}{1+t f}
=\mathbb E_{\mu_N}\frac{f^2}{1-t^2f^2}.
```
Because $`|u h A_R f|\le\beta`$,
```math
V\le
\mathbb E_{\mu_N}\frac{f^2}{1+u h A_R f}
\le\frac{V}{1-\beta^2}.
```

The exact gain-acceptance law implies, for $`N\ge2`$,
```math
P_R A_R^2
\le s^2P_R^{\,1-2/N}
\le s^2.
```
Hence, at the zero-amplitude point,
```math
\boxed{\;
\mathcal I_{\mathrm{check}}(0)
=h^2V\,\mathbb E_R[P_R A_R^2]
\le s^2h^2V.
\;}
```
Uniformly on the declared amplitude interval,
```math
\mathcal I_{\mathrm{check}}(u)
\le\frac{s^2h^2V}{1-\beta^2}.
```

Keeping the random schedule label is important. Its information is governed by $`\mathbb E_R[P_RA_R^2]`$, not by $`\mathbb E_R[P_R]\bar A^2`$, where $`\bar A`$ is the attenuation after erasing that label. The displayed bound holds before this erasure.

## A raw moment estimator using every attempt

Now perform the same transport and flip evolution with no charge checks, read out the final occupations, and keep every attempt. The final mode has
```math
\mathbb E_u f(Y)=u s h V.
```
At $`u=0`$, ideal SSEP leaves $`\mu_N`$ stationary. Independent flips then give
```math
\begin{aligned}
W&:=\mathbb E_0 f(Y)^2\\
&=s^2V+\frac{1-s^2}{4}\sum_jc_j^2
=a_N(s)V,\\
a_N(s)&:=\frac{2N-1+s^2}{2N}\le1.
\end{aligned}
```
The full raw channel commutes with global complementation. Its expectation of the even function $`f(Y)^2`$ has zero overlap with the odd initial perturbation $`\mu_N f`$. Thus, exactly throughout the affine family,
```math
\mathbb E_u f(Y)^2=W,\qquad
\operatorname{Var}_u[f(Y)]
=W-u^2s^2h^2V^2.
```

For $`m`$ fresh attempts, the unverified estimator
```math
\widehat u_{\mathrm{raw}}
=\frac{1}{m s h V}\sum_{a=1}^m f(Y_a)
```
is unbiased and has exact mean squared error
```math
\boxed{\;
\mathbb E_u(\widehat u_{\mathrm{raw}}-u)^2
=\frac{a_N(s)}{m s^2h^2V}-\frac{u^2}{m}.
\;}
```
At fixed finite $`N,T`$, the bounded-output central limit theorem supplies its usual asymptotic variance. Define the reciprocal variance coefficient
```math
\mathcal J_{\mathrm{raw}}(u)
:=\frac{s^2h^2V}{a_N(s)-u^2s^2h^2V}.
```
This is a performance achieved by the displayed moment estimator; it is not asserted to equal the Fisher information of the entire raw bitstring.

At $`u=0`$,
```math
\mathcal J_{\mathrm{raw}}(0)
=\frac{s^2h^2V}{a_N(s)}
\ge s^2h^2V
\ge\mathcal I_{\mathrm{check}}(0).
```
Thus no allowed charge-check cadence improves even this raw estimator's local information performance. On $`|u|\le u_*`$, the corresponding comparison is within a controlled factor:
```math
\mathcal I_{\mathrm{check}}(u)
\le\frac{1}{1-\beta^2}\,
\mathcal J_{\mathrm{raw}}(u).
```
Exact dominance is claimed at $`u=0`$; the finite-interval statement is a bounded-factor comparison.

These Fisher-information statements do not impose unbiasedness on every possible estimator. A separate [finite-sample argument](finite_sample.md) bounds the minimax mean squared error of arbitrary, including biased, estimators.

## A scoped transport-parameter consequence

For $`T>0`$ and a nonzero wave number, if the initial nonzero amplitude $`u`$ and the noise rate are known, and only $`D`$ in $`h(D)=e^{-4D\sin^2(k/2)T}`$ is unknown, the same transcript calculation gives
```math
\mathcal I^{(D)}_{\mathrm{check}}
=u^2[h'(D)]^2\,
\mathbb E_R\!\left[
P_R A_R^2\,
\mathbb E_{\mu_N}\frac{f^2}{1+u h(D)A_R f}
\right].
```
The raw moment estimator has achieved inverse asymptotic variance
```math
\mathcal J^{(D)}_{\mathrm{raw}}
=\frac{u^2s^2[h'(D)]^2V}
{a_N(s)-u^2s^2h(D)^2V},
```
using the local inverse of its mean at the stated $`D`$. Therefore
```math
\mathcal I^{(D)}_{\mathrm{check}}
\le\frac{\mathcal J^{(D)}_{\mathrm{raw}}}{1-\beta^2}.
```
In the weak-wave limit $`u\to0`$, the coefficient of $`u^2`$ in the checked information is no larger than that achieved by the raw moment. This is a local, same-time comparison with known noise and known initial amplitude. It is not a global optimality statement for estimating transport: choosing other times, fitting several wave numbers, or using other observables are different experiments.

## Attribution and scope

Acceptance penalties and accepted-transcript information accounting are standard ingredients of symmetry verification; see [Scavino Alfaro, arXiv:2606.15464](https://arxiv.org/abs/2606.15464). The model-specific content here is the exact dynamic attenuation, its bound for every allowed cadence, and the resulting comparison with a fully charged raw baseline.

The argument concerns the diagonal density experiment under stochastic SWAP transport and independent flips. It grants perfect charge checks but excludes coherent encoding/recovery, local syndromes and microscopic records before the final readout. It does not extend the commutation factorization to arbitrary charge-conserving Hamiltonians.

