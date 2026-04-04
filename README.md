# how does polyadenylation stop?
cailyx q. uci EiR/senior thesis project 2026

In the cell, a freshly made strand of RNA is commonly extended further by a poly(A) polymerase (PAP) successively adding A's to create a "poly(A) tail." Why, when, and how does tail growth stop? Biochemical study (from the Wahle group and others) has suggested the following picture. PAP is tethered to a protein complex bound to the RNA just upstream of where the poly(A) tail starts as it quickly and processively adds A's-- *i.e., the tail forms in something of a loop*, and not simply linearly outward from the 3' end. As it grows in a loop, a poly(A)-binding protein (PABP) binds to the growing tail every some number of A's, until PAP undergoes a sudden and large drop in rate and processivity at around 250 A's. While it can continue further slowly and distributively, we will consider this the effective "stopping point" for polyadenylation to be explained. Because the 250-A-point corresponds experimentally to the point at which 1) PAP ceases to be stimulated by (and presumably, bound to) the upstream protein complex, and 2) the length that achieves a maximum polyA-PABP "globule" size (seen by electron microscopy), we here suggest the "stopping point" is just when the loop of polyA RNA breaks.

Here, then, we try to understand this stopping point by treating the growth of a poly(A) tail as essentially a polymer loop growing in size, whose configurational entropy and excluded volume effects are weighed at each additional A added against the enthalpic gains of 1) PABPs self-associating, 2) PABP-polyA binding, and 3) PAP-mPSF binding. 

crucially, the association rate of PABP will determine when we can treat the polyA as naked versus coated, each having different persistence lengths. We'll have
* An, a loop of n number of A's that grows from one end at rate k;
* B, a poly(A)-binding protein that binds f number of A's (the footprint) with a specified Kd, k_on, and k_off

This moreoever enables us to explore the effects of salt concentration, known to modulate the persistence length of charged polymers.

<img width="720" height="504" alt="cartoon" src="https://github.com/user-attachments/assets/8d35ea81-481f-441b-94f9-2197fddf712b" />


## considerations
It should be noted that it remains unclear whether such a physiologically relevant globule forms and if so what its structure is. There are also other interesting possibilities for explaining tail length control. For example, evidence that the nuclear poly(A)-binding protein (PABPN1) exhibits phase separation adds the possibility of tail length control at the level of multiple polyA-PABPs in coordination. There are also not only additional poly(A)-binding proteins (incl. the cytoplasmic PABPCs) which may work in concert to control length, but also other mRNA processing and degradation factors (PABPN1 is involved in *hyper*adenylation-mediated decay). It might be studied whether these additional players influence tail length control inasmuch as they influence the polymer loop behavior described, although in general, the single-base, fairly cheap to build, and structurally dynamic poly(A) tail makes it a potential platform for additional, yet to be explored regulatory mechanisms.

#### future things to layer in, roughly in order of importance..
* A small but confusing detail that makes this story incomplete- does the PABP globule max out intrinsically or just exceed the energy of the PAP's interaction with the upstream protein complex, `breaking' it open? --> see if these things correspond.
* how does a growing poly(A) actually structure itself (surely not a perfect circle)? how does PABP-binding alter this?
* cooperativity of PABP binding.
* what about non-A's?
