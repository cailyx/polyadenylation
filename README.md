# how does polyadenylation stop?
cailyx q. uci EiR/senior thesis project 2026

In the cell, a freshly made strand of RNA is commonly extended further by a poly(A) polymerase successively adding A's to create a "poly(A) tail." Why, when, and how does tail growth stop? Let's consider that a tail length control mechanism occurs at the level of each strand; then, we suggest there is a "point" that triggers the stop and is wanting of characterization. A lot of biochemical study has suggested key clues. Poly(A) polymerase is initially fast and processive; it has a binding interface with a protein complex bound just upstream of where the poly(A) tail starts; it undergoes a sudden and large drop in rate and processivity at a (noticeable, albeit fuzzy) point around 250 A's. 

then the formation of the poly(A) tail might be described as a circle that increases in diameter by successive additions of single A units. (moreover, since the sequence is simply AAAAA...etc., there is no base pairing, and so the lowest energy is achieved by expanding out into a circle.) suppose that the point at which the loop stops growing is precisely when PAP breaks contact from the upstream protein complex and loses processivity. so let's suppose that the original question, When does PAP lose processivity, is a question of when PAP breaks contact from the protein complex, which might be a consequence of when the energy of growing the poly(A) loop exceeds the maximal energy allowed.  

But a simple growing loop of poly(A) RNA is far from ___. how can ___? We have a poly(A) binding protein. We suggest this 

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

1. how many pabp's can pack into a pabp-polyA globule?
2. how fast does it have to 

## contents
initial_pack.py gives the baseline answer to how many PABPs *could* pack inside a 20-nm globule. this is just to 

grow_pack.py will model the energy of a growing loop, only considering the torsional stiffness of growing in a circle. 

overall_grow_pack.py will layer in additional costs

salt.py is an analysis of how __, generates figure __.


## considerations.
It should be noted that it remains unclear whether such a physiologically relevant globule forms and what its structure is. There are also other interesting possibilities for explaining tail length control. One thing we did not consider is the evidence that the nuclear poly(A)-binding protein (PABPN1) exhibits phase separation, adding the possibility of tail length control at the level of multiple polyA-PABPs in coordination. There are also not only additional poly(A)-binding proteins (incl. the cytoplasmic PABPCs), but also almost certainly other proteins that ___, not to mention cis- or trans-acting factors. However, here we have tried to show that a growing RNA loop of a single base type (A) combined with the kinetics of binding can produce the stopping point in tail growth. And it might be studied wehter these additional players influence tail length control inasmuch as they influence the packing behavior described.
