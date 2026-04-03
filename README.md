# how does polyadenylation stop?
cailyx q. uci EiR/senior thesis project 2026

In the cell, a freshly made strand of RNA is commonly extended further by a poly(A) polymerase (PAP) successively adding A's to create a "poly(A) tail." Why, when, and how does tail growth stop? Biochemical study (from the Wahle group and others) has suggested the following picture. PAP is tethered to a protein complex bound to the RNA just upstream of where the poly(A) tail starts as it quickly and processively adds A's-- i.e., the tail forms in something of a loop, and not simply linearly outward from the 3' end. As it grows, a poly(A)-binding protein (PABP) binds to the growing tail every some number of A's. Then, PAP undergoes a sudden and large drop in rate and processivity at around 250 A's. While it can continue further, we will consider this the effective "stopping point" for polyadenylation to be explained. The 250-A-point corresponds experimentally to the point at which 1) PAP ceases to be stimulated by (and presumably, bound to) the upstream protein complex, and 2) the length that achieves a maximum polyA-PABP "globule" size (seen by electron microscopy). Here, then, I try to understand this stopping point by treating the growth of a poly(A) tail as essentially a circular polymer growing in diameter. PABPs packing onto the tail increase the stiffness of the polymer and introduce entropic costs that limit the growth of the loop at a defined point.   

We have
* An, a loop of n number of A's that grows from one end at rate k;
* B, a poly(A)-binding protein that binds f number of A's (the footprint) with some binding afifinty Kd


#### this yields 4 key stages in polyadenylation:
1. the starting stage, where the RNA is A0.
2. the loop-elongation stage, where the RNA is extended by some number of A's in a loop.
3. the PABP-packing stage, when PABPs pack onto A-binding sites stoichiometrically.
4. the breaking point- the loop exceeds

the core move here will be to explain how we get from step 3 to 4.

## sketch
how many pabp's can pack into a pabp-polyA globule? 

## contents
initial_pack.py gives the baseline answer to how many PABPs *could* pack inside a 20-nm globule without considering any entropic costs.

circle.py will give the persistence length of our circle polyA bound by PABP (modeled for now as simply a thicker strand...) (paul janmey tutorial)

grow_pack.py will model the energy of a growing loop

overall_grow_pack.py will layer in additional costs

salt.py is an analysis of how __, generates figure __.

## considerations
It should be noted that it remains unclear whether such a physiologically relevant globule forms and what its structure is. There are also other interesting possibilities for explaining tail length control. For example, the nuclear poly(A)-binding protein (PABPN1) exhibits phase separation, adding the possibility of tail length control at the level of multiple polyA-PABPs in coordination. There are also not only additional poly(A)-binding proteins (incl. the cytoplasmic PABPCs), but also almost certainly other proteins that ___, not to mention cis- or trans-acting factors. It might be studied wehter these additional players influence tail length control inasmuch as they influence the packing behavior described.

#### future things to layer in, roughly in order of importance..
* A small but confusing detail that makes this story incomplete- does the PABP globule max out intrinsically or just exceed the energy of the PAP's interaction with the upstream protein complex, `breaking' it open? --> see if these things correspond.
* of course, naked polyA emerges for some amount of time before PABP packs on. the rate at which this occurs should be considered against the avg rate of PABP association.
* how does a growing poly(A) actually structure itself (surely not a perfect circle)? how does PABP-binding alter this?
* cooperativity of PABP binding.
* what about non-A's?
