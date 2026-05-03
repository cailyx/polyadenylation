We separate energy gains represented by $E_{bind}$ and energy costs represented by $E_{strain}$:

\paragraph{$E_{strain}$} is composed of 1) a bending energy, $E_{bend}$, associated with 'wrapping in a circle' and is a function of the persistence length $l_p$ and the number of A's, $n$, and 2) an entropy term, $S_{loop}$, that reflects the probability of bringing two ends of a polymer together:

$E_{strain} = E_{bend}(l_p, n) + S_{loop}(n)$

\paragraph{$E_{bind}$} is a sum of the enthalpies of binding of PABP with polyA RNA, PABP self-associating, and PAP associating with mPSF. The first two terms scale with $n$ divided by the footprint of PABP, $f$. Somewhat unrealistically, we say the last two terms are only afforded to the loop conformation and not the linear.

$E_{bind} = (n/f)(\Delta H_{PABP-polyA} + \Delta H_{PABP-PABP}) + \Delta H_{PAP-mPSF}$

We sum these to get an energy associated with forming a polyA loop:
$E_{loop} = E_{bind} + E_{strain}$
