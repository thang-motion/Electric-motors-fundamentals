# Phasor diagram - 12-Slot/ 10-Pole/ Double-layer/ Concentrated winding

**Inputs**:
- `Q` (int): Total number of slots in the motor (e.g., 12).
- `p` (int): Total number of poles in the motor (e.g., 10).
- `m` (int): Number of phases in the motor (e.g., 3 for a three-phase motor).

**What you calculate**:
- `t = gcd(Q, PP)`
- `Qp = Q / t`, `phasors_per_layer = int(Qp)`
- `alpha_u`

**Phasor assignment**:
- Explanation: Phasors start at 90 degrees and proceed clockwise by subtracting `alpha_u`. 
- Phase Order: Defined as: `["phase -U", "phase +W", "phase -V", "phase +U", "phase -W", "phase +V"]`
    - Assignment: CW or CCW

![Phasor diagram](concentrated_12s10p/phasor_diagram.gif)


# Distribution factor - 12-Slot/ 10-Pole/ Double-layer/ Concentrated winding

The distribution factor for the fundamental component is given as geometric sum/ sum of absolute values

![Phasor distribution - fundamental](concentrated_12s10p/phasor_sum.gif)


**Citation: DESIGN OF ROTATING ELECTRICAL MACHINES - Juha Pyrhonen**