# Setup Guide — GitHub, VS Code, and Python

**FIN 4600 · Lab 3 · Financial Data Analytics**

Work through this once, in order. Budget about 45 minutes the first time.
When you reach the end you will have a working Python data science environment
and your own copy of the lab repository on GitHub.

If something goes wrong, jump to [Troubleshooting](#troubleshooting) at the
bottom before asking — the five most common problems are all listed there with
their fixes.

---

## Part 1 — GitHub account (10 minutes)

GitHub is where the code lives. It is version control, backup, and submission
in one place, and it is the single most visible line on a finance student's
résumé that says "I can work with data".

### 1.1 Create the account

1. Go to <https://github.com/signup>.
2. Use your **@mtu.edu email address**. This matters: it is what qualifies you
   for free student tools, and it is how the instructor identifies your work.
3. Choose a username you would be comfortable putting on a résumé.
   `jsmith-mtu` is fine. Something you picked in high school is not.
4. Verify the email GitHub sends you.

### 1.2 Turn on two-factor authentication

GitHub requires 2FA for all accounts that contribute code. Do it now rather
than being locked out at a deadline.

**Settings → Password and authentication → Two-factor authentication.**

An authenticator app (Microsoft Authenticator, Google Authenticator, Authy) is
better than SMS. Save the recovery codes somewhere you will still have them in
six months.

### 1.3 Claim your student benefits

Visit <https://education.github.com/pack> and apply with your MTU email.
Verification sometimes takes a day or two, and it is not required for this lab
— start the application and carry on with Part 2 while it processes.

---

## Part 2 — Visual Studio Code (10 minutes)

VS Code is the editor. It is free, it is what most working data teams use, and
it runs notebooks, a terminal, and Git in one window.

### 2.1 Install

Download from <https://code.visualstudio.com/> and install for your operating
system.

**Windows users:** during installation, tick **"Add to PATH"** if it is
offered. It saves trouble later.

### 2.2 Install the three extensions you need

Open VS Code, click the **Extensions** icon in the left sidebar (four squares),
and install:

| Extension | Publisher | What it does |
|---|---|---|
| **Python** | Microsoft | Language support, interpreter selection, debugging |
| **Jupyter** | Microsoft | Runs `.ipynb` notebooks inside VS Code |
| **GitHub Pull Requests** | GitHub | Sign-in and repository integration |

This repository also includes a `.vscode/extensions.json`, so when you open the
folder VS Code will offer to install exactly these. Say yes.

### 2.3 Sign in to GitHub from VS Code

Click the **account icon** at the bottom-left → **Sign in to sync settings** →
sign in with GitHub. This lets VS Code push your work without asking for a
password every time.

---

## Part 3 — Python, via uv (5 minutes)

**This is the part people usually get wrong, so we are going to sidestep it
entirely.**

The traditional advice is to install Python from python.org, then pip, then
learn about virtual environments, then discover that you have three Pythons and
the wrong one is first on your PATH. Every class loses a week to this.

Instead we use **uv**, a single tool that installs Python *for* this project,
creates the virtual environment, and installs the packages — from one command,
with no administrator rights, identically on Windows and macOS.

> **You do not need to install Python separately.** uv will download the exact
> version this project needs (3.12) and keep it inside the project folder.
> Nothing on your system changes.

### 3.1 Install uv

**Windows** — open **PowerShell** (press Start, type `powershell`, press Enter)
and paste:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS or Linux** — open **Terminal** and paste:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 3.2 Close the terminal and open a new one

The installer adds `uv` to your PATH, and a terminal that was already open will
not know about it. **Close it. Open a new one.** This single step resolves most
"uv is not recognised" reports.

### 3.3 Check it worked

```bash
uv --version
```

You should see something like `uv 0.8.17`. If you see "command not found" or
"not recognized", see [Troubleshooting](#uv-is-not-recognised).

---

## Part 4 — Get your own copy of the lab (5 minutes)

You will not work in the instructor's repository directly. You take your own
copy — a **fork** — make changes there, and push to it. That is exactly how
professional teams work.

### 4.1 Fork the repository

1. Go to the course repository on GitHub (the instructor will give you the link).
2. Click **Fork**, top right.
3. Leave the name as-is and click **Create fork**.

You now have `github.com/YOUR-USERNAME/mtu4600-lab3-analytics`.

### 4.2 Clone your fork to your computer

On **your** fork's page, click the green **Code** button and copy the HTTPS URL.

Then in VS Code:

1. **View → Command Palette** (`Ctrl+Shift+P` on Windows, `Cmd+Shift+P` on Mac)
2. Type `Git: Clone`, press Enter
3. Paste your URL
4. Choose a folder — somewhere sensible like `Documents\MTU` or `~/Documents/MTU`
5. When VS Code asks "Would you like to open the cloned repository?", click
   **Open**

> **Do not put the folder inside OneDrive, iCloud Drive, Dropbox, or Google
> Drive.** Cloud sync and virtual environments fight each other, and the
> symptoms are baffling. Use a plain local folder.

---

## Part 5 — Build the environment (5 minutes, mostly waiting)

In VS Code, open a terminal: **Terminal → New Terminal** (or `` Ctrl+` ``).
Confirm the prompt shows the repository folder, then run:

```bash
uv sync
```

That one command:

1. downloads Python 3.12 if you do not have it,
2. creates a `.venv` folder inside the project,
3. installs pandas, numpy, matplotlib, seaborn, scikit-learn and Jupyter at the
   exact versions recorded in `uv.lock`.

The first run takes two to five minutes and downloads several hundred megabytes.
Later runs take seconds.

Because of `uv.lock`, **every student in the class gets byte-identical package
versions**. When your output differs from someone else's, it is your code — not
your library versions.

---

## Part 6 — Run your first notebook (5 minutes)

1. In the VS Code file explorer, open `notebooks/00_environment_check.ipynb`.
2. Top right of the notebook, click **Select Kernel**.
3. Choose **Python Environments…** → the one whose path contains **`.venv`**.
   It will usually be labelled something like
   `.venv (Python 3.12.11)` and marked *Recommended*.
4. Click **Run All** at the top of the notebook.

Every cell should run without error, and you should see an Apple share price
chart near the bottom.

**If every cell ran, you are done with setup.** Go to
`notebooks/01_pandas_fundamentals.ipynb`.

---

## Part 7 — The working cycle

Once set up, this is your routine for every lab session.

### Each time you sit down

```bash
git pull                 # collect any fixes the instructor has pushed
```

### While you work

Edit notebooks, run cells, save with `Ctrl+S` / `Cmd+S`.

### When you have something worth keeping

Use the **Source Control** panel in VS Code (the branch icon in the left
sidebar):

1. Click the **+** next to each changed file to stage it.
2. Type a message that says what you did — `Completed notebook 02 exercises`,
   not `update`.
3. Click **Commit**.
4. Click **Sync Changes** to push to GitHub.

Or, in the terminal:

```bash
git add notebooks/02_returns_and_risk.ipynb
git commit -m "Completed notebook 02 exercises"
git push
```

**Commit often.** A commit is a save point you can return to. Committing after
each exercise is normal and good practice; committing once at the end of the
project is neither.

### Getting updates from the instructor's repository

If the instructor fixes something after you forked, pull it into your fork.
One-time setup:

```bash
git remote add upstream https://github.com/INSTRUCTOR-USERNAME/mtu4600-lab3-analytics.git
```

Then, whenever you need updates:

```bash
git fetch upstream
git merge upstream/main
```

---

## Troubleshooting

### `uv` is not recognised

Almost always an old terminal. **Close every terminal window and open a new
one**, then try `uv --version` again.

If it still fails:

- **Windows:** the installer puts uv in `%USERPROFILE%\.local\bin`. Check that
  the file exists there. If it does, restart VS Code entirely — not just the
  terminal.
- **macOS:** the installer puts it in `~/.local/bin`. Run
  `echo $PATH | tr ':' '\n' | grep local` to see whether that folder is on your
  PATH. If not, run `source ~/.zshrc` or open a fresh Terminal window.

### `uv sync` fails with an SSL or certificate error

You are probably on a restricted network. Try again on a different connection,
or on campus wired/eduroam rather than a guest network. Corporate VPNs are a
frequent cause.

### VS Code will not let me select the `.venv` kernel

1. Confirm `.venv` exists in the project folder. If not, `uv sync` did not
   finish — run it again and read the output.
2. Command Palette → **Developer: Reload Window**.
3. Command Palette → **Python: Select Interpreter** → **Enter interpreter
   path** → browse to:
   - Windows: `.venv\Scripts\python.exe`
   - macOS/Linux: `.venv/bin/python`

### `ModuleNotFoundError: No module named 'pandas'`

The notebook is running on the wrong Python. Run the first cell of
`00_environment_check.ipynb` — it prints which interpreter is in use. If the
path does not contain `.venv`, change the kernel as described in Part 6.

### `FileNotFoundError` when loading a CSV

You opened a single file rather than the project folder. Close VS Code, then
**File → Open Folder** and select the `mtu4600-lab3-analytics` folder itself —
not its parent, and not one of the notebooks.

### Git asks for a username and password and rejects my password

GitHub stopped accepting account passwords for Git operations in 2021. Sign in
through VS Code (Part 2.3) and it handles the credentials for you. If you are
using the terminal directly, install the
[GitHub CLI](https://cli.github.com/) and run `gh auth login`.

### `error: failed to push some refs`

Someone — usually you, from another machine — pushed since your last pull.

```bash
git pull --rebase
git push
```

### A notebook cell hangs on `[*]` forever

The kernel is stuck. Click **Restart** in the notebook toolbar, then
**Run All**. If it keeps happening on the same cell, look for an infinite loop
or an accidental `input()`.

### My charts do not appear

Make sure the cell ends with `plt.show()` and that you ran the setup cell at the
top of the notebook, which loads the shared style file.

### Everything is broken and I want to start over

Nothing in `.venv` is precious — it is rebuilt from `uv.lock` in minutes.

```bash
# Windows PowerShell
Remove-Item -Recurse -Force .venv
uv sync

# macOS / Linux
rm -rf .venv
uv sync
```

Your notebooks are untouched by this.

---

## Quick reference

| Task | Command |
|---|---|
| Build or repair the environment | `uv sync` |
| Run a script in the environment | `uv run python scripts/check_environment.py` |
| Add a package | `uv add package-name` |
| Check what is installed | `uv pip list` |
| Get instructor updates | `git pull` |
| Save and upload your work | `git add . && git commit -m "message" && git push` |
