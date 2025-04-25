# Explanations of Phasor Diagram Function Modifications (April 24, 2025)

This document compiles explanations for all modifications made to the `plot_phasor_diagram` Python function on April 24, 2025. The function generates a phasor diagram for an electric motor and returns an array of phasor details. Each modification is explained below, including the purpose, key parameters, calculations, plotting logic, sorting, phase assignments, and example outputs. The Python code is not included, as it was provided separately.

## Initial Understanding of the Script
The original script generates a phasor diagram for an electric motor based on:
- **Q**: Number of slots.
- **p**: Number of poles.
- **m**: Number of phases.
- Derived quantities: pole-pairs (`PP`), layers (`t`), angles (`alpha_u`, `alpha_z`).

It uses NumPy for calculations, Matplotlib for plotting, and the `fractions` module for slot per pole per phase (`q`). Phasors are plotted as arrows, with some colored red (`U_phasors=[1, 8, 7, 2]`), organized in layers with radii `1 + 0.5*i`. Angles are calculated, phasors are plotted clockwise from 90°, and the plot is displayed.

## Modification 1: Convert to Function with 4 Inputs (Q, p, m, alpha_u)
**Request**: Convert the script into a function taking four inputs: `Q`, `p`, `m`, and `alpha_u`.

**Explanation**:
- **Purpose**: Create a reusable function that accepts `alpha_u` directly, bypassing its calculation.
- **Changes**:
  - Defined `plot_phasor_diagram(Q, p, m, alpha_u)`.
  - Removed calculations for `alpha_u` and `alpha_z`, using the input `alpha_u`.
  - Eliminated `q` calculation and debug print statements.
  - Replaced `plt.show()` with `plt.savefig('phasor_diagram.png')` and `plt.close(fig)` to save the plot and free memory.
  - Retained plotting logic (clockwise phasors, red `U_phasors`).
- **Parameters**:
  - `Q`: Total slots.
  - `p`: Total poles.
  - `m`: Number of phases.
  - `alpha_u`: Angular displacement between phasors (degrees).
- **Plotting**:
  - Phasors plotted as arrows from (0,0) on a circle, starting at 90°, moving clockwise by `alpha_u`.
  - Red coloring for `U_phasors=[1, 8, 7, 2]`.
- **Output**: Saves the plot as 'phasor_diagram.png'; no array returned.

## Modification 2: Function with 3 Inputs (Q, p, m)
**Request**: Ignore the 4-input function; create a function with three inputs: `Q`, `p`, `m`.

**Explanation**:
- **Purpose**: Revert to calculating `alpha_u` internally, using only `Q`, `p`, `m`.
- **Changes**:
  - Defined `plot_phasor_diagram(Q, p, m)`.
  - Restored original calculations for `alpha_u` and `alpha_z` based on whether `t == PP` or fractional slot design.
  - Removed debug print statements (e.g., `print("n value = "...`).
  - Kept `plt.savefig('phasor_diagram.png')` and `plt.close(fig)`.
  - Retained `U_phasors=[1, 8, 7, 2]` and plotting logic.
- **Parameters**:
  - `Q`, `p`, `m`: As above.
- **Angle Calculations**:
  - `PP = p/2`: Pole-pairs.
  - `t = gcd(Q, PP)`: Number of layers.
  - `Qp = Q/t`: Phasors per layer.
  - `q = Q/(p*m)`: Slot per pole per phase.
  - `n = q.denominator`: Used for winding type.
  - If `t == PP`: `alpha_u = 360 * PP / Q`.
  - Else: `alpha_z = 360 / Qp`, `alpha_u = n * alpha_z` (if `n` odd) or `n/2 * alpha_z` (if `n` even).
- **Plotting**: Same as original (clockwise, red `U_phasors`).
- **Output**: Saves the plot; no array returned.

## Modification 3: Return Array of Phasor Numbers in Counter-Clockwise Order
**Request**: Return an array of length `Q/t`, starting with `phasor_number=1`, followed by phasors in counter-clockwise order.

