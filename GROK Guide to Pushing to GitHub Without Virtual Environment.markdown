# Guide to Pushing to GitHub Without Including the Python Virtual Environment

This guide explains how to push files to your GitHub repository (`https://github.com/thg244/Electric-motors-fundamentals.git`) without including your Python virtual environment (e.g., `.venv/`). It builds on your setup on Windows 11 with VS Code, where you’re managing LaTeX (`.tex`), Python (`.py`), Jupyter Notebook (`.ipynb`), and generated (`.png`, `.gif`) files in `C:\Users\YourName\Documents\TechDoc`. The virtual environment is excluded using a `.gitignore` file, and the guide ensures you can commit and push desired files while addressing authentication and common Git errors.

## Prerequisites

- **Existing Setup**:
  - GitHub repository: `https://github.com/thg244/Electric-motors-fundamentals.git`.
  - VS Code on Windows 11 with Git installed and configured.
  - Python environment (e.g., `.venv/`) with NumPy, Matplotlib, Plotly, Jupyter, and Pillow.
  - MiKTeX and LaTeX Workshop for LaTeX documents.
- **Tools**:
  - Git Credential Manager enabled for authentication.
  - Personal Access Token (PAT) with `repo` scope for GitHub authentication.

## Step 1: Update `.gitignore` to Exclude the Virtual Environment

1. **Locate or Create** `.gitignore`:
   - In VS Code, open your project folder (`C:\Users\YourName\Documents\TechDoc`).
   - Check for `.gitignore` in the root (alongside `latex_docs/`, `python_scripts/`, etc.).
   - If missing, create it:
     - Right-click in Explorer, select **New File**, and name it `.gitignore`.
2. **Add Virtual Environment Rules**:
   - Open `.gitignore` and append or verify:

     ```plaintext
     # Python Virtual Environment
     .venv/
     venv/
     env/
     *.venv/
     *.env/
     ```
   - Include existing exclusions for LaTeX, Python, and Jupyter:

     ```plaintext
     # LaTeX
     *.aux
     *.log
     *.out
     *.synctex.gz
     
     # Python
     __pycache__/
     *.pyc
     *.pyo
     *.pyd
     .Python
     *.egg-info/
     
     # Jupyter Notebook
     .ipynb_checkpoints/
     
     # Optional: Temporary files
     *.bak
     *.swp
     ```
   - **Note**: Do not add `outputs/` or specific `.png`/`gif` files you want to commit (e.g., `phasor_sum.png`, `rotating_vector.gif`).
3. **Save** `.gitignore`:
   - Save to ensure Git ignores the virtual environment.

## Step 2: Remove Virtual Environment from Git Tracking (If Already Tracked)

