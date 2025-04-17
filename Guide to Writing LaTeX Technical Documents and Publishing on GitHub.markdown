# Step-by-Step Guide to Writing LaTeX Technical Documents and Publishing on GitHub

This guide walks you through creating a technical document with mathematical notations using LaTeX, managing it with Visual Studio Code (VS Code) on Windows 11, and publishing it to GitHub. It assumes you have a GitHub account but are new to using it.

## Prerequisites

- **Windows 11** with VS Code installed.
- **GitHub account** (you have one but haven’t used it).
- **LaTeX distribution**: Install MiKTeX (or another LaTeX distribution like TeX Live).
- **Git**: For version control and GitHub integration.
- **VS Code extensions**: For LaTeX editing and GitHub integration.

## Step 1: Set Up Your Environment

### 1.1 Install MiKTeX

1. Download MiKTeX from miktex.org.
2. Run the installer and follow the prompts to install MiKTeX.
3. During installation, choose to install missing packages automatically (recommended for beginners).
4. After installation, open the **MiKTeX Console** (search for it in the Start menu) and click **Check for Updates** to ensure it’s up to date.

### 1.2 Install Git

1. Download Git from git-scm.com.
2. Run the installer, accepting default settings unless you have specific preferences.
3. Verify installation by opening a Command Prompt (`cmd`) and typing:

   ```
   git --version
   ```

   You should see the Git version (e.g., `git version 2.46.0.windows.1`).

### 1.3 Configure VS Code

1. Open VS Code.
2. Install the following extensions (via the Extensions view, `Ctrl+Shift+X`):
   - **LaTeX Workshop**: For LaTeX editing and compilation.
   - **GitLens**: For Git integration (optional but helpful).
3. Configure LaTeX Workshop:
   - Go to `File > Preferences > Settings` or press `Ctrl+,`.
   - Search for `latex-workshop.latex.recipes`.
   - Ensure a recipe exists for `pdflatex` (it’s included by default). If not, add this to your `settings.json` (accessible via `Ctrl+Shift+P`, then `Preferences: Open Settings (JSON)`):

     ```json
     "latex-workshop.latex.recipes": [
       {
         "name": "pdflatex",
         "tools": [
           "pdflatex"
         ]
       }
     ],
     "latex-workshop.latex.tools": [
       {
         "name": "pdflatex",
         "command": "pdflatex",
         "args": [
           "-synctex=1",
           "-interaction=nonstopmode",
           "-file-line-error",
           "%DOC%"
         ]
       }
     ]
     ```

## Step 2: Create a Simple LaTeX Document

1. **Create a Project Folder**:

   - Create a folder, e.g., `C:\Users\YourName\Documents\TechDoc`.
   - Open this folder in VS Code (`File > Open Folder`).

2. **Create a LaTeX File**:

   - In VS Code, create a new file named `document.tex`.

   - Add the following sample LaTeX code with mathematical notations:

     ```latex
     \documentclass{article}
     \usepackage{amsmath}
     \title{Sample Technical Document}
     \author{Your Name}
     \date{April 2025}
     
     \begin{document}
     
     \maketitle
     
     \section{Introduction}
     This document demonstrates basic mathematical notations using LaTeX.
     
     \section{Mathematical Examples}
     Below are some sample equations.
     
     \subsection{Quadratic Formula}
     The quadratic formula solves equations of the form $ax^2 + bx + c = 0$:
     \begin{equation}
     x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
     \end{equation}
     
     \subsection{Summation}
     A simple summation example:
     \begin{equation}
     \sum_{i=1}^{n} i = \frac{n(n+1)}{2}
     \end{equation}
     
     \section{Conclusion}
     These equations are rendered using LaTeX and can be compiled into a PDF.
     
     \end{document}
     ```

3. **Compile the Document**:

   - Save `document.tex`.
   - In VS Code, open the LaTeX Workshop sidebar (click the TeX icon on the left).
   - Click the **Build LaTeX project** button (or press `Ctrl+Alt+B`).
   - If MiKTeX is set up correctly, it will generate `document.pdf` in the same folder.
   - View the PDF by clicking **View LaTeX PDF** in the LaTeX Workshop sidebar (or `Ctrl+Alt+V`).

4. **Troubleshooting**:

   - If compilation fails, check the **Output** panel in VS Code (select `LaTeX Workshop` from the dropdown).
   - Common issues: Missing MiKTeX packages (MiKTeX should install them automatically) or syntax errors in the `.tex` file.

## Step 3: Set Up Git and GitHub

### 3.1 Configure Git