**Explanation**:
- **Purpose**: Provide an array listing phasor numbers in counter-clockwise order (opposite to the clockwise plotting) for the first layer.
- **Changes**:
  - Added `ccw_phasors` array of length `Q/t` (i.e., `phasors_per_layer`).
  - Set `ccw_phasors[0] = 1` (starting phasor).
  - For indices 1 to `Q/t-1`, computed counter-clockwise phasor numbers:
    - Used `(-i) % phasors_per_layer` to map to original phasor numbers (since plotting is clockwise, counter-clockwise reverses the order).
    - Adjusted to phasor numbers (1-based).
  - Kept plotting logic unchanged (clockwise).
  - Returned `ccw_phasors`.
- **Sorting**: No sorting; counter-clockwise order computed directly based on angular progression.
- **Output**:
  - Array for `Q=12`, `p=10`, `m=3`, `t=1`: `[1, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]`.
    - Phasor 1 at 90°, phasor 12 at 90°+150°=240° (mod 360), phasor 11 at 90°+300°=30° (mod 360), etc.
  - Plot saved as 'phasor_diagram.png'.
- **Note**: This modification focused on counter-clockwise order, not used in later steps.

## Modification 4: Return Array with Phasor Number and Angle
**Request**: Return an array of `[phasor_number, current_angle]` pairs for all phasors.

**Explanation**:
- **Purpose**: Capture each phasor's number and its plotting angle.
- **Changes**:
  - Initialized `phasor_angles` list to store `[phasor_number, current_angle]` during the plotting loop.
  - Appended pairs before updating `current_angle`.
  - Replaced `plt.show()` with `plt.close(fig)` after `plt.savefig('phasor_diagram.png')`.
  - Returned `phasor_angles`.
- **Output**:
  - Array length: `Q` (all phasors across all layers).
  - Example for `Q=12`, `p=10`, `m=3`, `t=1`, `alpha_u=150`:
    - `[[1, 90], [2, -60], [3, -210], [4, -360], [5, -510], [6, -660], [7, -810], [8, -960], [9, -1110], [10, -1260], [11, -1410], [12, -1560]]`.
    - Angles reflect clockwise plotting: 90°, 90°-150°=-60°, -60°-150°=-210°, etc.
- **Plotting**: Unchanged (clockwise, red `U_phasors`).
- **Note**: Negative angles were later addressed.

## Modification 5: Normalize Angles to [0, 360)
**Request**: Normalize `current_angle` in the returned array to [0, 360) to avoid negative/large angles (e.g., -1410°).

**Explanation**:
- **Purpose**: Ensure returned angles are in a standard range for clarity.
- **Changes**:
  - Used `normalized_angle = current_angle % 360` before appending to `phasor_angles`.
  - Stored `[phasor_number, normalized_angle]` pairs.
  - Kept plotting unchanged (uses `np.deg2rad(current_angle)`, unaffected by normalization).
- **Output**:
  - Example for `Q=12`, `p=10`, `m=3`:
    - `[[1, 90], [2, 300], [3, 150], [4, 0], [5, 210], [6, 60], [7, 270], [8, 120], [9, 330], [10, 180], [11, 150], [12, 0]]`.
    - Angles normalized: -60° → 300°, -210° → 150°, -360° → 0°, etc.
- **Plotting**: Unchanged.

## Modification 6: Sort Array by Normalized Angle Starting at 90°
**Request**: Sort the array by `normalized_angle`, starting with the phasor at 90°.

**Explanation**:
- **Purpose**: Reorder the array by angle, prioritizing the phasor at 90°.
- **Changes**:
  - Sorted `phasor_angles` using `key=lambda x: (x[1] - 90) % 360`.
- **Sorting Logic**:
  - `(x[1] - 90) % 360`: Maps 90° to 0, 91° to 1, ..., 89° to 359.
  - Ensures  sre 90° comes first, followed by increasing angles (wrapping at 360°).
  - Stable sort for equal angles (e.g., 150° for phasors 3 and 11).
- **Output**:
  - Example: `[[1, 90], [8, 120], [3, 150], [11, 150], [10, 180], [5, 210], [7, 270], [2, 300], [9, 330], [4, 0], [12, 0], [6, 60]]`.
- **Plotting**: Unchanged.

## Modification 7: Add Phase Designations
**Request**: Append phase designations: first `Q/t/m/2` phasors as "phase -U", next `Q/t/m/2` as "phase +W", then "-V", "+U", "-W", "+V".

