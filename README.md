
# Git and GitHub Basics

## Overview
This project demonstrates the fundamental Git and GitHub workflow for version control and project collaboration. It covers creating a local repository, tracking changes, recording commits, connecting to a remote repository, and publishing project files on GitHub.

## Learning Objectives
- Initialize and manage a local Git repository.
- Create and configure a public GitHub repository.
- Track and stage changes using Git.
- Record project changes through commits.
- Connect local and remote repositories.
- Push and pull changes between repositories.
- Clone an existing remote repository.
- Document a project using Markdown.
- Share project files through GitHub.

## Project Structure
```text
git-github-basics/
├── sample_data.py
└── README.md
```

## Files
- **`sample_data.py`** — A sample Python script demonstrating variables, user input, basic data types, counting, and string slicing.
- **`README.md`** — Project documentation describing the objectives, files, and Git workflow.

## Tools and Technologies
- **Git:** Version control and change tracking.
- **GitHub:** Remote repository hosting and project sharing.
- **Git Bash:** Command-line interface for running Git commands.
- **Python 3:** Programming language used for the sample script.
- **Markdown:** Format used to write this documentation.

## Git Workflow

### 1. Initialize a Repository
Create a project directory and initialize a local Git repository.

```bash
git init
```

### 2. Check Repository Status
Inspect the current state of the working directory.

```bash
git status
```

### 3. Stage and Commit Changes
Stage project files and record changes in the repository history.

```bash
git add .
git commit -m "Add project files"
```

### 4. View Commit History
Display the recorded commits.

```bash
git log --oneline
```

### 5. Connect to GitHub
Create a public repository on GitHub and connect it to the local repository.

```bash
git remote add origin <repository-url>
git branch -M main
```

### 6. Push and Pull Changes
Upload local commits to GitHub or retrieve and integrate remote changes.

```bash
git push -u origin main
git pull
```

### 7. Clone a Repository
Copy an existing remote repository to a local computer.

```bash
git clone <repository-url>
```

## Basic Git Workflow Summary
The fundamental workflow for recording and sharing changes is:

**Working Directory → Staging Area → Local Repository → Remote Repository**

- `git add` stages changes.
- `git commit` records changes locally.
- `git push` uploads commits to GitHub.
- `git pull` retrieves and integrates remote changes.
- `git clone` copies an existing repository to a local computer.

## Expected Deliverables
- A valid, public GitHub repository.
- A repository containing `sample_data.py`.
- A well-formatted `README.md`.
- At least two commits in the Git history.
- A screenshot of `git log` showing at least two commits.

## Author
Roza Alene
