# CT1: a conserved GABAergic amacrine divergence hub across three *Drosophila* optic lobes

**Shared circuit:** one hub neuron driving N = 1871 mutually non-adjacent targets (N = 1872 nodes total), with directed structure identical across **FAFB**, **MCNS**, and **MAOL** (VF2-verified). Focus dataset for biology: **FAFB v783**.

## The identified circuit

The submitted circuit is a directed **out-star** (divergence motif): a single presynaptic hub with edges to many targets that have no edges among themselves. In FAFB, Codex identifies the hub (root id `720575940628908548`, label LO.5422) as **CT1**: super-class *optic*, sub-class *lobula-medulla amacrine*, predicted neurotransmitter **GABA** (Codex confidence 0.64), with 5,997 upstream and 6,447 downstream partners.

CT1 is a single, giant wide-field amacrine neuron that tiles the entire optic lobe, sending one arbor into each retinotopic column of the medulla and lobula. The 3D morphology (Fig. 2) and its regional connectivity (Fig. 3, heavy input in the lobula LO_L with output to the medulla ME_L and lobula plate LOP_L) are both consistent with this identity.

![CT1 induced divergence circuit](figures/circuit_graph.png)
*Fig. 1. The submitted circuit in FAFB (72 of 1871 targets shown). Red: hub CT1; blue: the selected pairwise non-adjacent target subset that defines the induced star.*

## Structural and functional observations

- **The motif is large only where CT1 exists.** The shared out-star reaches 1872 in the three optic-lobe datasets (FAFB, MCNS, MAOL) but collapses to 314 in MANC, the male ventral nerve cord, which contains no optic lobe. This pattern is what one expects if the correspondence is anatomical rather than coincidental. Codex annotates CT1 instances in BANC (2), FAFB (2), MAOL (1), and MCNS (2).
- **A large non-adjacent target set exists rather than being forced.** That CT1 has hundreds of downstream partners which *can* be chosen pairwise non-adjacent implies those partners carry little lateral connectivity, consistent with a column-by-column output organisation. CT1 is independently known to be split into hundreds of electrically isolated compartments, roughly one per column (Meier & Borst 2019), which provides a mechanism for such parallel, weakly coupled output channels.

![CT1 3D mesh](figures/ct1_mesh.png)
*Fig. 2. Codex 3D mesh of CT1 (magenta) filling the left optic lobe with a thin medial projection: the characteristic wide-field amacrine morphology.*

## Hypothesis and interpretation

The shared circuit is an **inhibitory divergence / gain-control** motif. CT1 distributes a GABAergic signal in parallel across many retinotopic columns. CT1 is an established component of the T4/T5 elementary-motion-detection circuitry (Takemura et al. 2017; Shinomiya et al. 2019), where wide-field inhibition is a candidate substrate for spatial normalisation. The fan-out to a weakly coupled target set is consistent with parallel labelled-line processing, in which a common signal is broadcast to many channels without introducing lateral crosstalk.

**Limits of the claim.** The directed isomorphism across the three datasets is exact and machine-verified, but it is a *topological* statement and does not by itself establish homology. The hub is confirmed as CT1 only in FAFB; the MCNS and MAOL hubs (`10157`, `10046`) are strong candidate CT1 homologues to confirm directly in Codex.

![CT1 connectivity](figures/ct1_connectivity.png)
*Fig. 3. CT1 (R) connectivity (Codex). Gold: GABAergic. Heavy lobula input (LO_L, 1,284 synapses) with output to medulla (ME_L) and lobula plate (LOP_L).*

## References

1. Meier M, Borst A (2019) Extreme compartmentalization in a *Drosophila* amacrine cell. *Current Biology* 29:1545–1550.
2. Shinomiya K, et al. (2019) Comparative connectomics of the two motion pathways in *Drosophila*. *eLife* 8:e40025.
3. Takemura S, et al. (2017) The comprehensive connectome of a neural substrate for motion detection in *Drosophila*. *eLife* 6:e24394.
4. Dorkenwald S, et al. (2024) Neuronal wiring diagram of an adult brain. *Nature* 634:124–138.
5. Schlegel P, et al. (2024) Whole-brain annotation and multi-connectome cell typing of *Drosophila*. *Nature* 634:139–152.
6. Matsliah A, et al. (2024) Neuronal parts list and wiring diagram for a visual system. *Nature* 634:153–165.
7. Milo R, et al. (2002) Network motifs: simple building blocks of complex networks. *Science* 298:824–827.
