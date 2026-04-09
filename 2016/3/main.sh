#!/usr/bin/env bash
# https://adventofcode.com/2016/day/3
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INPUT="$DIR/input.txt"
[[ -f "$INPUT" ]] || { echo "input.txt not found" >&2; exit 1; }

# Strip CR so Windows (CRLF) inputs don't break arithmetic and comparisons.
stripped_input() {
  tr -d '\r' <"$INPUT"
}

# Plain `while read ...; do` drops the last line if the file has no final newline.

valid_triangle() {
  local a=$1 b=$2 c=$3
  ((a + b > c && a + c > b && b + c > a))
}

p1() {
  local count=0 a b c line
  while IFS= read -r line || [[ -n "$line" ]]; do
    read -r a b c <<<"$line"
    [[ -z "${a:-}" ]] && continue
    valid_triangle "$a" "$b" "$c" && ((count += 1)) || true
  done < <(stripped_input)
  echo "$count"
}

p2() {
  local -a buf=()
  local a b c line
  while IFS= read -r line || [[ -n "$line" ]]; do
    read -r a b c <<<"$line"
    [[ -z "${a:-}" ]] && continue
    buf+=("$a" "$b" "$c")
  done < <(stripped_input)
  local n=${#buf[@]} i count=0
  for ((i = 0; i + 8 < n; i += 9)); do
    valid_triangle "${buf[$((i))]}" "${buf[$((i + 3))]}" "${buf[$((i + 6))]}" &&
      ((count += 1)) || true
    valid_triangle "${buf[$((i + 1))]}" "${buf[$((i + 4))]}" "${buf[$((i + 7))]}" &&
      ((count += 1)) || true
    valid_triangle "${buf[$((i + 2))]}" "${buf[$((i + 5))]}" "${buf[$((i + 8))]}" &&
      ((count += 1)) || true
  done
  echo "$count"
}

p1
p2
