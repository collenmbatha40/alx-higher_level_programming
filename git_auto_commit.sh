#!/bin/bash

# Check if a commit message is provided as an argument, otherwise use a default message
commit_message="${1:-"Automatic commit"}"

# Function to check if the repository is a Git repository
function is_git_repository() {
  git rev-parse --is-inside-work-tree >/dev/null 2>&1
}

# Function to execute git commands and handle errors
function git_command() {
  git "$@"
  local status=$?
  if [ $status -ne 0 ]; then
    echo "Error: Git command failed: git $*" >&2
    exit $status
  fi
}

# Check if the current directory is a Git repository
if ! is_git_repository; then
  echo "Error: Not a Git repository. Please initialize a Git repository first."
  exit 1
fi

# Execute the git add, commit, and push commands
git_command add .
git_command commit -m "$commit_message"
git_command push origin HEAD

echo "Git add, commit, and push process completed successfully."

