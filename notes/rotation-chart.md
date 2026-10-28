# A concrete rotation chart for equal weights

Set the centre of mass to zero and lambda to one. Choose labels 0 and n-1 with distinct positions, rotate their difference onto the positive x axis, and impose y0=y_last and x0>x_last. This chart excludes a collision of those two labelled bodies. Relabelling charts must cover every admissible configuration before a global count is claimed.

Take x0 through x_(n-2) and y1 through y_(n-2) as the 2n-3 coordinates. Then y0=y_last=-sum(y1,...,y_(n-2))/2 and x_last=-sum(x0,...,x_(n-2)).

Retain F0_x and both components of F1 through F_(n-2). Drop both components of F_last and F0_y. Translation gives F_last=-sum(F0,...,F_(n-2)). The torque identity therefore becomes sum((q_i-q_last) cross F_i)=0. When all retained equations vanish, this reduces to (x0-x_last) F0_y=0. The strict chart inequality implies F0_y=0 and then both dropped last-body components vanish. Thus this is a square equivalent system inside the chart.

The numerical module implements these equations for the parameter a. Tests recover the explicit equilateral and collinear three-body solutions for a=0 and a=1 and check the two identities on a generic point. They do not prove that a numerical search is exhaustive.

## Remaining compactness and counting work

A global certifier still needs proven upper size and lower collision-distance bounds for lambda=1, an atlas covering chart boundaries, and a precise permutation/reflection quotient with stabilizer accounting. No compact domain or complete count is asserted here. Those gaps prevent issue 1 from closing.
