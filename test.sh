#!/usr/bin/env bash

set -x

while read p; do
    echo "$p" | nc -q 1 localhost 5555
done < test.mod
