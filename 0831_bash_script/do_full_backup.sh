#!/bin/bash
cd backups
tar -cvpf "$(date '+%Y-%m-%d_%H-%M-%S').tar" /home/zaemoore/Computational/src
find . -mindepth 1 -maxdepth 1 -type f -iname '*.tar' -printf "%C+ %p\n" | sort -n | cut -d ' ' -f 2- | head -n -3 | xargs -I{} rm "{}"