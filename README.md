# Symmetry-Verified Transport

**Does checking the total particle number preserve the information in a noisy density wave?**

Every retained run can have exactly the correct total charge while its spatial density signal remains strongly attenuated. This project determines the price of improving that signal with global charge checks, and compares the complete retained readout with an explicit unverified measurement at the same observation time.

The model is a half-filled chain of $`L=2N`$ spins undergoing stochastic nearest-neighbor exchange and independent symmetric bit flips at rate $`\gamma`$ per site. The experiment permits ideal global charge checks and keeps runs that pass every check. Microscopic occupations are read only at the final time $`T`$; extra coherent encoding, correcting feedback and input-label side information are additional resources.

## Main results

Let $`P`$ be the probability that an initialized run passes every check, and let $`A_1`$ be the retained density-wave amplitude divided by the amplitude under ideal exchange alone. Every finite check schedule obeys

```math
A_1\le e^{-2\gamma T}P^{-1/N}.
```

The bound also covers independently randomized schedules. A postselection gain $`G=A_1/e^{-2\gamma T}`$ therefore costs at least $`G^N`$ initialized attempts per retained run. Frequent checking approaches perfect retained visibility, with acceptance approaching $`e^{-2N\gamma T}`$. A single final check can have only polynomial acceptance cost, while leaving the leading local damping intact.

For $`N\ge2`$, the tradeoff has a stronger estimation consequence. At zero input amplitude in the declared weak density-amplitude experiment, the entire accepted bitstring, the check record and the known schedule give no more local Fisher information per initialized attempt than a simple raw density-moment estimator without checks. The [finite-sample account](science/finite_sample.md) gives a bounded-factor minimax mean-square-error comparison without assuming unbiased estimators.

At the longest diffusive time $`T=\Theta(L^2/D)`$, retaining any fixed fraction of the ideal density signal at fixed positive $`D,\gamma`$ as $`L\to\infty`$ requires

```math
P^{-1}=\exp\!\left[\Omega\!\left(\frac{\gamma L^3}{D}\right)\right].
```

This is the cost of retained-signal restoration. It is not a lower bound for every possible way of inferring a diffusion coefficient.

## Read the science

| Question | Authoritative account |
|---|---|
| Which preparations, controls, readouts and costs are included? | [Model](science/model.md) |
| How does conditioning change the noise channel? | [Conditional dynamics](science/conditional_dynamics.md) |
| Why does the bound hold for every check cadence? | [Visibility and acceptance](science/cadence_tradeoff.md) |
| What information remains in the complete retained record? | [Information comparison](science/information.md) |
| What follows for finite samples and biased estimators? | [Finite-sample inference](science/finite_sample.md) |
| What does a small complete example show? | [Four-spin example](science/worked_example.md) |
| Which additional controls escape the result? | [Controls and limits](science/controls_and_limits.md) |
| Which ingredients are inherited? | [Related work](references/RELATED_WORK.md) |

The [scientific overview](science/README.md) connects these chapters. For a guided route through the prerequisites and the result, start with the [learning overview](learning/README.md). The [LLM reading guide](llms.txt) maps technical questions to their proof sources.

## Learn the argument

The educational anchor is **John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018)**: [book record](https://doi.org/10.1017/9781316848142) · [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/). The [source-to-project bridge](learning/anchor_bridge.md) connects its treatment of channels, measurements and distinguishability to this transport experiment, then identifies the conditional-kernel, cadence and estimation arguments supplied here.

The [30-milestone map](learning/milestones.md) gives a reader-independent path from those foundations to the full result and its control boundaries. Use the [learning overview](learning/README.md) to choose an entry point, or go directly to the scientific chapters above.

## Reproduce

```bash
python -m pip install -r verification/requirements.txt
python verification/checks.py
```

The suite builds the full noisy Markov generator and charge-conditioned measurement records independently of the analytical formulas. It checks exact finite identities, randomized schedules, the two-spin exception and a coherent-control counterexample. See the [verification guide](verification/README.md) for recorded outputs and limits. Finite calculations support the proof conventions; the analytical arguments establish the general bounds.

## Scope and significance

Exponential dynamical-postselection overhead, undetectable symmetry-preserving errors, noisy transport damping and finite-shot verification costs are established ideas. The contribution here is the exact cadence-independent visibility-versus-acceptance law and its matched comparison of useful response information in a solvable transport experiment. [Related work](references/RELATED_WORK.md) gives the source-by-source subtraction.

The dynamics is stochastic exchange, whose noise and permutation structure permits an exact calculation. The results do not cover arbitrary interacting Hamiltonians or extra coherent protection. Global charge support and local conservation are different operational properties: postselection enforces the former while paired undetected flips can erase the latter.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
