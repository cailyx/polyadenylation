# how does polyadenylation stop?
cailyx q. uci EiR/senior thesis project 2026

In the cell (we will consider mammalian), a freshly made strand of RNA is commonly extended further by a poly(A) polymerase successively adding A's to create a "poly(A) tail." Why, when, and how does tail growth stop? Thorough biochemical studies in the 90s and 2000s suggest a model in which at some critical point (term used non-technically), poly(A) polymerase experiences a large drop in processivity. Here we explore a way to understand this critical point as arising from a summation of __.

consider our piece of RNA, we call A0 for no poly(A) tail added yet, and 4 things-
* IP, "initial protein" that binds to the A0 (stand-in name for mPSF/CPSF that binds AAUAAA.);
* PAP, polymerase adding A's;
* POLYA, growing tail of A's;
* PABP, POLYA-binding protein that binds every some number of A's.

If we assume that IP is bound to PAP for some initial period of A-elongation (there is indeed an experimentally-determined IP-PAP binding interface.),

...then POLYA grows in essentially a loop. Surely this loop can't grow forever, so we suppose that the point at which the loop stops growing is precisely when PAP breaks contact from IP and loses processivity. Ie, let's suppose that the question, When does PAP lose processivity, might be formulated as the question, When can the loop no longer exist? To answer this, remove IP and PAP from the scenario only now consider the POLYA as a (negatively charged) polymer that grows in a loop, and PABP that binds with some affinity to some number of A's. We then formulate the problem as follows:



#### this yields 4 key stages in polyadenylation:
1. the starting stage, where the RNA is A0.
2. the loop-elongation stage, where the RNA is extended by some number of A's in a loop.
3. the PABP-packing stage, when PABPs pack onto A-binding sites stoichiometrically.
4. the breaking point- the loop is unsustainable.

the core move here is to try to explain how we get from step 3 to 4.

## model
so now we are set up to ask a few questions,

1. how many pabp's can pack into a pabp-polyA globule?
2. how fast

## contents
initial_pack.py gives the baseline answer to how many PABPs *could* pack inside a 20-nm globule.
overall_pack.py layers in additional energy costs of sfl;kj
salt.py is an analysis of how __, generates figure __.


## considerations.
It should be noted that it remains unclear (experimentally) whether the formation of such a globule is relevant to tail length control.
