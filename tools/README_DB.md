# Database Reset Script (`resetdb.py`)

A Python script that completely resets your Django project's database and removes all migration files, allowing you to start fresh with a clean database schema.

## Overview

The `resetdb.py` script provides a safe way to:
- Drop all tables in your Django database
- Delete all migration files (except `__init__.py`)
- Prepare your project for creating fresh migrations

This is particularly useful when:
- You need to restructure your models significantly
- Migration files have become corrupted or inconsistent
- You want to start with a clean database state
- You're refactoring your database schema

## Features

- **Version checking**: Verifies Python 3.x and Django are available before proceeding
- **Auto-detection**: Automatically finds your Django project root and settings
- **Multi-database support**: Works with SQLite, MySQL, and PostgreSQL
- **Safe foreign key handling**: Properly disables/enables foreign key constraints
- **Complete cleanup**: Removes migration files from all apps
- **Confirmation prompt**: Requires explicit confirmation before proceeding
- **Clear next steps**: Provides instructions for what to do after reset

## Requirements

- Running in the correct Virtual Environment with the correct version of Python and Django
- Django project with `manage.py` in the root directory
- Database configured in Django settings
- Appropriate database permissions

## Before You Start

Make sure you have the correct latest version of `dj4e-samples` and it is checked out to the correct version.  Also this resets any inadvertent changes you have made to `dj4e-samples`.

    cd (the folder where dj4e-samples is)/dj4e-samples

For example if you are working on the www.dj4e.com `market` assignment on PythonAnywhere.

    cd ~/dj4e-samples

Then 

    bash ./tools/rollback.sh
    git checkout django52
    git pull

These steps ensure you're working with the latest code from the correct branch 
in `dj4e-samples` before resetting your database.

## Usage

### Basic Usage

From any directory within your Django project (the folder with `manage.py`)

    python (the folder where dj4e-samples is)/dj4e-samples/tools/resetdb.py

For example if you are working on the www.dj4e.com `market` assignment on PythonAnywhere.

    python ~/dj4e-samples/tools/resetdb.py

The script will:
1. Check Python version (requires Python 3.x)
2. Check Django version (must be installed and available in your virtual environment)
3. Automatically find your Django project root (by looking for `manage.py`)
4. Detect your settings module
5. Connect to your database
6. Display version information
7. Ask for confirmation
8. Drop all tables
9. Delete all migration files

### What Gets Deleted

⚠️ **WARNING**: This script will permanently delete:

- **All database tables** in your Django database
- **All migration files** (`.py` files in `*/migrations/` folders, except `__init__.py`)
- **Compiled migration files** (`.pyc` files in `__pycache__` folders)

The script preserves:
- `__init__.py` files in migrations folders
- Your Django project code
- Your `settings.py` and other configuration files

## Example Output

```
============================================================
Database and Migration Reset Script
============================================================
Python version: 3.11.5
Django version: 4.2.7
============================================================
Found Django project at: /path/to/dj4e-samples
Using settings module: dj4e-samples.settings

This will DELETE ALL TABLES and ALL MIGRATION FILES!
Are you sure you want to continue? (yes/no): yes

Dropping all tables...
  Dropping table: auth_user
  Dropping table: django_migrations
  Dropping table: cats_cat
  ...
All tables dropped successfully.

Deleting migration files...
  Processing: /path/to/dj4e-samples/cats/migrations
    Deleting: /path/to/dj4e-samples/cats/migrations/0001_initial.py
    Deleting: /path/to/dj4e-samples/cats/migrations/0002_auto_20240101_1200.py
  Processing: /path/to/dj4e-samples/autos/migrations
    Deleting: /path/to/dj4e-samples/autos/migrations/0001_initial.py
  ...

Deleted 15 migration files.

============================================================
Reset completed successfully!
============================================================

Next steps:
  1. Run: python manage.py makemigrations
  2. Run: python manage.py migrate
  3. Run: python manage.py createsuperuser (if needed)
```

## After Running the Script

After the script completes, you need to recreate your database schema:

### Step 1: Create New Migrations

```bash
python manage.py makemigrations
```

This will create fresh migration files based on your current models.

### Step 2: Apply Migrations

```bash
python manage.py migrate
```

This will create all the tables in your database based on the new migrations.

### Step 3: Create Superuser (Optional)

If you need an admin user:

```bash
python manage.py createsuperuser
```

## Database Support

The script handles different database backends:

### SQLite
- Disables foreign key constraints before dropping tables
- Re-enables them after cleanup

### MySQL
- Disables foreign key checks before dropping tables
- Re-enables them after cleanup

### PostgreSQL
- Uses `CASCADE` when dropping tables to handle foreign key dependencies

## Settings Detection

The script automatically detects your Django settings module by:

1. Looking for common patterns:
   - `config/settings.py`
   - `settings.py`
   - `project/settings.py`
   - `mysite/settings.py`

2. Searching for any `settings.py` file in your project (excluding virtual environments and cache directories)

3. Converting the file path to a module path (e.g., `config/settings.py` → `config.settings`)

## Safety Features

1. **Confirmation required**: The script requires you to type "yes" to proceed
2. **Clear warnings**: Explicitly states what will be deleted
3. **Error handling**: Provides clear error messages if something goes wrong
4. **Project detection**: Verifies you're in a Django project before proceeding

## Troubleshooting

### "ERROR: Python 3.x is required!"

The script detected that you're not using Python 3.x. Solutions:
- Make sure you're using Python 3.x (check with `python --version` or `python3 --version`)
- Activate your virtual environment if you're using one
- Use `python3` instead of `python` if your system has both versions

### "WARNING: Django is not installed or not available in current environment!"

The script couldn't import Django. This usually means:
- Django is not installed in your current Python environment
- You're not in the correct virtual environment
- Django needs to be installed: `pip install django`

Solutions:
- Activate your project's virtual environment
- Install Django: `pip install django` or `pip install -r requirements.txt`
- Verify Django is installed: `python -c "import django; print(django.get_version())"`

### "Could not find manage.py"

Make sure you're running the script from within your Django project directory or a subdirectory. The script searches up the directory tree to find `manage.py`.

### "Could not find settings.py"

The script couldn't locate your settings file. Common solutions:
- Make sure `settings.py` exists in your project
- Check that it's not in a location the script ignores (like `.venv` or `__pycache__`)
- Try running from the project root directory

### Database Connection Errors

If you get database connection errors:
- Verify your database settings in `settings.py`
- Make sure your database server is running
- Check that you have appropriate permissions
- Verify database credentials are correct

### Permission Errors

If you get permission errors when deleting migration files:
- Check file permissions in your migrations folders
- Make sure you have write access to the project directory

## Important Notes

- **Backup first**: Consider backing up your database before running this script if you have important data
- **Development use**: This script is intended for development environments. Use caution in production
- **Team coordination**: If working in a team, coordinate before running this script, as it affects migration files that should be in version control
- **Version control**: After running this script, you'll need to commit the new migration files to git

## Related Tools

- `rollback.sh` - Roll back git repository to tags or latest commit
- See `README_GIT.md` for git rollback documentation

