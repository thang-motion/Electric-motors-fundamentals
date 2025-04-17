from fractions import Fraction
from math import gcd

# Define motor general parameters
Q = 12 # No. of slots
p = 10 # "p" is the no. of poles NOTE: Pyrhonen use "p" as Pole-pair
PP = int(p/2) # No. of pole-pairs
m = 3 # no. phases
t = gcd(Q,PP) # largest common divider between Q slot and Pole-pairs PP according to Pyrhonen
# "t" is the no. of layers in the star of slots plot
print("t = " + str(t) +" & Pole-pairs = " + str(PP))


y = 5 # the actual winding pitch => Corresponding to MCAD throw value
yQ = Q/(p) # the no. slots/ per pole

# alpha_u (degrees): is the angle between voltages in the slots in electrical degrees
# alpha_z (degrees): is the angle between two adjacent phasors in electrical degrees
# q = Q/p/m
q = Fraction(Q,p*m) # slot per pole per phase
z = q.numerator
n = q.denominator
q = z/n
print("n value = " + str(n))
print("n is odd? " +  str(n%2!=0))
print("q = " + str(q))
if t == PP:
    print("normal alpha_u cal")
    alpha_u = 360* PP/ Q # only true if t == PP
    alpha_z = alpha_u
else:
    print("method 2")
    Qp = Q/t
    alpha_z = 360/Qp
    if n%2!=0:# if n is odd => First grade winding - Pyrhonen Tab 2.7 
        alpha_u = n*alpha_z
    else:
        alpha_u = n/2*alpha_z
    # alpha_u = n*360/Q*t # second method for calculating slot angle if we have fractional slot design
print("alpha_z = " + str(alpha_z))
print("alpha_u = " + str(alpha_u))


skew_angle = 0 # mechanical skewing degree
# s_sp calculation based on skew_angle
if skew_angle == 0:
    s_sp = 0 # no skewing
else:
    s_sp = 360/Q/skew_angle # if s_sp =1 => skewing by 1 stator slot pitch

    
# Calculate k_wv for each V
harmonic_order = 20

# Define the list of V values (odd numbers from 1 to harmonic_order)
V_list = list(range(1, harmonic_order, 2))  # [1, 3, 5, 7, ..., harmonic_order]