1. **Check Git Status**:
   - In VS Code’s terminal (\`Ctrl+\`\`) or Command Prompt:

     ```bash
     cd C:\Users\YourName\Documents\TechDoc
     git status
     ```
   - Ensure `.venv/` or `venv/` is not listed in staged, modified, or untracked files.
2. **Remove from Git (If Tracked)**:
   - If `.venv/` was previously committed:

     ```bash
     git rm -r --cached .venv/
     ```
     - Replace `.venv/` with your virtual environment folder name (e.g., `venv/`).
     - This removes `.venv/` from Git’s index but keeps it locally.
3. **Commit the Removal**:

   ```bash
   git commit -m "Remove virtual environment from tracking"
   ```

## Step 3: Stage and Commit Desired Files

1. **Repository Structure**:
   - Your current structure:

     ```plaintext
     Electric-motors-fundamentals/
     ├── latex_docs/
     │   └── document.tex
     │   └── document.pdf
     ├── python_scripts/
     │   └── example.py
     ├── notebooks/
     │   └── example.ip
     ├── outputs/
     │   └── phasor_sum.png
     │   └── rotating_vector.gif
     ├── README.md
     ├── .gitignore
     └── .venv/  (ignored)
     ```
2. **Stage Files**:
   - In VS Code’s Source Control view (`Ctrl+Shift+G`):
     - Stage files (e.g., `python_scripts/example.py`, `notebooks/example.ipynb`, `outputs/phasor_sum.png`, `outputs/rotating_vector.gif`, `.gitignore`) by clicking `+` next to each.
     - Stage new or updated files (e.g., `latex_docs/document.tex`).
     - Verify `.venv/` is not staged.
   - Or, in the terminal:

     ```bash
     git add latex_docs/ python_scripts/ notebooks/ outputs/ README.md .gitignore
     ```
3. **Check Staged Files**:

   ```bash
   git status
   ```
   - Confirm only intended files (`.tex`, `.py`, `.ipynb`, `.png`, `.gif`, `.md`, `.gitignore`) are staged.
4. **Commit Changes**:
   - In VS Code, enter a commit message (e.g., “Add new Python files and update gitignore”) and click the checkmark.
   - Or, in the terminal:

     ```bash
     git commit -m "Add new Python files and update gitignore"
     ```

## Step 4: Pull Remote Changes

- To avoid errors like `non-fast-forward` or `unrelated histories`:

  ```bash
  git pull origin main
  ```
- If conflicts occur, resolve them in VS Code’s merge editor.
- If you see `refusing to merge unrelated histories`:

  ```bash
  git pull origin main --allow-unrelated-histories
  ```

## Step 5: Push to GitHub

1. **Push Changes**:

   ```bash
   git push origin main
   ```
2. **Authenticate**:
   - If prompted, enter:
     - **Username**: `thg244`
     - **Password**: Your PAT (e.g., `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`).
   - If no prompt appears:
     - Clear cached credentials:

       ```bash
       git credential-manager reject https://github.com
       git push origin main
       ```
     - Or embed credentials temporarily:

       ```bash
       git remote set-url origin https://thg244:ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx@github.com/thg244/Electric-motors-fundamentals.git
       git push origin main
       git remote set-url origin https://github.com/thg244/Electric-motors-fundamentals.git
       ```
   - Or use VS Code’s Source Control view:
     - Click `...` &gt; **Push**.
     - Enter credentials if prompted.
3. **Verify Credential Manager**:
   - Ensure Git Credential Manager is enabled:

     ```bash
     git config --global credential.helper manager
     ```
   - Check Windows Credential Manager (Control Panel &gt; User Accounts &gt; Credential Manager &gt; Windows Credentials) for `git:https://github.com`.

## Step 6: Verify on GitHub

- Visit `https://github.com/thg244/Electric-motors-fundamentals`.
- Confirm files:
  - `latex_docs/document.tex` (and `.pdf` if included).
  - `python_scripts/example.py`.
  - `notebooks/example.ipynb`.
  - `outputs/phasor_sum.png`, `rotating_vector.gif`.
  - Updated `.gitignore`, `README.md`.
- Ensure `.venv/` or its contents (e.g., `Scripts/`, `Lib/`) are **not** present.

## Step 7: Troubleshooting

- **Virtual Environment Still Tracked**:
  - If `.venv/` appears in `git status`:
    - Verify `.gitignore` includes `.venv/` and is saved.
    - Remove from tracking:

      ```bash
      git rm -r --cached .venv/
      git commit -m "Remove virtual environment"
      git push origin main
      ```
- **Authentication Issues**:
  - If `remote: Invalid username or password`:
    - Regenerate PAT (GitHub &gt; Settings &gt; Developer settings &gt; Personal access tokens &gt; Tokens (classic), `repo` scope).
    - Test:

      ```bash
      curl -u thg244 https://api.github.com/user
      ```
  - Share terminal output if push fails.
- **Push Errors**:
  - For `non-fast-forward`, pull first (Step 4).
  - Share full terminal output for other errors.
- **Large Files**:
  - For large `.gif` files, use Git LFS:

    ```bash
    git lfs install
    git lfs track "*.gif"
    git add .gitattributes outputs/rotating_vector.gif
    git commit -m "Track GIF with LFS"
    git push origin main
    ```
- **Repository Confirmation**:
  - If you meant `technical-documents`, update:

    ```bash
    git remote set-url origin https://github.com/thg244/technical-documents.git
    ```

## Step 8: Example Workflow for Future Pushes

- **Add New Files**:

  ```bash
  git add python_scripts/new_file.py outputs/new_output.png
  git commit -m "Add new Python script and output"
  ```
- **Pull and Push**:

  ```bash
  git pull origin main
  git push origin main
  ```
- **Authenticate**:
  - Use username (`thg244`) and PAT, or rely on cached credentials.

## Step 9: Connection to Prior Work

- **Virtual Environment**: Excludes `.venv/` from your Python setup (Feb 13, 2025).
- **File Types**: Manages LaTeX, Python, Jupyter, and outputs (April 3 and 14, 2025).
- **GitHub Issues**: Builds on resolving `unrelated histories` and authentication (April 17, 2025).

## Next Steps

- Add more `.py` or `.ipynb` files for electric motor simulations.
- Update `README.md` to document new scripts/outputs.
- Explore GitHub Actions for automation.

If issues arise, share:

- Terminal output (e.g., `git status`, `git push`).
- `.gitignore` contents.
- Repository name confirmation.
- Whether `.venv/` appears in `git status` or GitHub.