**Explanation**:
- **Purpose**: Assign electrical phase labels to phasors in the sorted array.
- **Changes**:
  - Computed `elements_per_phase = Q/t/m/2`.
  - Defined `phase_order = ["phase -U", "phase +W", "phase -V", "phase +U", "phase -W", "phase +V"]`.
  - Created `phase_assignments` with `elements_per_phase` copies of each phase (6 groups).
  - Added "unassigned" for remaining phasors if `t>1` (later modified).
  - Output array: `[phasor_number, normalized_angle, phase]`.
- **Phase Assignment**:
  - For `Q=12`, `t=1`, `m=3`, `elements_per_phase=2`: 2 phasors per phase, covering 12 phasors.
- **Output**:
  - `[[1, 90, "phase -U"], [8, 120, "phase -U"], [3, 150, "phase +W"], [11, 150, "phase +W"], [10, 180, "phase -V"], [5, 210, "phase -V"], [7, 270, "phase +U"], [2, 300, "phase +U"], [9, 330, "phase -W"], [4, 0, "phase -W"], [12, 0, "phase +V"], [6, 60, "phase +V"]]`.
- **Plotting**: Unchanged (phasor number labels only).

## Modification 8: Add Layer Column
**Request**: Add a column for the layer index (`t`).

**Explanation**:
- **Purpose**: Include the layer (0 to `t-1`) in the output array to distinguish phasors across layers.
- **Changes**:
  - Stored `[phasor_number, normalized_angle, layer]` during plotting.
  - Final array: `[p[0], p[1], phase_assignments[i], p[2]]` (quadruples).
  - Layer index (`layer`) added from the plotting loop (0 for `t=1`).
- **Output**:
  - For `t=1`, all `layer=0`: `[[1, 90, "phase -U", 0], ..., [6, 60, "phase +V", 0]]`.
- **Plotting**: Unchanged.

## Modification 9: Sort by Layer, Then Angle
**Request**: Sort by layer (0 to `t-1`), then by `normalized_angle` within each layer.

**Explanation**:
- **Purpose**: Group phasors by layer, with each layer sorted by angle starting at 90°.
- **Changes**:
  - Grouped phasors into `layered_phasors` (one list per layer).
  - Sorted each layer by `(x[1] - 90) % 360`.
  - Concatenated layers: layer 0 phasors, then layer 1, etc.
- **Sorting Logic**:
  - `layered_phasors[i]`: Phasors for layer `i`.
  - Sort each layer by `(x[1] - 90) % 360` to start at 90°.
  - Combine layers in order (0, 1, ..., `t-1`).
- **Output**: Same as previous for `t=1` (single layer); for `t>1`, layers are distinctly grouped.
- **Plotting**: Unchanged.

## Modification 10: Repeat Phase Order for All Phasors
**Request**: Replace "unassigned" with repeated phase order for `t>1`.

**Explanation**:
- **Purpose**: Ensure all `Q` phasors receive a phase by cycling the phase order.
- **Changes**:
  - Removed "unassigned" fallback.
  - Used a `while` loop to repeat `phase_order` until `Q` assignments are made.
  - Truncated to exactly `Q` assignments.
- **Phase Assignment**:
  - `elements_per_phase = Q/t/m/2`.
  - Cycle `["phase -U", "phase +W", "phase -V", "phase +U", "phase -W", "phase +V"]` to cover all phasors.
  - For `t>1`, additional cycles ensure full coverage.
- **Output**: Unchanged for `t=1`; for `t>1`, all phasors assigned phases.
- **Plotting**: Unchanged.

## Modification 11: Add Detailed Comments
**Request**: Add more comments to explain the code and sorting logic.

**Explanation**:
- **Purpose**: Enhance code readability for better understanding.
- **Changes**:
  - Added detailed comments explaining:
    - Function purpose and parameters (`Q`, `p`, `m`).
    - Derived parameters (`PP`, `t`, `Qp`, `q`, `n`).
    - Angle calculations (`alpha_u`, `alpha_z`, normalization).
    - Plotting (arrows, radii, labels, red coloring).
    - Sorting (group by layer, sort by angle, concatenate).
    - Phase assignments (cycle phases for all `Q` phasors).
  - No functional changes to the code.
- **Sorting Logic Recap**:
  - Group phasors into `layered_phasors` by layer.
  - Sort each layer by `(x[1] - 90) % 360` to prioritize 90°.
  - Concatenate layers to prioritize layer order.
