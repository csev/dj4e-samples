# Git Rollback Script (`rollback.sh`)

A bash script that allows you to roll back your git repository to any tag or to the latest commit on your current branch, discarding all local changes and untracked files.

## Overview

The `rollback.sh` script provides an interactive way to:
- View all git tags with their creation dates
- Roll back to any specific tag
- Roll back to the latest commit on the currently checked out branch
- Discard all local changes and untracked files

## Features

- **Interactive menu**: Easy-to-use numbered list of tags
- **Safety checks**: Warns about uncommitted changes before proceeding
- **Automatic branch detection**: Works with any branch you're currently on
- **Remote sync**: Fetches latest tags and branch updates from remote
- **Complete cleanup**: Removes both tracked changes and untracked files
- **Colored output**: Uses color coding for warnings, errors, and success messages

## Requirements

- Git must be installed
- Must be run from within a git repository
- Bash shell (standard on macOS and Linux)

## Usage

### Basic Usage

From any directory within your git repository:

```bash
./tools/rollback.sh
```

Or if you're already in the `tools` directory:

```bash
./rollback.sh
```

### What the Script Does

1. **Checks repository**: Verifies you're in a git repository
2. **Shows current branch**: Displays the branch you're currently on
3. **Warns about changes**: If you have uncommitted changes, it will warn you
4. **Fetches tags**: Attempts to fetch latest tags from remote
5. **Lists tags**: Displays all available tags with their creation dates
6. **Interactive selection**: Prompts you to choose a rollback option

### Options

When you run the script, you'll see:

```
Options:
  [0] Roll back to latest commit on '<branch-name>' (discard local changes)
  [1-N] Roll back to a specific tag
  [q] Quit
```

- **Option 0**: Rolls back to the latest commit on your current branch
  - Fetches latest from remote
  - Resets to `origin/<branch>` if available, otherwise `HEAD`
  - Discards all local changes and untracked files

- **Options 1-N**: Roll back to a specific tag
  - Selects the tag from the numbered list
  - Requires confirmation before proceeding
  - Discards all local changes and untracked files

- **Option q**: Quit without making any changes

## What Gets Discarded

⚠️ **WARNING**: This script will permanently discard:

- All uncommitted changes to tracked files
- All untracked files and directories
- Any local modifications

The script uses:
- `git reset --hard` to discard tracked file changes
- `git clean -fd` to remove untracked files and directories

## Examples

### Example 1: Roll back to latest commit on current branch

```bash
$ ./tools/rollback.sh
Git Rollback Script
Current directory: dj4e-samples
Current branch: feature-branch

Available tags:
===============
 1. v1.2.0                         2024-01-15 10:30:00 -0500
 2. v1.1.0                         2024-01-01 09:00:00 -0500
 3. v1.0.0                         2023-12-15 14:20:00 -0500

Options:
  [0] Roll back to latest commit on 'feature-branch' (discard local changes)
  [1-3] Roll back to a specific tag
  [q] Quit

Enter your choice: 0
```

### Example 2: Roll back to a specific tag

```bash
Enter your choice: 2

Rolling back to tag: v1.1.0
This will discard all local changes and untracked files!
Are you sure? (yes/no): yes
```

## Safety Features

1. **Confirmation prompts**: The script asks for confirmation before making destructive changes
2. **Status display**: Shows your current git status before proceeding
3. **Error handling**: Exits gracefully if not in a git repository
4. **Remote fallback**: Falls back to local HEAD if remote branch isn't available

## Troubleshooting

### "Error: Not a git repository!"

Make sure you're running the script from within a git repository. The script will automatically detect if you're in a git repo.

### "Could not fetch tags from remote"

This is a warning, not an error. The script will continue using local tags. This might happen if:
- You're not connected to the internet
- The remote repository is unavailable
- You don't have permission to fetch from remote

### No tags found

If your repository has no tags, the script will offer to roll back to the latest commit on your current branch instead.

## Notes

- The script works with any branch (not just master/main)
- Tags are sorted by creation date (newest first)
- The script preserves the `.git` directory and repository structure
- After rollback, you'll see the current HEAD commit displayed

## Related Tools

- `resetdb.py` - Reset Django database and migrations
- See `README_DB.md` for database reset documentation

