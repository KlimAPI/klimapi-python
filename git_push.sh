#!/bin/sh

git_user_id=$1
git_repo_id=$2
release_note=$3

if [ "$git_user_id" = "" ]; then
git_user_id="KlimAPI"
echo "[INFO] No command line input provided. Set \$git_user_id to $git_user_id"
fi

if [ "$git_repo_id" = "" ]; then
git_repo_id="klimapi-python"
echo "[INFO] No command line input provided. Set \$git_repo_id to $git_repo_id"
fi

if [ "$release_note" = "" ]; then
release_note="1.1.29"
echo "[INFO] No command line input provided. Set \$release_note to $release_note"
fi

# Adds the files in the local repository and stages them for commit.
git add .

# Commits the tracked changes and prepares them to be pushed to a remote repository.
git commit -m "$release_note"

git push -f -u origin main
