# Git Commands — Complete Reference Guide

---

## 1. SETUP & CONFIGURATION

| Command | Description |
|--------|-------------|
| `git config --global user.name "Your Name"` | Set your global username |
| `git config --global user.email "you@example.com"` | Set your global email |
| `git config --global core.editor "code"` | Set VS Code as default editor |
| `git config --list` | List all configuration settings |
| `git config user.name` | Check current username |

---

## 2. INITIALIZE & CLONE

| Command | Description |
|--------|-------------|
| `git init` | Initialize a new local repository |
| `git init my-project` | Create a new folder and initialize repo inside it |
| `git clone <url>` | Clone a remote repository locally |
| `git clone <url> my-folder` | Clone into a specific folder name |
| `git clone --depth 1 <url>` | Shallow clone (only latest snapshot) |

---

## 3. STAGING & SNAPSHOTS

| Command | Description |
|--------|-------------|
| `git status` | Show working tree status (modified, staged, untracked) |
| `git add <file>` | Stage a specific file |
| `git add .` | Stage all changes in current directory |
| `git add -A` | Stage all changes (including deletions) |
| `git add -p` | Interactively stage chunks of changes |
| `git reset <file>` | Unstage a file (keep changes) |
| `git rm <file>` | Remove file from repo and working directory |
| `git rm --cached <file>` | Remove file from staging only (keep locally) |
| `git mv <old> <new>` | Move or rename a tracked file |

---

## 4. COMMITTING

| Command | Description |
|--------|-------------|
| `git commit -m "message"` | Commit staged changes with a message |
| `git commit -am "message"` | Stage tracked files and commit in one step |
| `git commit --amend` | Modify the last commit (message or files) |
| `git commit --amend --no-edit` | Amend last commit without changing message |

---

## 5. BRANCHING

| Command | Description |
|--------|-------------|
| `git branch` | List all local branches |
| `git branch -a` | List local and remote branches |
| `git branch <name>` | Create a new branch |
| `git branch -d <name>` | Delete a branch (safe — merged only) |
| `git branch -D <name>` | Force delete a branch |
| `git branch -m <old> <new>` | Rename a branch |
| `git switch <branch>` | Switch to a branch |
| `git switch -c <branch>` | Create and switch to a new branch |
| `git checkout <branch>` | Switch to a branch (older syntax) |
| `git checkout -b <branch>` | Create and switch to a new branch (older syntax) |

---

## 6. MERGING

| Command | Description |
|--------|-------------|
| `git merge <branch>` | Merge a branch into the current branch |
| `git merge --no-ff <branch>` | Merge with a merge commit (no fast-forward) |
| `git merge --squash <branch>` | Squash all commits into one before merging |
| `git merge --abort` | Abort an in-progress merge |
| `git mergetool` | Open merge conflict resolution tool |

---

## 7. REBASING

| Command | Description |
|--------|-------------|
| `git rebase <branch>` | Rebase current branch onto another |
| `git rebase -i HEAD~3` | Interactive rebase — edit last 3 commits |
| `git rebase --continue` | Continue after resolving conflicts |
| `git rebase --abort` | Abort the rebase process |
| `git rebase --skip` | Skip the current conflicting commit |

---

## 8. REMOTE REPOSITORIES

