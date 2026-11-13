# Thirty milestones for symmetry-verified transport

This is a common map of the project's understanding targets. The single educational anchor is **John Watrous, The Theory of Quantum Information (2018)**; [the bridge](anchor_bridge.md) identifies its relevant sections and supplies the project's additional transport and statistical foundations.

There are **12 background milestones, M01–M12**, followed by **18 narrative milestones, M13–M30**. The background builds from one spin and one operation to the complete observation and resource contract. The narrative builds from one conditioned noise interval to every permitted cadence, the matched inference comparison, and the contribution's physical meaning and boundaries. This allocation gives the quantum-channel language, classical transport and statistical experiment enough preparation while keeping most targets on the project's argument.

The map provides a connected understanding of the result. It does not replace every proof or cover all neighboring quantum error-mitigation methods. Watrous uses base-two logarithms; this project uses natural-log relative entropy, with $`D_{\mathrm{KL}}=(\ln2)D_{\mathrm{book}}`$ and total variation equal to half the $`\ell_1`$ distance. The adaptive classical transcript chain rule is supplied in the project proof.

## Background and preliminaries

### M01 — From a spin to an observed occupation

- **Central question:** What does a computational-basis occupation measurement reveal about one spin?
- **Understanding target:** Distinguish a quantum state, a basis configuration and a measurement outcome; explain why occupation data need not describe all quantum coherence.
- **Dependencies and story role:** None. Establishes the local physical object and the final readout.
- **Conceptual connection:** Diagonal state entries become classical occupation probabilities, while the underlying experiment remains a quantum-channel model.
- **Sources:** Watrous sections 2.1.1–2.1.2, 2.3.1; [model: spins and charge](../science/model.md#spins-charge-and-transport).

### M02 — A fixed total charge leaves many spatial states

- **Central question:** What remains unknown when the total particle number is known exactly?
- **Understanding target:** Explain the half-filled sector $`\Omega_N`$, its projector $`\Pi_N`$ and uniform state $`\mu_N`$; distinguish fixed total number from a fixed arrangement.
- **Dependencies and story role:** M01. Builds the register and its global constraint.
- **Conceptual connection:** A sector projector specifies an allowed subspace, not a particular microscopic state.
- **Sources:** Watrous sections 2.1.1–2.1.2, 2.3.1; [model](../science/model.md#spins-charge-and-transport); [canonical susceptibility](../science/information.md#canonical-susceptibility).

### M03 — Random physical operations define a channel

- **Central question:** How can stochastic SWAPs and flips be represented within quantum mechanics?
- **Understanding target:** Recognize a convex mixture of unitary operations as a channel and distinguish its action on states from its adjoint action on observables.
- **Dependencies and story role:** M01–M02. Supplies the local evolution language.
- **Conceptual connection:** The same quantum channel has an ordinary Markov description when restricted to diagonal occupation data.
- **Sources:** Watrous sections 2.2.1–2.2.2, 4.1.1; [model generators](../science/model.md#spins-charge-and-transport).

### M04 — A flip rate is not a flip probability

- **Central question:** Why does independent flipping at rate $`\gamma`$ produce $`p=(1-e^{-2\gamma\Delta})/2`$ after time $`\Delta`$?
- **Understanding target:** Explain net odd versus even flip counts and identify the surviving single-site density factor $`s=e^{-2\gamma\Delta}`$.
- **Dependencies and story role:** M03. Fixes the noise convention before any resource law.
- **Conceptual connection:** Continuous-time repeated errors become one exact product channel over an interval.
- **Sources:** Watrous sections 2.2.1–2.2.2 for channel representation; [rate convention and interval noise](../science/model.md#spins-charge-and-transport).

### M05 — Conditioning changes both a state and its yield

- **Central question:** What does a successful global charge measurement do, and what is paid for it?
- **Understanding target:** Describe the unnormalized successful map, its probability and its normalized retained state; count rejected initializations.
- **Dependencies and story role:** M02–M04. Introduces the verification operation and its resource meaning.
- **Conceptual connection:** A trace-nonincreasing operation records both a retained output and the chance of obtaining it.
- **Sources:** Watrous sections 2.3.1–2.3.2; [allowed protocols](../science/model.md#allowed-verification-protocols); [charged resources](../science/model.md#what-is-charged).

### M06 — Spatial density is different from total density

- **Central question:** How can a density wave change while total charge stays fixed?
- **Understanding target:** Interpret a zero-sum mode $`f(x)=\sum_jc_j(x_j-\tfrac12)`$ and explain which spatial information it measures.
- **Dependencies and story role:** M01–M02. Connects individual occupations to a distributed physical observable.
- **Conceptual connection:** Removing the uniform component separates the known total charge from the signal being transported.
- **Sources:** Watrous sections 2.1.1, 2.3.1 for observable probabilities; [density modes](../science/model.md#density-modes-and-the-input-amplitude-family).

### M07 — Exchange moves a density wave diffusively

- **Central question:** How do random neighboring SWAPs attenuate a Fourier density mode?
- **Understanding target:** Explain the SSEP discrete Laplacian, ideal factor $`h=e^{-\omega_kT}`$ and longest-wavelength time scale $`T=\Theta(L^2/D)`$.
- **Dependencies and story role:** M03, M06. Places the mode in its spatial and temporal setting.
- **Conceptual connection:** Local exchange conserves particle number while relaxing nonuniform profiles.
- **Sources:** Watrous sections 4.1.1 for random-unitary channels; [transport and density rates](../science/model.md#density-modes-and-the-input-amplitude-family). The SSEP calculation is supplied locally.

### M08 — A reversible kernel is an evolution rule and a proof tool

- **Central question:** Why is uniformity on the fixed-charge sector useful?
- **Understanding target:** Interpret a Markov kernel, a stationary distribution and reversibility; distinguish evolving functions from evolving densities.
- **Dependencies and story role:** M02–M03, M06–M07. Joins local transition rules into a tractable global framework.
- **Conceptual connection:** A symmetric sector kernel acts consistently on likelihood perturbations and measured observables.
- **Sources:** Watrous sections 1.2.2, 4.2.2 for probability and fixed-point language; [the conditional kernel](../science/conditional_dynamics.md#one-interval-and-its-success-probability).

### M09 — A small density wave is a specified statistical source

- **Central question:** What exactly is unknown in the amplitude experiment?
- **Understanding target:** Explain the source $`\mu_N(1+uf)`$, variance $`V`$, and positivity interval $`|u|\leq\beta/\|f\|_\infty`$; retain its possible size dependence.
- **Dependencies and story role:** M02, M06, M08. Turns a qualitative density signal into a precise input promise.
- **Conceptual connection:** Linear response is an explicit family of positive states, not permission to assume a fixed macroscopic modulation at every size.
- **Sources:** Watrous sections 1.2.2, 2.1.1–2.1.2; [amplitude family](../science/information.md#the-fixed-late-readout-experiment); [susceptibility](../science/information.md#canonical-susceptibility).

### M10 — Conditional signal strength is not information per attempt

- **Central question:** Which quantity measures useful estimation performance once failures are counted?
- **Understanding target:** Distinguish attenuation, Fisher information of an entire record, and variance achieved by a named estimator.
- **Dependencies and story role:** M05, M09. Establishes the statistical performance distinction used by the result.
- **Conceptual connection:** Measurement probabilities define a likelihood; a larger retained mean need not compensate for discarded trials.
- **Sources:** Watrous sections 2.3.1–2.3.2 for outcome laws; [information account](../science/information.md). Fisher information and the achieved-variance convention are defined locally.

### M11 — Estimation can be bounded through distinguishability

- **Central question:** How can one constrain biased as well as unbiased estimators?
- **Understanding target:** Explain the reduction from estimating an amplitude to distinguishing two amplitudes, and the roles of relative entropy and total variation.
- **Dependencies and story role:** M09–M10. Adds the finite-sample tool needed beyond a local variance bound.
- **Conceptual connection:** An accurate estimate would identify which of two source states was supplied; weakly distinguishable records limit that possibility.
- **Sources:** Watrous sections 3.1.1, 5.1.1–5.1.2; [two-point argument](../science/finite_sample.md#a-finite-two-point-distinguishability-bound).

### M12 — The complete comparison is one fixed late-readout experiment

- **Central question:** Which source, controls, output and costs must agree before checked and raw data can be compared?
- **Understanding target:** Reconstruct the full contract: fresh source, fixed duration, allowed charge records, final bitstrings, noise knowledge and every initialized attempt.
- **Dependencies and story role:** M01–M11. Integrates the background into the actual problem.
- **Conceptual connection:** A channel description becomes an operational resource comparison only after accessible information and excluded side records are explicit.
- **Sources:** Watrous sections 2.2–2.3; [model](../science/model.md); [fixed experiment](../science/information.md#the-fixed-late-readout-experiment); [resource boundaries](../science/controls_and_limits.md#allowed-experiment-and-charged-resources).

## Narrative and contribution

### M13 — Passing means balanced errors, not absence of errors

- **Central question:** Which flip patterns pass one half-filling check?
- **Understanding target:** Derive the event $`A=B`$ for two independent binomial counts and interpret the exact return probability $`P_N(p)`$.
- **Dependencies and story role:** M02, M04–M05, M12. Starts the argument with one check.
- **Conceptual connection:** Errors at different positions can cancel in total charge while changing spatial information.
- **Sources:** Watrous sections 1.2.2 for probability notation; [one-interval success](../science/conditional_dynamics.md#one-interval-and-its-success-probability).

### M14 — Input-independent success gives a linear retained channel

- **Central question:** Why does normalizing successful runs define a channel here?
- **Understanding target:** Explain why success depends only on the input sector, then construct $`\mathcal K_p`$ and the reversible kernel $`K_p(x,y)`$.
- **Dependencies and story role:** M03, M05, M08, M13. Converts selection into an exact conditional evolution law.
- **Conceptual connection:** The constant success probability preserves linearity; a state-dependent normalization would require different reasoning.
- **Sources:** Watrous sections 2.2.1–2.2.2, 2.3.1–2.3.2; [retained channel](../science/conditional_dynamics.md#one-interval-and-its-success-probability).

### M15 — A pair difference reveals the density eigenvalue

- **Central question:** What survives when one follows a difference of two occupations through the retained kernel?
- **Understanding target:** Reconstruct the pair generating-function argument and obtain $`\lambda_1=(1-2p)P_{N-1}/P_N`$ for every linear zero-sum mode.
- **Dependencies and story role:** M06, M13–M14. Identifies the local mechanism controlling density loss.
- **Conceptual connection:** Removing one opposite occupied–empty pair reduces a spatial-observable calculation to a smaller balanced-return probability.
- **Sources:** Watrous sections 2.2.1–2.2.2 for adjoint-observable language; [density attenuation proof](../science/conditional_dynamics.md#density-attenuation).

### M16 — Difference spaces separate scalar noise from transport

- **Central question:** What extends from one pair without assuming every many-body mode has the same transport rate?
- **Understanding target:** Explain products of disjoint pair differences, their permutation span, and $`\lambda_r=(1-2p)^rP_{N-r}/P_N`$; distinguish scalar noise action from ideal evolution within the space.
- **Dependencies and story role:** M03, M07–M08, M15. Extends the mechanism while preserving its exact scope.
- **Conceptual connection:** Permutations preserve the defined difference spaces, so stochastic SWAP transport and scalar retained noise can be composed without an irreducible-decomposition assumption.
- **Sources:** Watrous sections 2.2.1–2.2.2, 4.1.1; [higher-degree spaces](../science/conditional_dynamics.md#higher-degree-difference-spaces); [commutation](../science/model.md#why-transport-and-noise-commute).

### M17 — A whole check schedule has an exact channel and an uninformative failure record

- **Central question:** How do interval results combine, and can failure times reveal the amplitude?
- **Understanding target:** Obtain $`P=\prod_iP_N(p_i)`$ and $`A_r=\prod_i\lambda_r(p_i)`$; explain why first-failure time and global charge are input-independent.
- **Dependencies and story role:** M12–M16. Joins individual checks into the complete permitted transcript.
- **Conceptual connection:** Every pass returns to the same input sector; each subsequent global-charge law again depends only on its size and interval.
- **Sources:** Watrous sections 2.2–2.3; [schedule composition](../science/conditional_dynamics.md#several-intervals); [failure record](../science/conditional_dynamics.md#why-the-global-failure-record-carries-no-input-information).

### M18 — A return probability is a positive moment

- **Central question:** Which feature of $`P_M`$ links different sector sizes?
- **Understanding target:** Explain the Fourier coefficient representation $`P_M=\mathbb E[W^M]`$ with $`0\leq W\leq1`$, and why Hölder gives $`P_{N-r}\leq P_N^{1-r/N}`$.
- **Dependencies and story role:** M13, M15–M17. Exposes the mechanism behind the global bound.
- **Conceptual connection:** A combinatorial error count becomes a positive moment, allowing a standard convexity principle to constrain conditional visibility.
- **Sources:** Watrous sections 1.2.2 for expectation notation; [positive moment formula](../science/conditional_dynamics.md#a-positive-moment-formula); [Hölder step](../science/cadence_tradeoff.md#the-gain-versus-acceptance-theorem).

### M19 — Every cadence obeys the gain–acceptance law

- **Central question:** How much retained gain can a schedule buy at a given acceptance?
- **Understanding target:** Derive and interpret $`A_r\leq e^{-2r\gamma T}P^{-r/N}`$ and $`1/P\geq G_r^{N/r}`$; identify when its rearranged restoration bound is informative.
- **Dependencies and story role:** M17–M18. Establishes the central finite-size resource theorem.
- **Conceptual connection:** The same interval inequality multiplies across arbitrary spacings, converting conditional signal gain into a lower bound on initialized attempts.
- **Sources:** Watrous sections 2.3.1–2.3.2 for branch probabilities; [gain theorem](../science/cadence_tradeoff.md#the-gain-versus-acceptance-theorem); [resource meaning](../science/cadence_tradeoff.md#what-the-theorem-prices).

### M20 — A random schedule label is part of the data

- **Central question:** Which averaging is legitimate when cadence is randomized?
- **Understanding target:** Distinguish accepted averaging after erasing the schedule from the labeled experiment; explain the Jensen bound and later label-conditioned information averaging.
- **Dependencies and story role:** M10, M12, M17–M19. Completes the schedule quantifiers.
- **Conceptual connection:** Randomization does not evade an inequality valid for each schedule, but discarding labels can reduce the information being bounded.
- **Sources:** Watrous sections 1.2.2, 2.3.1–2.3.2; [randomized schedules](../science/cadence_tradeoff.md#randomized-schedules); [exact retained experiment](../science/information.md#exact-retained-experiment).

### M21 — Arbitrarily frequent checks restore the retained branch at a precise cost

- **Central question:** Is complete retained-signal restoration attainable?
- **Understanding target:** Explain the fixed-$`N,T`$ limit $`A_r\to1`$, $`P\to e^{-2N\gamma T}`$ and its relation to no-flip histories; distinguish endpoint saturation from a solved finite-cadence frontier.
- **Dependencies and story role:** M04, M17–M19. Supplies a sharp attainable endpoint.
- **Conceptual connection:** Suppressing accepted multiple-error events can recover ideal density evolution while retaining an extensive selection penalty.
- **Sources:** Watrous sections 2.2–2.3 for repeated channel composition; [restoration limit](../science/cadence_tradeoff.md#the-noiseless-retained-endpoint-is-attained-as-a-limit).

### M22 — A final check can be inexpensive and still leave the density loss

- **Central question:** Why can correct retained charge coexist with nearly unchanged local attenuation?
- **Understanding target:** Interpret the return-probability asymptotics and $`\lambda_1/(1-2p)\to1`$ at fixed nonzero $`p`$ as size grows; distinguish this limit from frequent checking.
- **Dependencies and story role:** M13, M15, M18–M21. Compares the other physical operating regime.
- **Conceptual connection:** Many balanced-error histories pass a final global check, giving polynomial acceptance without restoring spatial information.
- **Sources:** Watrous sections 1.2.2 for probability interpretation; [single final check](../science/cadence_tradeoff.md#a-single-final-check).

### M23 — The full accepted bitstring has a calculable information budget

- **Central question:** Does access to every retained occupation evade the density-mode bound?
- **Understanding target:** Reconstruct the accepted likelihood $`\mu_N(1+uhA_1f)`$ and its acceptance-weighted Fisher information, including schedule labels and input-independent failures.
- **Dependencies and story role:** M09–M10, M14–M17, M19–M20. Turns the dynamic theorem into an information statement for the whole allowed record.
- **Conceptual connection:** The checked protocol receives its complete permitted output; its limitation is not imposed by restricting it to one estimator.
- **Sources:** Watrous sections 2.3.1–2.3.2; [exact retained likelihood and information](../science/information.md#exact-retained-experiment).

### M24 — A raw moment already matches or exceeds the local information performance

- **Central question:** What does the unverified experiment achieve with every attempt retained?
- **Understanding target:** Explain the raw mean, exact second moment and estimator variance; derive the $`N\geq2`$ comparison using $`PA_1^2\leq s^2`$.
- **Dependencies and story role:** M09–M10, M19, M23. Establishes the matched constructive baseline.
- **Conceptual connection:** A lower conditional signal can carry more information per initialization because it avoids the acceptance penalty.
- **Sources:** Watrous sections 1.2.2 for moments; [raw estimator](../science/information.md#a-raw-moment-estimator-using-every-attempt).

### M25 — Finite amplitude preserves a controlled comparison

- **Central question:** What remains valid away from the zero-amplitude point?
- **Understanding target:** Retain the denominator margin $`\beta`$, distinguish exact local dominance from the bounded-factor finite-interval statement, and interpret the raw estimator's exact finite-sample MSE.
- **Dependencies and story role:** M09–M10, M23–M24. Keeps local and uniform claims separate.
- **Conceptual connection:** Positivity of the full source family controls the likelihood denominator; the amplitude interval is part of the physical-statistical promise.
- **Sources:** Watrous sections 1.2.2, 2.1.1–2.1.2; [information comparison](../science/information.md#a-raw-moment-estimator-using-every-attempt); [raw finite-sample upper bound](../science/finite_sample.md#an-explicit-raw-upper-bound).

### M26 — A finite-sample lower bound covers every estimator

- **Central question:** Can biased estimation or choosing later schedules from earlier records evade the sampling law?
- **Understanding target:** Follow the two-point relative-entropy bound, transcript chain rule and testing reduction; compare its minimax MSE order with the clipped raw estimator while retaining $`u_*`$.
- **Dependencies and story role:** M11–M12, M19–M20, M23–M25. Integrates dynamic and statistical controls into a finite-budget result.
- **Conceptual connection:** A bound on every conditional one-attempt transcript survives adaptive choice between attempts and constrains arbitrary estimators.
- **Sources:** Watrous sections 3.1.1, 5.1.1–5.1.2; [finite-sample argument](../science/finite_sample.md); [what is matched](../science/finite_sample.md#what-is-matched).

### M27 — Small systems expose the cost distinction and the size boundary

- **Central question:** What do the four-spin example and two-spin exception reveal about the theorem?
- **Understanding target:** Explain why $`P=59/128`$ and $`A_1=40/59`$ improve retained visibility but lose to the raw information benchmark; identify why the $`N=1`$ frequent-check case does not obey the $`N\geq2`$ no-benefit conclusion.
- **Dependencies and story role:** M19, M21, M23–M24. Grounds the abstract comparison and checks its size restriction.
- **Conceptual connection:** A complete example illustrates the theorem, while an exception prevents extending its statistical conclusion beyond its hypotheses.
- **Sources:** Watrous sections 2.3.1–2.3.2 for branch records; [four-spin example](../science/worked_example.md); [two-site boundary](../science/controls_and_limits.md#two-sites-are-a-genuine-exception).

### M28 — Restoring a hydrodynamic signal is costlier than inferring from a noisy one

- **Central question:** Why do restoration and inference have different noise exponents at a diffusive horizon?
- **Understanding target:** Connect $`T=\Theta(L^2/D)`$ to the restoration exponent $`\Theta(\gamma L^3/D)`$ and the raw inference exponent $`\Theta(\gamma L^2/D)`$ in their stated regimes; keep amplitude and accuracy scaling explicit.
- **Dependencies and story role:** M07, M09, M19, M21–M26. Connects the finite-channel result to macroscopic observation times.
- **Conceptual connection:** Preserving an order-one physical response pays an extensive no-error penalty, whereas calibrated inference can use many weak raw responses.
- **Sources:** Watrous sections 2.2–2.3 for the underlying experiments; [hydrodynamic times](../science/cadence_tradeoff.md#hydrodynamic-observation-times); [matched inference dependence](../science/finite_sample.md#what-is-matched).

### M29 — Extra coherent controls and new records change the conclusion

- **Central question:** Which changes would create a different protection or inference problem?
- **Understanding target:** Explain the global-complement encoding escape, distinguish it from reproducing ideal diffusion, and identify the separate roles of local checks, feedback, early microscopic records and unknown-noise calibration.
- **Dependencies and story role:** M01–M03, M05, M12, M16, M23–M28. Tests the boundaries controlling the interpretation.
- **Conceptual connection:** Quantum coherence can move the amplitude into a fixed observable outside the diagonal-density theorem; extra records or different control operations alter the resource contract.
- **Sources:** Watrous sections 2.2.1–2.2.2, 4.2.2; [controls and limits](../science/controls_and_limits.md); [coherent-control construction](../science/cadence_tradeoff.md#coherent-controls-change-the-model).

### M30 — The complete contribution has one scoped operational meaning

- **Central question:** What does the field learn after the prior symmetry-verification and statistical ingredients are credited?
- **Understanding target:** Reconstruct the connected chain from balanced-error kernel to all-cadence tradeoff, full-record information bound, raw baseline and finite-sample consequence; state the assumptions, attained endpoint, inherited tools and meaningful escapes together.
- **Dependencies and story role:** M13–M29, with M12's experiment contract. Synthesizes the narrative into the complete scientific account.
- **Conceptual connection:** Perfect global charge in retained records is insufficient to establish efficient recovery of spatial density information in this operation class. That conclusion is distinct from a universal error-mitigation or transport-inference impossibility.
- **Sources:** [Watrous sections bridge](anchor_bridge.md); [scientific overview](../science/README.md); [prior-work comparison](../references/RELATED_WORK.md); [controls and limits](../science/controls_and_limits.md).

