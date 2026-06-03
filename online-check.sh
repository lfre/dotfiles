#!/bin/zsh

# Saved in ~/online-check.sh and in a cron job as:
# * * * * * ~/online-check.sh

if dig @8.8.8.8 +time=1 +tries=1 +short google.com A 2>/dev/null | grep -q .; then
  rm -f "$HOME/.offline"
else
  touch "$HOME/.offline"
fi
