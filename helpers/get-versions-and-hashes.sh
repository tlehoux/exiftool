#!/usr/bin/env bash

[[ "${OSTYPE}" =~ ^linux ]] || { echo "We need linux for gnu-stat." ; exit 1 ; }

set -e
for X in 12.{00..99} ; do
  grep -q "\s\+$X:" "${0%/*}/../vars/main.yml" && continue
  file="Image-ExifTool-$X.tar.gz"
  wget -q https://exiftool.org/$file
  echo "$X: $(sha1sum "$file" | awk '{print $1}')  # $(stat -c "%y" "$file" | awk '{print $1}')"
done
