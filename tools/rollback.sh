#!/bin/bash

# Git Rollback Script
# This script allows you to roll back to any git tag or to the latest commit
# on the currently checked out branch, discarding all local changes and untracked files.

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_error() {
    echo -e "${RED}$1${NC}"
}

print_success() {
    echo -e "${GREEN}$1${NC}"
}

print_warning() {
    echo -e "${YELLOW}$1${NC}"
}

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    print_error "Error: Not a git repository!"
    exit 1
fi

# Get the current branch name
CURRENT_BRANCH=$(git branch --show-current 2>/dev/null || git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "unknown")

# Get the current directory name for display
CURRENT_DIR=$(basename "$(pwd)")
echo "Git Rollback Script"
echo "Current directory: $CURRENT_DIR"
echo "Current branch: $CURRENT_BRANCH"
echo ""

# Check for uncommitted changes
if ! git diff-index --quiet HEAD -- 2>/dev/null || [ -n "$(git ls-files --others --exclude-standard)" ]; then
    print_warning "Warning: You have uncommitted changes or untracked files!"
    echo ""
    git status --short
    echo ""
    read -p "Do you want to continue? This will DISCARD ALL local changes and untracked files! (yes/no): " confirm
    if [ "$confirm" != "yes" ]; then
        echo "Rollback cancelled."
        exit 0
    fi
fi

# Fetch latest tags from remote (optional, but helpful)
echo "Fetching latest tags from remote..."
git fetch --tags 2>/dev/null || print_warning "Could not fetch tags from remote (continuing with local tags)"

# List all tags with dates
echo ""
echo "Available tags:"
echo "==============="
tags=($(git tag --sort=-creatordate))
if [ ${#tags[@]} -eq 0 ]; then
    print_warning "No tags found in this repository."
    echo ""
    read -p "Do you want to roll back to the latest commit on '$CURRENT_BRANCH'? (yes/no): " rollback_branch
    if [ "$rollback_branch" = "yes" ]; then
        echo ""
        print_warning "Rolling back to latest commit on '$CURRENT_BRANCH' (discarding all local changes)..."
        # Try to reset to remote branch first, then fall back to local HEAD
        git fetch origin "$CURRENT_BRANCH" 2>/dev/null || true
        git reset --hard "origin/$CURRENT_BRANCH" 2>/dev/null || git reset --hard HEAD
        git clean -fd
        print_success "Successfully rolled back to latest commit on '$CURRENT_BRANCH'"
        exit 0
    else
        echo "Rollback cancelled."
        exit 0
    fi
fi

# Display tags with dates
declare -a tag_array
index=1
for tag in "${tags[@]}"; do
    # Get tag date
    tag_date=$(git log -1 --format=%ai "$tag" 2>/dev/null || echo "Unknown date")
    printf "%2d. %-30s %s\n" "$index" "$tag" "$tag_date"
    tag_array+=("$tag")
    ((index++))
done

echo ""
echo "Options:"
echo "  [0] Roll back to latest commit on '$CURRENT_BRANCH' (discard local changes)"
echo "  [1-${#tags[@]}] Roll back to a specific tag"
echo "  [q] Quit"
echo ""

# Get user selection
read -p "Enter your choice: " choice

# Handle quit
if [ "$choice" = "q" ] || [ "$choice" = "Q" ]; then
    echo "Rollback cancelled."
    exit 0
fi

# Handle rollback to latest commit on current branch
if [ "$choice" = "0" ]; then
    echo ""
    print_warning "Rolling back to latest commit on '$CURRENT_BRANCH' (discarding all local changes)..."
    # Fetch latest from remote for current branch
    git fetch origin "$CURRENT_BRANCH" 2>/dev/null || true
    # Try to reset to remote branch first, then fall back to local HEAD
    git reset --hard "origin/$CURRENT_BRANCH" 2>/dev/null || git reset --hard HEAD
    git clean -fd
    print_success "Successfully rolled back to latest commit on '$CURRENT_BRANCH'"
    echo ""
    echo "Current HEAD:"
    git log -1 --oneline
    exit 0
fi

# Handle tag selection
if [[ "$choice" =~ ^[0-9]+$ ]] && [ "$choice" -ge 1 ] && [ "$choice" -le "${#tags[@]}" ]; then
    selected_tag="${tag_array[$((choice-1))]}"
    echo ""
    print_warning "Rolling back to tag: $selected_tag"
    print_warning "This will discard all local changes and untracked files!"
    read -p "Are you sure? (yes/no): " final_confirm
    if [ "$final_confirm" = "yes" ]; then
        # Discard local changes
        git reset --hard "$selected_tag"
        # Remove untracked files and directories
        git clean -fd
        print_success "Successfully rolled back to tag: $selected_tag"
        echo ""
        echo "Current HEAD:"
        git log -1 --oneline
    else
        echo "Rollback cancelled."
        exit 0
    fi
else
    print_error "Invalid choice. Please run the script again."
    exit 1
fi

