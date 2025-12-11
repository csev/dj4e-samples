# Environment Checkup Script (`checkup.sh`)

A bash script that validates your Django development environment setup on PythonAnywhere, checking for common configuration issues and ensuring you're using the correct versions of Python and Django.   This also looks for unnecessary files and folders that many students create by mistake when things go wrong.

This is less useful for an environment outside PythonAnywhere but it should be harmless.

## Overview

The `checkup.sh` script performs a comprehensive check of your PythonAnywhere development environment to ensure:
- You're running in the correct virtual environment
- Python and Django versions are within acceptable ranges
- Your project folder structure follows best practices
- Configuration files have the correct settings

This script is particularly useful when:
- Setting up a new development environment
- Troubleshooting environment issues
- Verifying your setup before starting work
- Ensuring consistency across different machines

## Features

- **Virtual environment validation**: Verifies you're using the correct virtual environment (`.ve52`)
- **Version checking**: Validates Python (3.10.0 - 3.13.9) and Django (5.2 - 5.9) versions
- **Folder structure validation**: Checks for old or incorrectly placed project folders
- **Configuration validation**: Verifies important settings in Django configuration files
- **Automatic patching**: Applies patches to `manage.py` files to warn about using `runserver` if we are on PythonAnywhere
- **Clear error reporting**: Provides specific warnings and error messages

## Requirements

- Bash shell (standard on macOS and Linux)
- Must be run from within your Django development environment
- Access to your home directory and Django projects

## Usage

### Basic Usage

Since `checkup.sh` scans your entire home folder on PythonAnywhere you
can run it as follows:

    bash ~/dj4e-samples/tools/checkup.sh

### What the Script Checks

The script performs the following checks in order:

1. **Virtual Environment Check**
   - Verifies you're running in a virtual environment
   - Ensures you're using `.ve52` (not `django42` or other environments)
   - Exits with error if virtual environment is incorrect

2. **Python Version Check**
   - Validates Python version is between 3.10.0 and 3.13.9
   - Warns if version is outside the acceptable range

3. **Django Version Check**
   - Validates Django version is between 5.2 and 5.9
   - Warns if version is outside the acceptable range

4. **Folder Structure Validation**
   - Checks for old/incorrect folder locations:
     - `~/djangotutorial` (should not exist)
     - `~/mysite` (should not exist)
     - `~/django_projects/djangotutorial` (should not exist)
     - `~/polls` (should not exist)
     - `~/locallibrary` (should not exist)
     - `~/django_projects/mysite/locallibrary` (should not exist)

5. **Configuration File Checks**
   - Verifies `STATIC_ROOT` is defined in `locallibrary/settings.py`
   - Checks that redirects don't use `permanent=True` in `locallibrary/urls.py`

6. **Automatic Patching**
   - Automatically patches `manage.py` files in:
     - `~/django_projects/mysite/manage.py`
     - `~/django_projects/locallibrary/manage.py`

## Example Output

### Successful Checkup

```
Running in a virtual environment: /home/username/.ve52
Success: Python version 3.13.5 is within the required range (3.10.0 to 3.13.9).
Django version 5.2.7 is within the range (5.2 to 5.9).
Checkup complete
```

### Checkup with Warnings

```
Running in a virtual environment: /home/username/.ve52
Success: Python version 3.13.5 is within the required range (3.10.0 to 3.13.9).
Django version 5.2.7 is within the range (5.2 to 5.9).

******  ERROR:
The folder /home/username/mysite should not exist - we use
/home/username/django_projects/mysite instead - you should remove
/home/username/mysite to avoid confusion
******

Please address the warning errors and re-run the script
```

### Fatal Errors

```
******  ERROR:
You are not running in a virtual environment, please consult the DJ4E
install instructions.  Perhaps you need to run "source ~/.ve52/bin/activate"
******

Checkup cannot continue...
```

## Common Issues and Solutions

### "You are not running in a virtual environment"

**Solution**: Activate your virtual environment:
```bash
source ~/.ve52/bin/activate
```

Then run the checkup script again.

### "You are running in an out-of-date Django 4.2 virtual environment"

**Solution**: You need to switch to the Django 5.2 virtual environment:
```bash
deactivate  # Exit current environment
source ~/.ve52/bin/activate  # Activate Django 5.2 environment
```

### "Python version is outside the required range"

**Solution**: 
- Make sure you're using Python 3.10 - 3.13
- Verify your virtual environment was created with a compatible Python version
- Recreate your virtual environment if needed:
  ```bash
  python3.13 -m venv ~/.ve52
  source ~/.ve52/bin/activate
  pip install --upgrade pip
  pip install django==5.2
  ```

### "Django version is NOT within the required range"

**Solution**: Install the correct Django version:
```bash
pip install django==5.2
```

Or if you need to upgrade:
```bash
pip install --upgrade django
```

### Folder Structure Warnings

If you see warnings about folders that shouldn't exist:

**Solution**: Remove the old folders:
```bash
rm -rf ~/djangotutorial
rm -rf ~/mysite
rm -rf ~/polls
rm -rf ~/locallibrary
# etc.
```

Make sure your projects are in the correct locations:
- `~/django_projects/mysite/`
- `~/django_projects/locallibrary/`

### "STATIC_ROOT is not defined"

**Solution**: Add `STATIC_ROOT` to your `locallibrary/settings.py`:
```python
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

### "permanent=True in redirect entry"

**Solution**: Remove `permanent=True` from redirects in `locallibrary/urls.py`. Change:
```python
RedirectView.as_view(url='/catalog/', permanent=True)
```

To:
```python
RedirectView.as_view(url='/catalog/')
```

After fixing, you may need to clear your browser cache.

## Version Requirements

The script enforces the following version requirements:

- **Python**: 3.10.0 to 3.13.9
- **Django**: 5.2 to 5.9

These ranges are designed to ensure compatibility with the DJ4E course materials and Django 5.2 features.

## Automatic Patching

The script automatically patches `manage.py` files if:
- The `manage.py` file exists
- The `patch_manage.py` script is available in `~/dj4e-samples/tools/`

This patching ensures your `manage.py` files are compatible with the current Django version and course requirements.

## Best Practices

1. **Run checkup regularly**: Run the script whenever you:
   - Set up a new development environment
   - Switch between projects
   - Encounter unexpected errors
   - Before starting new work

2. **Fix warnings promptly**: Address any warnings the script reports to avoid confusion and potential issues later.

3. **Keep folder structure clean**: Follow the recommended folder structure to avoid conflicts and confusion.

4. **Use the correct virtual environment**: Always activate `.ve52` before working on Django 5.2 projects.

## Exit Codes

- **0**: Checkup completed (may have warnings)
- **1**: Fatal error occurred (virtual environment issue)

## Related Tools

- `rollback.sh` - Roll back git repository to tags or latest commit
- `resetdb.py` - Reset Django database and migrations
- See `README_GIT.md` for git rollback documentation
- See `README_DB.md` for database reset documentation

## Notes

- The script checks your home directory (`$HOME`) for folder structure issues
- Some checks are specific to the DJ4E course structure
- The script will continue checking even if it finds warnings, but will exit on fatal errors
- All warnings should be addressed before proceeding with development work

