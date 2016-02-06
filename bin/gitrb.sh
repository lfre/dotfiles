#!/bin/bash
git rebase -p $(git rev-parse --symbolic-full-name --abbrev-ref @{upstream} | sed 's!/! !')