- **Phase Assignment Recap**:
  - Compute `elements_per_phase`.
  - Repeat phase order to cover `Q` phasors.
- **Output**: Identical to previous modification.
- **Plotting**: Unchanged.

## Modification 12: Reduce Text Size and Add Phase Labels in Plot
**Request**: Reduce the text size of phasor number labels in the plot and add phase designations (e.g., "(-U)") next to the numbers.

**Explanation**:
- **Purpose**: Make plot labels less prominent and include phase information for clarity.
- **Changes**:
  - Reduced `fontsize` from 10 to 8 in the `ax.text` call for phasor number labels.
  - Added phase designations to plot labels (e.g., "1 (-U)") using a mapping from full phase names (`"phase -U"`) to short forms (`"-U"`).
  - Computed phases in plotting order (`phase_assignments_plot`) to label phasors during plotting, using the same phase order as the output array.
  - Stored `[phasor_number, normalized_angle, layer, phase]` temporarily during plotting to track phases.
  - Output array unchanged: `[phasor_number, normalized_angle, phase, layer]`.
- **Plotting**:
  - Labels changed from phasor numbers (e.g., "1") to `f"{phasor_number} ({short_phase})"`, e.g., "1 (-U)".
  - Phases assigned in plotting order (phasor 1, 2, ..., 12), which caused a mismatch with the sorted output array.
- **Phase Assignment**:
  - Used `elements_per_phase = Q/t/m/2` to assign phases in plotting order.
  - Mismatch occurred: e.g., phasor 8 labeled "+U" in the plot but "phase -U" in the sorted array.
- **Output**:
  - Array unchanged: Correct phases (e.g., phasor 8 as "phase -U").
  - Plot labels: Incorrectly assigned due to plotting order (e.g., phasor 8 as "+U").
- **Plotting Output**:
  - Labels: "1 (-U)", "2 (+W)", "3 (-V)", ..., "12 (+V)" in plotting order, with `fontsize=8`.
  - Saved as 'phasor_diagram.png'.
- **Issue**: Plot phase labels did not match the sorted array's phase assignments, addressed in the next modification.

## Modification 13: Align Plot Phase Labels with Sorted Array
**Request**: Ensure plot phase labels (e.g., "8 (-U)") match the phase assignments in the sorted output array (e.g., phasor 8 as "phase -U").

**Explanation**:
- **Purpose**: Fix the mismatch between plot phase labels and the sorted output array's phase assignments, ensuring consistency (e.g., phasor 8 labeled "(-U)" in the plot to match "phase -U" in the array).
- **Changes**:
  - Computed the sorted array (`sorted_phasors`) and phase assignments (`phase_assignments`) before plotting text labels.
  - Created `phasor_to_phase`, a dictionary mapping `phasor_number` to its phase in the sorted array (e.g., `8: "phase -U"`).
  - Stored text coordinates (`text_x`, `text_y`) during the plotting loop for later use, appending them to `phasor_angles`.
  - After sorting and phase assignment, iterated through `phasor_angles` to add text labels using `phasor_to_phase` to retrieve the correct phase for each phasor number.
  - Retained `fontsize=8` for reduced text size.
  - Kept label format `f"{phasor_number} ({short_phase})"`, e.g., "8 (-U)".
  - Output array unchanged: `[phasor_number, normalized_angle, phase, layer]`.
- **Plotting**:
  - Arrows, radii, and red coloring (`U_phasors=[1, 8, 7, 2]`) unchanged.
  - Text labels now reflect the sorted array's phase assignments: e.g., "1 (-U)", "8 (-U)", "3 (+W)", instead of the previous plotting order labels.
  - Labels use `fontsize=8` and include shortened phases (e.g., "-U" for "phase -U").
- **Sorting**: Unchanged:
  - Group phasors by layer into `layered_phasors`.
  - Sort each layer by `(x[1] - 90) % 360` to start at 90°.
  - Concatenate layers (layer 0, then 1, etc.).
- **Phase Assignment**:
  - Phases assigned once for the sorted array, used for both the output array and plot labels via `phasor_to_phase`.
  - Ensures consistency: e.g., phasor 8 is "-U" in both the plot and the output array.
  - Phases cycled using `elements_per_phase = Q/t/m/2` to cover all `Q` phasors.
