# Electric-motors-fundamentals

# Technical Documents
This repository contains LaTeX technical documents with mathematical notations.

## Files
- `document.tex`: Source LaTeX file.
- `document.pdf`: Compiled PDF (if uploaded).

## How to Compile
1. Install a LaTeX distribution (e.g., MiKTeX).
2. Compile `document.tex` using `pdflatex` or a LaTeX editor like VS Code with LaTeX Workshop.

# Adding a guideline from Grok on Latex and Github
Testing: modifying the readme file for the second time. 
Also, adding the guideline on writing latex in VSCode and push to Github 


# Electric Motors Fundamentals

This repository contains technical documents, Python scripts, and Jupyter notebooks for electric motor analysis.

## Mathematical Concepts

### Phasor Addition
Phasors are used to represent sinusoidal signals. For two phasors with magnitudes \( A_1 \), \( A_2 \) and phase angles \( \theta_1 \), \( \theta_2 \), the resultant phasor is:

\[
A_r e^{j\theta_r} = A_1 e^{j\theta_1} + A_2 e^{j\theta_2}
\]

In rectangular form, this is:

\[
A_r \cos\theta_r + j A_r \sin\theta_r = (A_1 \cos\theta_1 + A_2 \cos\theta_2) + j (A_1 \sin\theta_1 + A_2 \sin\theta_2)
\]

$x^2 + y^2 = z^2$

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

### Space Vector Rotation
A rotating space vector at frequency \( f \) (e.g., 50 Hz) can be expressed as:

\[
\vec{V}(t) = V e^{j 2\pi f t}
\]

For a 50 Hz system, the angular frequency is \( \omega = 2\pi \cdot 50 = 314.16 \, \text{rad/s} \).

## Files
- `latex_docs/document.tex`: LaTeX document with equations.
- `python_scripts/example.py`: Plots phasor sums as `outputs/phasor_sum.png`.
- `notebooks/example.ipynb`: Animates a rotating vector as `outputs/rotating_vector.gif`.