| Command | Description |
|--------|-------------|
| `git remote -v` | List remote connections |
| `git remote add origin <url>` | Add a remote named "origin" |
| `git remote remove <name>` | Remove a remote connection |
| `git remote rename <old> <new>` | Rename a remote |
| `git remote set-url origin <url>` | Change the URL of a remote |
| `git fetch` | Download changes from remote (don't merge) |
| `git fetch --all` | Fetch from all remotes |
| `git pull` | Fetch and merge remote changes |
| `git pull --rebase` | Fetch and rebase instead of merge |
| `git push` | Push current branch to remote |
| `git push origin <branch>` | Push a specific branch to remote |
| `git push -u origin <branch>` | Push and set upstream tracking |
| `git push --force` | Force push (overwrite remote — use carefully) |
| `git push origin --delete <branch>` | Delete a remote branch |

---

## 9. VIEWING HISTORY & LOGS

| Command | Description |
|--------|-------------|
| `git log` | Show full commit history |
| `git log --oneline` | Show compact one-line commit history |
| `git log --oneline --graph --all` | Visual branch graph |
| `git log -n 5` | Show last 5 commits |
| `git log --author="Name"` | Filter commits by author |
| `git log --since="2 weeks ago"` | Commits from last 2 weeks |
| `git log <file>` | Show history of a specific file |
| `git show <commit>` | Show details of a specific commit |
| `git diff` | Show unstaged changes |
| `git diff --staged` | Show staged changes |
| `git diff <branch1>..<branch2>` | Show diff between two branches |
| `git blame <file>` | Show who changed each line of a file |
| `git shortlog -sn` | Summary of commits per author |

---

## 10. UNDOING CHANGES

| Command | Description |
|--------|-------------|
| `git restore <file>` | Discard unstaged changes in a file |
| `git restore --staged <file>` | Unstage a file (keep changes) |
| `git revert <commit>` | Create a new commit that undoes a commit |
| `git reset HEAD~1` | Undo last commit (keep changes staged) |
| `git reset --soft HEAD~1` | Undo last commit (keep changes staged) |
| `git reset --mixed HEAD~1` | Undo last commit (keep changes unstaged) |
| `git reset --hard HEAD~1` | Undo last commit and discard all changes |
| `git clean -fd` | Remove untracked files and directories |

---

## 11. STASHING

| Command | Description |
|--------|-------------|
| `git stash` | Stash current uncommitted changes |
| `git stash save "message"` | Stash with a description |
| `git stash list` | List all stashes |
| `git stash pop` | Apply latest stash and remove it |
| `git stash apply stash@{0}` | Apply a specific stash (keep it) |
| `git stash drop stash@{0}` | Delete a specific stash |
| `git stash clear` | Delete all stashes |
| `git stash branch <branch>` | Create a branch from a stash |

---

## 12. TAGGING

| Command | Description |
|--------|-------------|
| `git tag` | List all tags |
| `git tag <name>` | Create a lightweight tag |
| `git tag -a v1.0 -m "message"` | Create an annotated tag |
| `git tag -a v1.0 <commit>` | Tag a specific commit |
| `git push origin <tag>` | Push a tag to remote |
| `git push origin --tags` | Push all tags to remote |
| `git tag -d <name>` | Delete a local tag |
| `git push origin --delete <tag>` | Delete a remote tag |

---

## 13. SEARCHING

| Command | Description |
|--------|-------------|
| `git grep "keyword"` | Search for a keyword in tracked files |
| `git grep -n "keyword"` | Search with line numbers |
| `git log --all --grep="keyword"` | Search commit messages for keyword |
| `git log -S "keyword"` | Find commits that added/removed keyword |

---

## 14. CHERRY-PICK

| Command | Description |
|--------|-------------|
| `git cherry-pick <commit>` | Apply a specific commit to current branch |
| `git cherry-pick <c1>..<c2>` | Apply a range of commits |
| `git cherry-pick --abort` | Abort a cherry-pick in progress |
| `git cherry-pick --continue` | Continue after resolving conflicts |

---

## 15. SUBMODULES

| Command | Description |
|--------|-------------|
| `git submodule add <url>` | Add a submodule |
| `git submodule init` | Initialize submodules |
| `git submodule update` | Update submodules |
| `git submodule update --init --recursive` | Init and update all nested submodules |
| `git clone --recurse-submodules <url>` | Clone repo with all submodules |

---

## 16. GITIGNORE

| Task | How |
|------|-----|
| Ignore a file | Add filename to `.gitignore` (e.g. `secret.txt`) |
| Ignore a folder | Add `folder/` to `.gitignore` |
| Ignore by extension | Add `*.log` or `*.pyc` |
| Ignore but already tracked | `git rm --cached <file>` then add to `.gitignore` |
| Check what is ignored | `git check-ignore -v <file>` |
| Global gitignore | `git config --global core.excludesfile ~/.gitignore_global` |

---

## 17. ALIASES (Shortcuts)

```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.lg "log --oneline --graph --all"
git config --global alias.undo "reset --soft HEAD~1"
```

Usage: `git st`, `git lg`, `git undo`

---

## 18. USEFUL WORKFLOWS

### Start a new project
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <url>
git push -u origin main
```

### Feature branch workflow
```bash
git switch -c feature/my-feature   # create branch
# ... make changes ...
git add .
git commit -m "Add my feature"
git push origin feature/my-feature
git switch main
git merge feature/my-feature
git branch -d feature/my-feature
```

### Undo last commit safely
```bash
git reset --soft HEAD~1    # keeps your changes staged
```

### Sync fork with upstream
```bash
git remote add upstream <original-repo-url>
git fetch upstream
git merge upstream/main
```

---

*Generated for the ML with Python — Data Science Course*