- **Output**:
  - Array unchanged: `[[1, 90, "phase -U", 0], [8, 120, "phase -U", 0], [3, 150, "phase +W", 0], [11, 150, "phase +W", 0], [10, 180, "phase -V", 0], [5, 210, "phase -V", 0], [7, 270, "phase +U", 0], [2, 300, "phase +U", 0], [9, 330, "phase -W", 0], [4, 0, "phase -W", 0], [12, 0, "phase +V", 0], [6, 60, "phase +V", 0]]`.
  - Plot labels now match: "1 (-U)", "8 (-U)", "3 (+W)", "11 (+W)", "10 (-V)", "5 (-V)", "7 (+U)", "2 (+U)", "9 (-W)", "4 (-W)", "12 (+V)", "6 (+V)".
  - Plot saved as 'phasor_diagram.png'.
- **Plotting Output**:
  - Labels corrected to align with the sorted array, using smaller text (`fontsize=8`).
  - Arrows plotted in original order (1, 2, ..., 12), but labels reflect sorted phases.
- **Note**: This modification resolved the mismatch issue, ensuring plot labels are consistent with the output array.

## Modification 14: Generate Updated .md Document
**Request**: Generate a `.md` document that explains all modifications made today, including the latest explanations, without including the Python code.

**Explanation**:
- **Purpose**: Compile a comprehensive document summarizing all modifications to the `plot_phasor_diagram` function, including the latest changes (text size reduction, phase label addition, and plot label alignment), for future reference.
- **Changes**:
  - Updated the previous `.md` document to include explanations for Modifications 12 and 13.
  - Added this section (Modification 14) to document the creation of the updated `.md`.
  - Maintained the structure: purpose, changes, parameters, calculations, plotting, sorting, phase assignments, and outputs.
  - Excluded Python code, focusing on explanations.
- **Parameters**: Not applicable (document creation).
- **Calculations**: None.
- **Plotting**: Not applicable.
- **Sorting**: Not applicable.
- **Phase Assignment**: Not applicable.
- **Output**:
  - This document, saved as a `.md` file.
  - No changes to the `plot_phasor_diagram` function or its output.
- **Note**: This modification is purely documentary, ensuring all prior work is clearly explained.

### Consistent Example Output (for `Q=12`, `p=10`, `m=3`)
- **Parameters**: `t = 1`, `phasors_per_layer = 12`, `q = 2/5`, `n = 5` (odd), `alpha_z = 360/12 = 30`, `alpha_u = 5 * 30 = 150`.
- **Angles (normalized)**: 90°, 300°, 150°, 0°, 210°, 60°, 270°, 120°, 330°, 180°, 150°, 0°.
- **Phasors**: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12].
- **Sorted Angles (layer 0)**: 90°, 120°, 150°, 150°, 180°, 210°, 270°, 300°, 330°, 0°, 0°, 60°.
- **Phasors (sorted)**: [1, 8, 3, 11, 10, 5, 7, 2, 9, 4, 12, 6].
- **Phases** (`elements_per_phase = 12/1/3/2 = 2`):
  - "phase -U": Phasors 1, 8.
  - "phase +W": Phasors 3, 11.
  - "phase -V": Phasors 10, 5.
  - "phase +U": Phasors 7, 2.
  - "phase -W": Phasors 9, 4.
  - "phase +V": Phasors 12, 6.
- **Final Array** (from Modification 7 onward):
  ```python
  [
      [1, 90, "phase -U", 0], [8, 120, "phase -U", 0], [3, 150, "phase +W", 0], [11, 150, "phase +W", 0],
      [10, 180, "phase -V", 0], [5, 210, "phase -V", 0], [7, 270, "phase +U", 0], [2, 300, "phase +U", 0],
      [9, 330, "phase -W", 0], [4, 0, "phase -W", 0], [12, 0, "phase +V", 0], [6, 60, "phase +V", 0]
  ]
  ```
- **Plot Output** (from Modification 13):
  - Labels: "1 (-U)", "8 (-U)", "3 (+W)", "11 (+W)", "10 (-V)", "5 (-V)", "7 (+U)", "2 (+U)", "9 (-W)", "4 (-W)", "12 (+V)", "6 (+V)", with `fontsize=8`.
  - Matches the sorted array's phase assignments.
  - Saved as 'phasor_diagram.png'.

