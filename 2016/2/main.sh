#!/usr/bin/env bash
# https://adventofcode.com/2016/day/2
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INPUT="$DIR/input.txt"
[[ -f "$INPUT" ]] || { echo "input.txt not found" >&2; exit 1; }

# Part 1: 3x3 keypad, 5 center
# Part 2: diamond keypad

p1() {
  local r=1 c=1 code=""
  local line ch
  while IFS= read -r line || [[ -n "$line" ]]; do
    [[ -z "$line" ]] && continue
    for ((i = 0; i < ${#line}; i++)); do
      ch="${line:i:1}"
      case "$ch" in
        U) ((r > 0)) && r=$((r - 1)) ;;
        D) ((r < 2)) && r=$((r + 1)) ;;
        L) ((c > 0)) && c=$((c - 1)) ;;
        R) ((c < 2)) && c=$((c + 1)) ;;
      esac
    done
    local -a row0=(1 2 3)
    local -a row1=(4 5 6)
    local -a row2=(7 8 9)
    case $r in
      0) code+="${row0[c]}" ;;
      1) code+="${row1[c]}" ;;
      2) code+="${row2[c]}" ;;
    esac
  done <"$INPUT"
  echo "$code"
}

p2() {
  # Positions as (r,c) on 5-row grid; valid cells hold hex digit
  local -A kp=(
    [0,2]=1 [1,1]=2 [1,2]=3 [1,3]=4
    [2,0]=5 [2,1]=6 [2,2]=7 [2,3]=8 [2,4]=9
    [3,1]=A [3,2]=B [3,3]=C
    [4,2]=D
  )
  local r=2 c=0 code=""
  local line ch nr nc
  while IFS= read -r line || [[ -n "$line" ]]; do
    [[ -z "$line" ]] && continue
    for ((i = 0; i < ${#line}; i++)); do
      ch="${line:i:1}"
      nr=$r nc=$c
      case "$ch" in
        U) nr=$((r - 1)) ;;
        D) nr=$((r + 1)) ;;
        L) nc=$((c - 1)) ;;
        R) nc=$((c + 1)) ;;
      esac
      local key="$nr,$nc"
      [[ -n "${kp[$key]:-}" ]] && r=$nr && c=$nc
    done
    code+="${kp[$r,$c]}"
  done <"$INPUT"
  echo "$code"
}

p1
p2
