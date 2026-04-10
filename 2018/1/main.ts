// https://adventofcode.com/2018/day/1
import * as fs from "fs";
import * as path from "path";
import { fileURLToPath } from "url";

const filePath = fileURLToPath(import.meta.url);
const inputPath = path.join(path.dirname(filePath), "input.txt");
if (!fs.existsSync(inputPath)) {
  throw new Error("input.txt not found");
}

function p1(text: string): number {
  return text
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter(Boolean)
    .map(Number)
    .reduce((a, b) => a + b, 0);
}

function p2(text: string): number {
  const changes = text
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter(Boolean)
    .map(Number);

  const seen = new Set<number>();
  let freq = 0;
  let i = 0;

  while (true) {
    if (seen.has(freq)) return freq;
    seen.add(freq);

    freq += changes[i % changes.length];

    i++;
  }
}

const text = fs.readFileSync(inputPath, "utf-8").trim();
console.log(p1(text));
console.log(p2(text));
