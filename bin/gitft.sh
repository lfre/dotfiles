#!/bin/bash
git fetch $(git rev-parse --symbolic-full-name --abbrev-ref @{upstream} | sed 's!/! !')