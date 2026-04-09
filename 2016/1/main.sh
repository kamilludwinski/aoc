#!/usr/bin/env bash
# https://adventofcode.com/2016/day/1

set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INPUT="$DIR/input.txt"
[[ -f "$INPUT" ]] || { echo "input.txt not found" >&2; exit 1; }

text="$(tr -d '\n' <"$INPUT" | sed 's/,$//')"

p1() {
  local x=0 y=0 d=0 turn dist ch
  local -a parts
  
  IFS=', ' read -ra parts <<<"$text"
  for w in "${parts[@]}"; do
    [[ -z "$w" ]] && continue
    turn="${w:0:1}"
    dist="${w:1}"
    [[ "$turn" == "R" ]] && d=$(( (d + 1) % 4 )) || d=$(( (d + 3) % 4 ))
    case $d in
      0) y=$((y + dist)) ;;
      1) x=$((x + dist)) ;;
      2) y=$((y - dist)) ;;
      3) x=$((x - dist)) ;;
    esac
  done
  echo $(( ${x#-} + ${y#-} ))
}

p2() {
  local x=0 y=0 d=0 turn dist
  local -A seen=()
  local -a parts
  IFS=', ' read -ra parts <<<"$text"
  seen["0,0"]=1
  for w in "${parts[@]}"; do
    [[ -z "$w" ]] && continue
    turn="${w:0:1}"
    dist="${w:1}"
    [[ "$turn" == "R" ]] && d=$(( (d + 1) % 4 )) || d=$(( (d + 3) % 4 ))
    for ((i = 0; i < dist; i++)); do
      case $d in
        0) y=$((y + 1)) ;;
        1) x=$((x + 1)) ;;
        2) y=$((y - 1)) ;;
        3) x=$((x - 1)) ;;
      esac
      local k="$x,$y"
      [[ -n "${seen[$k]:-}" ]] && echo $(( ${x#-} + ${y#-} )) && return
      seen[$k]=1
    done
  done
  echo 0
}

p1
p2
