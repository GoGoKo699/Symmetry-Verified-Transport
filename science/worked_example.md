# A complete four-spin example

Consider four sites with two particles and choose one final global number check. Let the total independent flip noise have survival factor $`s=e^{-2\gamma T}=1/2`$, so the probability that any one bit has changed is $`p=1/4`$. The exchange evolution is retained in a common ideal factor $`h(T)`$.

## Acceptance and retained signal

Passing requires equal numbers of flips among the two initially occupied and two initially empty sites. The exact probability is

```math
P_2=(1-p)^4+4p^2(1-p)^2+p^4
=\frac{59}{128}.
```

The one-pair pass factor is $`P_1=(1-p)^2+p^2=5/8`$. The first-harmonic eigenvalue from [conditional dynamics](conditional_dynamics.md) is therefore

```math
A_1=\frac{sP_1}{P_2}=\frac{40}{59}.
```

Retaining the correct total charge increases the conditional density signal from $`1/2`$ to approximately $`0.678`$ relative to the ideal exchange output. This improvement concerns each retained run; only $`59/128`$ of initialized runs are retained.

## Information per initialized attempt

Choose the real Fourier mode $`f=x_1-x_3`$ on the four-site ring. Under the uniform two-particle input, $`V=\mathbb E[f^2]=2/3`$. Prepare the local amplitude family $`\mu_2(1+u f)`$ and evaluate information at $`u=0`$. Before the final microscopic readout only the allowed global charge record is available.

Normalize all information values below by the common factor $`h(T)^2V`$. The checked experiment is granted the complete accepted bitstring. Its information is

```math
\frac{I_{\rm check}(0)}{h(T)^2V}
=P_2A_1^2=\frac{25}{118}.
```

Without checks, use only the final raw value of $`f`$. Its variance coefficient is $`a_2=(3+s^2)/4=13/16`$, so the raw sample mean has reciprocal asymptotic variance

```math
\frac{J_{\rm raw}}{h(T)^2V}
=\frac{s^2}{a_2}=\frac4{13}.
```

Thus the complete checked output has normalized information about $`0.212`$, while the simple unverified moment estimator attains about $`0.308`$. The larger conditional signal has not paid for the rejected attempts.

This example compares the same source family, observation time, exchange process and noise. It does not optimize a physical sensor over different preparations or allow an earlier microscopic readout. The general proof and finite-sample consequences are in [information](information.md) and [finite-sample inference](finite_sample.md).