### Notes
- The function evolved from a standalone script to a function returning a detailed array of phasor information, with plot enhancements for clarity.
- Sorting by layer then angle organizes phasors clearly, especially for `t>1`.
- Phase assignments cycle to ensure all phasors are labeled, with no "unassigned" labels.
- Plot modifications (text size reduction, phase labels, and alignment) improved visualization and consistency.
- The plot remains consistent, with red coloring for `U_phasors=[1, 8, 7, 2]`.
- For `t>1`, the array groups phasors by layer, and phases may span layers.
- This document provides a complete record of all modifications made on April 24, 2025, for future review.




# Explanation of Calculations in the `plot_phasor_diagram` Function

The `plot_phasor_diagram` function generates a phasor diagram for an electric motor, visualizing the spatial distribution of phasors (representing coil currents) in a stator with specified slots, poles, and phases. It also produces animation frames to show the step-by-step construction of the diagram. This document explains the key calculations performed in the function, focusing on the mathematical and logical steps used to compute phasor positions, angles, layers, and phase assignments.

## Function Overview

**Purpose**: The function calculates the angular positions and phase assignments of phasors for a motor's stator slots, plots them in a circular diagram (with multiple layers if needed), and generates animation frames for a .gif. The phasors are sorted by layer and angle, and each is labeled with a number and phase designation (e.g., "1 (-U)").

**Inputs**:
- `Q` (int): Total number of slots in the motor (e.g., 12).
- `p` (int): Total number of poles in the motor (e.g., 10).
- `m` (int): Number of phases in the motor (e.g., 3 for a three-phase motor).

**Outputs**:
- A list of `[phasor_number, normalized_angle, phase, layer]` quadruples, where:
  - `phasor_number`: Integer from 1 to `Q`, identifying each phasor.
  - `normalized_angle`: Angle in degrees [0, 360), representing the phasor's position.
  - `phase`: Phase designation (e.g., "phase -U", "phase +W").
  - `layer`: Layer index (0 to `t-1`, where `t` is the number of layers).
- A list of image arrays (frames) for creating an animated .gif (not covered in calculations).

## Key Calculations

The function performs several calculations to determine phasor positions, layers, and phase assignments. Below, each step is explained in detail.

### 1. Derived Parameters

The function calculates several parameters based on the inputs `Q`, `p`, and `m` to configure the phasor diagram:

- **Pole-Pairs (`PP`)**:
  - Formula: `PP = int(p / 2)`
  - Explanation: The number of pole-pairs is half the total number of poles, as each pole-pair consists of a north and south pole. For `p=10`, `PP=5`.
  - Purpose: Used in angle calculations and layer determination.

- **Number of Layers (`t`)**:
  - Formula: `t = gcd(Q, PP)`
  - Explanation: The number of layers is the greatest common divisor (GCD) of the number of slots (`Q`) and pole-pairs (`PP`). This determines how phasors are grouped into concentric layers in the diagram. For `Q=12` and `PP=5`, `t=gcd(12, 5)=1` (single layer). If `Q=12` and `p=4` (`PP=2`), `t=gcd(12, 2)=2` (two layers).
  - Purpose: Defines the number of radial layers for plotting phasors.

- **Phasors per Layer (`Qp` and `phasors_per_layer`)**:
  - Formula: `Qp = Q / t`, `phasors_per_layer = int(Qp)`
  - Explanation: The number of phasors per layer is the total number of slots divided by the number of layers. For `Q=12` and `t=1`, `Qp=12/1=12`, so `phasors_per_layer=12`. For `Q=12` and `t=2`, `Qp=12/2=6`, so `phasors_per_layer=6`.
  - Purpose: Determines how many phasors are plotted in each layer.

- **Slots per Pole per Phase (`q`)**:
  - Formula: `q = Fraction(Q, p * m)`
  - Explanation: The number of slots per pole per phase is calculated as a fraction, where `Q` is the total slots, `p` is the number of poles, and `m` is the number of phases. For `Q=12`, `p=10`, `m=3`, `q=12/(10*3)=12/30=2/5`. The numerator (`z=q.numerator=2`) and denominator (`n=q.denominator=5`) are extracted.
  - Purpose: Used to determine the winding type (integral or fractional) and angular displacements.