1. Open a Command Prompt or VS Code’s integrated terminal (\`Ctrl+\`\`).
2. Set your Git username and email (replace with your details):

   ```
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

### 3.2 Create a GitHub Repository

1. Go to github.com and sign in.
2. Click the **+** icon in the top-right corner and select **New repository**.
3. Fill in:
   - Repository name: e.g., `technical-documents`.
   - Description: Optional, e.g., “LaTeX technical documents”.
   - Visibility: Public or Private (Public for this guide).
   - Initialize with a README: Check this box.
   - Add `.gitignore`: Select `TeX` to ignore LaTeX auxiliary files (e.g., `.aux`, `.log`).
4. Click **Create repository**.

### 3.3 Initialize Git in Your Project

1. In VS Code’s terminal, navigate to your project folder:

   ```
   cd C:\Users\YourName\Documents\TechDoc
   ```
2. Initialize a Git repository:

   ```
   git init
   ```
3. Link to your GitHub repository (replace `your-username` and `technical-documents` with your GitHub username and repository name):

   ```
   git remote add origin https://github.com/your-username/technical-documents.git
   ```

### 3.4 Commit and Push Your Document

1. Add your files to Git:

   ```
   git add document.tex
   ```

   (Note: Avoid adding `document.pdf` or auxiliary files; the `.gitignore` should exclude them.)

2. Commit the changes:

   ```
   git commit -m "Add initial LaTeX document"
   ```

3. Push to GitHub:

   ```
   git push -u origin main
   ```

4. If prompted, authenticate with your GitHub credentials (you may need to generate a Personal Access Token):

   - Go to GitHub &gt; Settings &gt; Developer settings &gt; Personal access tokens &gt; Tokens (classic).
   - Generate a new token with `repo` scope, copy it, and use it as your password in the terminal.

5. Verify on GitHub:

   - Visit your repository (e.g., `https://github.com/your-username/technical-documents`).
   - Confirm that `document.tex` is uploaded.

## Step 4: Publish and Share

1. **Compile on GitHub (Optional)**:

   - GitHub doesn’t render LaTeX directly, but you can compile `document.tex` locally and upload `document.pdf` to your repository:

     ```
     git add document.pdf
     git commit -m "Add compiled PDF"
     git push
     ```
   - Alternatively, use a service like Overleaf to share live LaTeX previews (not covered here).

2. **Share Your Repository**:

   - Share the repository URL (e.g., `https://github.com/your-username/technical-documents`).
   - Others can download `document.tex` and compile it locally or view `document.pdf` if uploaded.

3. **Add a README**:

   - Create `README.md` in your project folder:

     ```markdown
     # Technical Documents
     This repository contains LaTeX technical documents with mathematical notations.
     
     ## Files
     - `document.tex`: Source LaTeX file.
     - `document.pdf`: Compiled PDF (if uploaded).
     
     ## How to Compile
     1. Install a LaTeX distribution (e.g., MiKTeX).
     2. Compile `document.tex` using `pdflatex` or a LaTeX editor like VS Code with LaTeX Workshop.
     ```
   - Commit and push:

     ```
     git add README.md
     git commit -m "Add README"
     git push
     ```

## Step 5: Maintain Your Project

- **Edit Your Document**:
  - Open `document.tex` in in VS Code, make changes (e.g., add more equations), and recompile.
  - Example addition:

    ```latex
    \subsection{Pythagorean Theorem}
    For a right triangle with sides $a$, $b$, and hypotenuse $c$:
    \begin{equation}
    a^2 + b^2 = c^2
    \end{equation}
    ```
- **Update GitHub**:
  - After editing, commit and push:

    ```
    git add document.tex
    git commit -m "Add Pythagorean theorem"
    git push
    ```
- **Collaborate** (Optional):
  - Invite collaborators via GitHub’s repository settings.
  - Use branches for experimental changes (e.g., `git branch new-feature`, `git checkout new-feature`).

## Tips

- **Backup**: Your files are safe on GitHub, but keep local backups.
- **Learn More LaTeX**: Explore packages like `amsmath`, `tikz` (for diagrams), or `bibentry` (for references).
- **Automate Compilation**: Use GitHub Actions to auto-compile LaTeX to PDF (advanced, not covered here).
- **VS Code Shortcuts**: Use `Ctrl+Alt+B` to build and `Ctrl+Alt+V` to view the PDF.

## Troubleshooting

- **LaTeX Errors**: Check the VS Code Output panel for specific error messages (e.g., missing packages or syntax issues).
- **Git Push Issues**: Ensure you’re authenticated (use a Personal Access Token if password authentication fails).
- **GitHub Access**: If you chose a private repository, share access with collaborators explicitly.

You now have a LaTeX document with mathematical notations and a GitHub repository to share it. Happy documenting!