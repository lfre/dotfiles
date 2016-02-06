#!/bin/bash
MYCURRENTGITBRANCH=$(git rev-parse --abbrev-ref HEAD)
git checkout develop && \
git pull && \
git checkout $MYCURRENTGITBRANCH && \
git rebase -p develop
