# Development Tools

This repository includes helpful tools in the `tools/` directory for managing
your development environment:

## Environment Checkup Tool (`checkup.sh`)

A bash script that validates your Django development environment setup, checking
for common configuration issues and ensuring you're using the correct versions of
Python and Django. This is useful when setting up a new environment, troubleshooting
issues, or verifying your setup before starting work.

For detailed documentation, see [README_CHECKUP.md](README_CHECKUP.md)

## Git Rollback Tool (`rollback.sh`)

A bash script that allows you to roll back your git repository to any tag or
to the latest commit on your current branch, discarding all local changes and
untracked files. This is useful when you need to reset your working directory
to a clean state.

For detailed documentation, see [README_GIT.md](README_GIT.md)

## Database Reset Tool (`resetdb.py`)

A Python script that completely resets your Django project's database and
removes all migration files, allowing you to start fresh with a clean database
schema. This is particularly useful when migration files have become corrupted
or when you need to restructure your models significantly.

For detailed documentation, see [README_DB.md](README_DB.md)

