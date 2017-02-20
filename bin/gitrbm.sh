#!/bin/bash
MYCURRENTGITBRANCH=$(git rev-parse --abbrev-ref HEAD)
git checkout master && \
git pull && \
git checkout $MYCURRENTGITBRANCH && \
git rebase master
