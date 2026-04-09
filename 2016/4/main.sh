#!/usr/bin/env bash
# https://adventofcode.com/2016/day/4
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INPUT="$DIR/input.txt"
[[ -f "$INPUT" ]] || { echo "input.txt not found" >&2; exit 1; }

checksum_ok() {
  local name="$1" want="$2"
  local got
  got="$(printf '%s' "$name" | tr -d '-' | grep -o . | LC_ALL=C grep -E '^[a-z]$' |
    LC_ALL=C sort | uniq -c | LC_ALL=C sort -k1,1nr -k2,2 | head -5 | awk '{printf "%s", $2}')"
  [[ "$got" == "$want" ]]
}

decrypt_name() {
  local name="$1" sid=$2 first=1 word i ch oc out="" rw
  IFS='-' read -ra parts <<<"$name"
  for word in "${parts[@]}"; do
    rw=""
    for ((i = 0; i < ${#word}; i++)); do
      ch="${word:i:1}"
      oc=$(( ( $(printf '%d' "'$ch") - 97 + sid) % 26 + 97 ))
      rw+=$(printf '%b' "\\$(printf '%03o' "$oc")")
    done
    [[ $first -eq 1 ]] && out="$rw" || out+=" $rw"
    first=0
  done
  echo "$out"
}

p1() {
  local sum=0 line name sector chk
  while IFS= read -r line || [[ -n "$line" ]]; do
    line="${line%$'\r'}"
    [[ -z "$line" ]] && continue
    [[ "$line" =~ ^(.+)-([0-9]+)\[([a-z]+)\]$ ]] || continue
    name="${BASH_REMATCH[1]}"
    sector="${BASH_REMATCH[2]}"
    chk="${BASH_REMATCH[3]}"
    checksum_ok "$name" "$chk" && sum=$((sum + sector))
  done <"$INPUT"
  echo "$sum"
}

p2() {
  local line name sector chk dec
  while IFS= read -r line || [[ -n "$line" ]]; do
    line="${line%$'\r'}"
    [[ -z "$line" ]] && continue
    [[ "$line" =~ ^(.+)-([0-9]+)\[([a-z]+)\]$ ]] || continue
    name="${BASH_REMATCH[1]}"
    sector="${BASH_REMATCH[2]}"
    chk="${BASH_REMATCH[3]}"
    checksum_ok "$name" "$chk" || continue
    dec="$(decrypt_name "$name" "$sector")"
    [[ "$dec" == *"northpole object storage"* ]] && echo "$sector" && return
  done <"$INPUT"
  echo 0
}

p1
p2
