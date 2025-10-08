# /bin/bash

warn () {
    echo
    echo '******  ERROR:'
    echo $1 | fold -s -w 80
    echo '******'
    echo
    HAVE_WARNING="true"
}

die () {
    warn "$1"
    echo 
    echo 'Checkup cannot continue...'
    exit
}

if [ -n "$VIRTUAL_ENV" ]; then
    : echo "Running in a virtual environment: $VIRTUAL_ENV"
else
    die 'You are not running in a virtual environment, please consult the DJ4E install instructions.  Perhaps you need to run "source ~/.ve52/bin/activate"'
fi

if [[ "$VIRTUAL_ENV" =~ "ve52" ]]; then
  : echo "Running in .ve52"
elif [[ "$VIRTUAL_ENV" =~ "django42" ]]; then
  die "You are running in an out-of-date Django 4.2 virtual environment - you should be running the ve52 virtual environment - see DJ4E install instructions"
else
  die "Not running in virtual environment ve52 - please consult the DJ4E install instructions."
fi

# Define the version range and the python command
MIN_VERSION="3.10.0"
MAX_VERSION="3.13.9"
PYTHON_CMD="python"

# Get the current Python version
# Use 2>&1 to capture output sent to stderr
CURRENT_VERSION=$(${PYTHON_CMD} --version 2>&1 | cut -d ' ' -f 2)

# Check if the python command exists
if ! command -v ${PYTHON_CMD} &> /dev/null; then
    die "Error: ${PYTHON_CMD} not found."
fi

# Compare the versions
if [ "$(printf '%s\n' "$MIN_VERSION" "$CURRENT_VERSION" "$MAX_VERSION" | sort -V | head -n2 | tail -n1)" = "$CURRENT_VERSION" ]; then
    : echo "Success: Python version ${CURRENT_VERSION} is within the required range ($MIN_VERSION to $MAX_VERSION)."
else
    warn "Failure: Python version ${CURRENT_VERSION} is outside the required range ($MIN_VERSION to $MAX_VERSION)."
fi

# Define the desired version range
DJANGO_MIN_MAJOR=5
DJANGO_MIN_MINOR=2
MAX_MAJOR=5
MAX_MINOR=9

# Get the Django version
DJANGO_VERSION=$(python -m django --version)

# Extract major, minor, and patch numbers
# Using awk to split the version string by '.'
DJANGO_MAJOR=$(echo "$DJANGO_VERSION" | awk -F'.' '{print $1}')
DJANGO_MINOR=$(echo "$DJANGO_VERSION" | awk -F'.' '{print $2}')
# Optional: DJANGO_PATCH=$(echo "$DJANGO_VERSION" | awk -F'.' '{print $3}')

# Perform the version comparison
if (( DJANGO_MAJOR > DJANGO_MIN_MAJOR || (DJANGO_MAJOR == DJANGO_MIN_MAJOR && DJANGO_MINOR >= DJANGO_MIN_MINOR) )) && \
   (( DJANGO_MAJOR < MAX_MAJOR || (DJANGO_MAJOR == MAX_MAJOR && DJANGO_MINOR <= MAX_MINOR) )); then
    : echo "Django version $DJANGO_VERSION is within the range ($DJANGO_MIN_MAJOR.$DJANGO_MIN_MINOR to $MAX_MAJOR.$MAX_MINOR)."
else
    warn "Django version $DJANGO_VERSION is NOT within the range ($DJANGO_MIN_MAJOR.$DJANGO_MIN_MINOR to $MAX_MAJOR.$MAX_MINOR)."
fi

if [[ -e "$HOME/djangotutorial" ]]; then
    warn "The folder $HOME/djangotutorial should not exist - we use $HOME/django_projects instead - you should remove $HOME/djangotutorial to avoid confusion"
fi

if [[ -e "$HOME/mysite" ]]; then
    warn "The folder $HOME/mysite should not exist - we use $HOME/django_projects/mysite instead - you should remove $HOME/mysite to avoid confusion"
fi

if [[ -e "$HOME/polls" ]]; then
    warn "The folder $HOME/polls should not exist - we use $HOME/django_projects/mysite/polls instead - you should remove $HOME/polls to avoid confusion"
fi

if [[ -e "$HOME/locallibrary" ]]; then
    warn "The folder $HOME/locallibrary should not exist - we use $HOME/django_projects/locallibrary instead in your home directory"
fi

if [[ -e "$HOME/django_projects/mysite/locallibrary" ]]; then
    warn "The folder $HOME/django_projects/mysite/locallibrary should not exist - we use $HOME/django_projects/locallibrary instead in your home directory"
fi

if [[ -f "$HOME/django_projects/locallibrary/locallibrary/settings.py" ]]; then
    if grep -q "STATIC_ROOT" "$HOME/django_projects/locallibrary/locallibrary/settings.py"; then
        : echo STATIC_ROOT defined
    else
        warn "The $HOME/django_projects/locallibrary/locallibrary/settings.py does not have STATIC_ROOT defined - please see instructions"
    fi
fi

if [[ -f "$HOME/django_projects/locallibrary/locallibrary/urls.py" ]]; then
    if grep -q "RedirectView.as_view(url=.*permanent=True" "$HOME/django_projects/locallibrary/locallibrary/urls.py"; then
        warn "The $HOME/django_projects/locallibrary/locallibrary/urls.py should not have 'permanent=True' in the redirect entry - please see instructions.  Once you fix this, you will may need to clear your browser cache to get the redirect out of the browser cache."
    else
        : echo STATIC_ROOT defined
    fi
fi


MANAGE_FILE=$HOME/django_projects/mysite/manage.py
if [[ -f "$MANAGE_FILE" && -f "$HOME/dj4e-samples/tools/patch_manage.py" ]]; then
    python $HOME/dj4e-samples/tools/patch_manage.py $MANAGE_FILE
fi

MANAGE_FILE=$HOME/django_projects/locallibrary/manage.py
if [[ -f "$MANAGE_FILE" && -f "$HOME/dj4e-samples/tools/patch_manage.py" ]]; then
    python $HOME/dj4e-samples/tools/patch_manage.py $MANAGE_FILE
fi

if [[ "$HAVE_WARNING" == "true" ]]; then
  echo Please address the warning errors and re-run the script
else
  echo Checkup complete
fi

