#!/bin/bash
set -e

# Ensure we're on the right branch
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo "Current branch: $CURRENT_BRANCH"

if [ "$CURRENT_BRANCH" != "dev_page" ]; then
  echo "⚠️  Warning: you are not on 'dev_page' (currently on '$CURRENT_BRANCH')"
fi

# Start Jekyll with live reload, drafts, and future posts visible
bundle exec jekyll serve \
  --livereload \
  --drafts \
  --future \
  --host 0.0.0.0 \
  --port 4000 \
  --baseurl ""
