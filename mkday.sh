#!/usr/bin/env bash

set -euxo pipefail

N=$1
TARGET="day${N}.py"

sed "s/{{N}}/$N/g" < day.in > "$TARGET"
chmod +x "$TARGET"
touch "inp_$N"
