# how does polyadenylation stop?
cailyx q. uci EiR/senior thesis project 2026

In the cell, a freshly made strand of RNA is commonly extended further by a poly(A) polymerase (PAP) successively adding A's to create a "poly(A) tail." Why, when, and how does tail growth stop? Biochemical study (from the Wahle group and others) has suggested the following picture. PAP is tethered to a protein complex bound to the RNA just upstream of where the poly(A) tail starts as it quickly and processively adds A's-- *i.e., the tail forms in something of a loop*, and not simply linearly outward from the 3' end. As it grows in a loop, a poly(A)-binding protein (PABP) binds to the growing tail every some number of A's, until PAP undergoes a sudden and large drop in rate and processivity at around 250 A's. While it can continue further slowly and distributively, we will consider this the effective "stopping point" for polyadenylation to be explained. Because the 250-A-point corresponds experimentally to the point at which 1) PAP ceases to be stimulated by (and presumably, bound to) the upstream protein complex, and 2) the length that achieves a maximum polyA-PABP "globule" size (seen by electron microscopy), we here suggest the "stopping point" is precisely when the loop of polyA RNA breaks.

Here, then, we try to understand this stopping point by treating the growth of a poly(A) tail as a polymer loop growing in size. At each tail length, maximization of configurational entropy and minimization of excluded volume effects are in competition with favorability of the globule formation (a sum of PABPs self-associating, PABP-polyA binding, and PAP-mPSF binding). This creates distinct stages over the course of polyadenylation and invites control by parameters like salt concentration, which influence polymer persistence lengths.

we sketch a few stages:
* (left) - initially, the polymer is simply too short to be forced into a circle. i.e., the energy of it circularizing is infinitely high.
* (middle) - there exists a point when the costs and gains of forming a loop are perfectly balanced.
* (right) - the loop snaps open, as the cost of forming a loop again exceeds the gains.

<img width="720" height="504" alt="cartoon" src="https://github.com/user-attachments/assets/8d35ea81-481f-441b-94f9-2197fddf712b" />



## considerations
It should be noted that it is unclear whether such a physiologically relevant globule forms and if so what its structure is. There are also other interesting possibilities for explaining tail length control. For example, evidence that the nuclear poly(A)-binding protein (PABPN1) exhibits phase separation adds the possibility of tail length control at the level of multiple polyA-PABPs in coordination. There are also not only additional poly(A)-binding proteins (incl. the cytoplasmic PABPCs) which may work in concert to control length, but also other mRNA processing and degradation factors (PABPN1 is involved in *hyper*adenylation-mediated decay). It might be studied whether these additional players influence tail length control inasmuch as they influence the polymer loop behavior described.

#### future things to layer in, roughly in order of importance..
* **the rate of tail length growth and the k_on/k_off of pabp, which determines when/which parts of polyA are naked (low L_p) vs. coated (high L_p)**
* A small but confusing detail that makes this story incomplete- does the PABP globule max out intrinsically or just exceed the energy of the PAP's interaction with the upstream protein complex, `breaking' it open? --> see if these things correspond.
* how does a growing poly(A) actually structure itself (surely not a perfect circle)? how does PABP-binding alter this?
* cooperativity of PABP binding.
* what about non-A's?
* can we predict tail length changes in poorer solvents? polya acylation?