### 2. Angular Displacements

The function calculates the angular spacing between phasors, which depends on whether the motor has an integral or fractional slot winding:

- **Base Angle (`alpha_z`)**:
  - Formula: `alpha_z = 360 / Qp` (for fractional slot designs) or `alpha_z = alpha_u` (for integral slot designs).
  - Explanation: This is the base angular spacing in degrees. For fractional slot designs (`t != PP`), it’s the angle between phasors within a layer. For `Qp=12`, `alpha_z=360/12=30` degrees.

- **Phasor Angle (`alpha_u`)**:
  - Formula:
    - If `t == PP` (integral slot winding): `alpha_u = 360 * PP / Q`
    - If `t != PP` (fractional slot winding):
      - If `n` (denominator of `q`) is odd: `alpha_u = n * alpha_z`
      - If `n` is even: `alpha_u = n / 2 * alpha_z`
  - Explanation:
    - For integral slot windings (`t == PP`), the angle between consecutive phasors is based on the pole-pairs and slots. For `PP=5`, `Q=12`, `alpha_u=360*5/12=150` degrees.
    - For fractional slot windings, the angle depends on the winding type:
      - Odd `n` (first-grade winding): `alpha_u` is the denominator times the base angle. For `n=5`, `alpha_z=30`, `alpha_u=5*30=150` degrees.
      - Even `n` (second-grade winding): `alpha_u` is half the denominator times the base angle. For `n=4`, `alpha_z=30`, `alpha_u=(4/2)*30=60` degrees.
  - Purpose: Determines the angular step between consecutive phasors when plotting.

- **Current Angle**:
  - Initial Value: `current_angle = 90`
  - Update: `current_angle -= alpha_u` for each phasor.
  - Normalized Angle: `normalized_angle = current_angle % 360`
  - Explanation: Phasors start at 90 degrees (top of the plot, positive y-axis) and proceed clockwise by subtracting `alpha_u`. The angle is normalized to [0, 360) to avoid negative or large values. For `alpha_u=150`, the angles might be 90, -60 (normalized to 300), 150, etc.
  - Purpose: Positions each phasor on the diagram.

### 3. Layer Radii

- **Formula**: `radii = [1 + 0.5 * i for i in range(t)]`
- Explanation: Each layer is plotted at a different radius to avoid overlap. The first layer (index 0) has radius 1, the second (index 1) has radius 1.5, and so on. For `t=1`, `radii=[1]`; for `t=2`, `radii=[1, 1.5]`.
- Purpose: Defines the radial distance for plotting phasors in each layer, ensuring visual separation.

### 4. Phasor Plotting and Frame Generation

While not the focus of calculations, the plotting logic involves:
- **Shaft Scale**: `shaft_scale = 1 - (head_length / radius)`, where `head_length=0.05`. This adjusts the arrow length so the tip (including the arrowhead) lies on the circle of the given radius.
- **Coordinates**: For each phasor, the x and y coordinates are calculated as:
  - `angle_rad = np.deg2rad(current_angle)`
  - `x = radius * shaft_scale * np.cos(angle_rad)`
  - `y = radius * shaft_scale * np.sin(angle_rad)`
- **Text Position**: Labels are placed slightly beyond the arrow tip using:
  - `text_offset = 1.08 * radius`
  - `text_x = text_offset * np.cos(angle_rad - text_angle_offset / 180 * np.pi)`
  - `text_y = text_offset * np.sin(angle_rad - text_angle_offset / 180 * np.pi)`
  - where `text_angle_offset=7` degrees avoids overlap.
- **Frames**: Each phasor addition generates a frame, with the final frame including phase labels.

### 5. Phasor Sorting

Phasors are sorted to ensure consistent ordering in the output array:
- **Grouping by Layer**:
  - Phasors are grouped into `t` lists based on their layer index.
  - For each phasor `[number, angle, layer, text_coords]`, it’s added to `layered_phasors[layer]`.
- **Sorting by Angle**:
  - Within each layer, phasors are sorted by their normalized angle, starting at 90 degrees.
  - Sorting key: `(x[1] - 90) % 360`, where `x[1]` is the normalized angle. This maps 90° to 0, 91° to 1, ..., 89° to 359, ensuring phasors are ordered clockwise from the top.
