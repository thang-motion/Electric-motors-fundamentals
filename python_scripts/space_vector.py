import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
omega = 2 * np.pi * 0.5  # Angular frequency (0.5 Hz for smooth rotation)
num_frames = 100  # Restore to 100 frames
# The generated animation will run for 2 seconds
t = np.linspace(0, 2, num_frames)  # Time array for 2 seconds
alpha = 2 * np.pi / 3  # 120 degrees in radians
beta = 4 * np.pi / 3   # 240 degrees in radians

# Define the complex exponential terms
e_alpha = np.cos(alpha) + 1j * np.sin(alpha)  # e^(j*2pi/3)
e_beta = np.cos(beta) + 1j * np.sin(beta)     # e^(j*4pi/3)

# Time-varying variables (rotating at angular speed omega)
theta = [0, 2*np.pi/3, 4*np.pi/3]  # Phase angles
# The following 3-phase variables representing
# a positive sequence with fa leading fb by 120deg, and fb leading fc by 120deg
fa = 1 * np.cos(omega * t - theta[0])
fb = 1 * np.cos(omega * t - theta[1])
fc = 1 * np.cos(omega * t - theta[2])

# Compute the space vector f
f = (2/3) * (fa + fb * e_alpha + fc * e_beta)

# Set up the plot with extra space on the right
fig, ax = plt.subplots(figsize=(10, 6))  # Increased width further to ensure space
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_xlabel('Real')
ax.set_ylabel('Imaginary')
ax.grid(False)
ax.set_aspect('equal')

# Plot the vectors using quivers with LaTeX labels
quiver_f = ax.quiver(0, 0, 0, 0, angles='xy', scale_units='xy', scale=1, color='black', width=0.01, label=r'$f$')  # Black arrow for f
quiver_fa = ax.quiver(0, 0, 0, 0, angles='xy', scale_units='xy', scale=1, color='red', width=0.01, label=r'$f_a$')  # Red arrow for fa
quiver_fb = ax.quiver(0, 0, 0, 0, angles='xy', scale_units='xy', scale=1, color='blue', width=0.01, label=r'$f_b$')  # Blue arrow for fb
quiver_fc = ax.quiver(0, 0, 0, 0, angles='xy', scale_units='xy', scale=1, color='darkgreen', width=0.01, label=r'$f_c$')  # Dark green arrow for fc

# Add a text element to display the time
time_text = ax.text(0.05, 0.95, '', transform=ax.transAxes, fontsize=12, verticalalignment='top')

# Add the equations as text elements on the right
eq_f = ax.text(1.05, 0.90, r'$f = \frac{2}{3} \left( f_a + f_b e^{j \frac{2\pi}{3}} + f_c e^{j \frac{4\pi}{3}} \right)$',
               transform=ax.transAxes, fontsize=12, verticalalignment='top')
eq_fa = ax.text(1.05, 0.80, r'$f_a(t) = \cos(\omega t)$',
                transform=ax.transAxes, fontsize=12, verticalalignment='top')
eq_fb = ax.text(1.05, 0.73, r'$f_b(t) = \cos(\omega t - \frac{2\pi}{3})$',
                transform=ax.transAxes, fontsize=12, verticalalignment='top')
eq_fc = ax.text(1.05, 0.66, r'$f_c(t) = \cos(\omega t - \frac{4\pi}{3})$',
                transform=ax.transAxes, fontsize=12, verticalalignment='top')

# Add the legend with LaTeX labels
ax.legend()

# Adjust the layout to ensure space for the equations
plt.subplots_adjust(left=0.1, right=0.8, top=0.9, bottom=0.1)  # Adjusted margins to ensure space

# Initialization function for animation
def init():
    quiver_f.set_UVC(0, 0)
    quiver_fa.set_UVC(0, 0)
    quiver_fb.set_UVC(0, 0)
    quiver_fc.set_UVC(0, 0)
    time_text.set_text('t = 0.00 sec')
    return quiver_f, quiver_fa, quiver_fb, quiver_fc, time_text

# Animation update function
def update(frame):
    # Safety check for frame index
    if frame >= len(f):
        frame = len(f) - 1  # Cap the frame to the last valid index
    
    # Get the real and imaginary parts of f at this frame
    real_f = np.real(f[frame])
    imag_f = np.imag(f[frame])
    
    # Update the quiver for f
    quiver_f.set_UVC(real_f, imag_f)
    
    # Update quivers for fa, fb, fc (projected as real values with phase rotation)
    quiver_fa.set_UVC(fa[frame] * np.cos(theta[0]), fa[frame] * np.sin(theta[0]))
    quiver_fb.set_UVC(fb[frame] * np.cos(theta[1]), fb[frame] * np.sin(theta[1]))
    quiver_fc.set_UVC(fc[frame] * np.cos(theta[2]), fc[frame] * np.sin(theta[2]))
    
    # Update the time text
    time_text.set_text(f't = {t[frame]:.2f} sec')
    
    return quiver_f, quiver_fa, quiver_fb, quiver_fc, time_text

# Create the animation with explicit frame range
ani = animation.FuncAnimation(fig, update, frames=range(num_frames), init_func=init, blit=False, interval=20)

# Save the animation as a .gif
try:
    ani.save('rotating_space_vector_with_latex_fixed.gif', writer='pillow', fps=50)
    print("Animation saved successfully.")
except Exception as e:
    print(f"Error saving animation: {e}")

# Variable to define the frame to plot as a static image
frame_to_plot = 1  # Example: plot the frame at the 2nd frame

# Safety check for frame_to_plot
if 0 <= frame_to_plot < num_frames:
    # Update the plot to the specified frame
    real_f = np.real(f[frame_to_plot])
    imag_f = np.imag(f[frame_to_plot])
    quiver_f.set_UVC(real_f, imag_f)
    quiver_fa.set_UVC(fa[frame_to_plot] * np.cos(theta[0]), fa[frame_to_plot] * np.sin(theta[0]))
    quiver_fb.set_UVC(fb[frame_to_plot] * np.cos(theta[1]), fb[frame_to_plot] * np.sin(theta[1]))
    quiver_fc.set_UVC(fc[frame_to_plot] * np.cos(theta[2]), fc[frame_to_plot] * np.sin(theta[2]))
    time_text.set_text(f't = {t[frame_to_plot]:.2f} sec')
    
    # Save the static plot as a .png
    plt.savefig(f'rotating_space_vector_frame_{frame_to_plot}.png', dpi=300, bbox_inches='tight')
    print(f"Static image saved for frame {frame_to_plot} at {t[frame_to_plot]:.2f} seconds.")
else:
    print(f"Invalid frame_to_plot value {frame_to_plot}. Must be between 0 and {num_frames-1}.")

plt.close()
