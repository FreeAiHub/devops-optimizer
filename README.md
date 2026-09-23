# devops-optimizer: a script that reports on a local Git repository

I wrote this to see, in one command, how big a checked-out Git repository is and which
objects it contains. It is one Python file, and it only reports: no command it runs changes
the repository.

## Status

Working, with a small scope. Last commit 2025-12-17.

## What is in the repository

- `tools/git_optimizer.py` is the whole tool. Checks that `git` is on `PATH`, finds the
  repository root with `git rev-parse --show-toplevel`, sums the size of the files in the
  working tree, runs `git rev-list --objects --all`, then prints four general
  recommendations. Confirmation: `tools/git_optimizer.py`.
- MIT license. Confirmation: `LICENSE`.

## Quick start

Requires Python 3 and `git`. No third-party packages, no install step.

```bash
git clone https://github.com/FreeAiHub/devops-optimizer.git
cd devops-optimizer
python3 tools/git_optimizer.py
```

Run it from inside any repository: it reports on the repository containing the current
directory, not on the one the script lives in.

## How it works

```
main()
  ├─ git --version                     → exit if git is missing
  ├─ git rev-parse --show-toplevel     → repository root, exit if not a repo
  ├─ sum of file sizes under the root  → "Current size: N MB"
  ├─ git rev-list --objects --all      → object list (output not parsed yet)
  └─ print four recommendations
```

`git rev-list` is called but its output is not used to compute anything, so the "Current
size" line measures the working tree, not `.git`.

## What is not here yet

- The size report covers the working tree. Packfiles and history are not measured, so the
  number is not the size the repository takes on a server.
- `git rev-list --objects --all` output is discarded. No large-object ranking, no
  before/after comparison.
- The tool prints recommendations but applies none of them: no `git gc`, no LFS migration,
  no history rewrite.
- Only one tool exists. A disk-space analyzer and a cleanup script were described in the
  earlier version of this README; neither file is in the repository.
- No tests, no CI.

## License

MIT. See `LICENSE`.