- **Combining Layers**:
  - The sorted phasors are concatenated: layer 0, then layer 1, etc., into `sorted_phasors`.
- **Purpose**: Ensures the output array is ordered by layer and angle, matching the visual plot.

### 6. Phase Assignments

Phase designations are assigned to phasors based on the motor’s configuration:
- **Elements per Phase**:
  - Formula: `elements_per_phase = int(Q / t / m / 2)`
  - Explanation: Each phase (e.g., U, V, W) has positive and negative phasors (e.g., +U, -U). The number of phasors per phase direction is `Q/(t*m*2)`. For `Q=12`, `t=1`, `m=3`, `elements_per_phase=12/(1*3*2)=2`.
- **Phase Order**:
  - Defined as: `["phase -U", "phase +W", "phase -V", "phase +U", "phase -W", "phase +V"]`
  - This cyclic order ensures balanced phase distribution.
- **Assignment**:
  - Generate a list `phase_assignments` by repeating each phase `elements_per_phase` times until `Q` phasors are assigned.
  - For `Q=12`, `elements_per_phase=2`, the assignments might be: `[-U, -U, +W, +W, -V, -V, +U, +U, -W, -W, +V, +V]`.
- **Mapping**:
  - A dictionary `phasor_to_phase` maps each phasor number to its phase based on the sorted order.
- **Purpose**: Assigns each phasor a phase for labeling (e.g., “1 (-U)”) and for use in phasor sum calculations.

### 7. Final Output Array

- **Construction**:
  - Formula: `phasor_angles_with_phase = [[p[0], p[1], phase_assignments[i], p[2]] for i, p in enumerate(sorted_phasors)]`
  - Explanation: Combines the sorted phasor data (`p[0]=number`, `p[1]=normalized_angle`, `p[2]=layer`) with the corresponding phase from `phase_assignments`.
- **Format**: List of `[phasor_number, normalized_angle, phase, layer]` quadruples.
- **Example**: For `Q=12`, `p=10`, `m=3`, the output might include entries like `[1, 90, "phase -U", 0]`, `[2, 300, "phase -U", 0]`, etc., sorted by layer and angle.
- **Purpose**: Provides a structured representation of all phasors for further processing (e.g., phasor sum plots) and matches the plotted diagram.

## Example Calculation Walkthrough

For `Q=12`, `p=10`, `m=3`:
- **Derived Parameters**:
  - `PP = 10/2 = 5`
  - `t = gcd(12, 5) = 1`
  - `Qp = 12/1 = 12`, `phasors_per_layer = 12`
  - `q = 12/(10*3) = 12/30 = 2/5`, `z=2`, `n=5`
- **Angular Displacements**:
  - Since `t=1 != PP=5`, use fractional slot calculation.
  - `alpha_z = 360/12 = 30` degrees.
  - `n=5` (odd), so `alpha_u = 5 * 30 = 150` degrees.
  - Start at `current_angle=90`, then 90-150=-60 (normalized to 300), 300-150=150, etc.
- **Layer Radii**: `t=1`, so `radii=[1]`.
- **Sorting**:
  - Single layer (`t=1`), sort 12 phasors by angle from 90° clockwise.
  - Angles (e.g., 90, 300, 150, ...) are sorted as (90-90)%360=0, (300-90)%360=210, (150-90)%360=60, etc.
- **Phase Assignments**:
  - `elements_per_phase = 12/(1*3*2) = 2`
  - Assign: 2 *-U, 2 *+W, 2 *-V, 2 *+U, 2 *-W, 2 *+V.
- **Output**: A list of 12 quadruples, sorted by angle within the single layer, with phase labels.

## Notes
- **Winding Type**: The function handles both integral (`t == PP`) and fractional (`t != PP`) slot windings, affecting angle calculations.
- **Layering**: Multiple layers (`t > 1`) are rare for typical inputs but are supported for complex motor designs.
- **Animation**: The calculations support frame generation, but the plotting logic (e.g., arrow coordinates, text positions) is secondary to the core phasor computations.
- **Applications**: The output array is used for subsequent phasor sum calculations, as in `generate_phasor_list_for_X_phase` and `plot_multiple_phasor_sum`.

This document provides a comprehensive overview of the calculations in `plot_phasor_diagram`, making the function’s logic accessible to those analyzing electric motor phasor diagrams.


