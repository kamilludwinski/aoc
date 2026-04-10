import * as fs from "fs";
import * as path from "path";
import { fileURLToPath } from "url";

const filePath = fileURLToPath(import.meta.url);
const inputPath = path.join(path.dirname(filePath), "input.txt");

function p1(text: string): number {
  const lines = text.split(/\r?\n/).filter(Boolean);
  let twos = 0,
    threes = 0;

  for (const line of lines) {
    const freq = new Map<string, number>();
    for (const char of line) {
      freq.set(char, (freq.get(char) ?? 0) + 1);
    }

    if (Array.from(freq.values()).includes(2)) twos++;
    if (Array.from(freq.values()).includes(3)) threes++;
  }

  return twos * threes;
}

function p2(text: string): string {
  const lines = text.split(/\r?\n/).filter(Boolean);

  for (let i = 0; i < lines.length; i++) {
    for (let j = i + 1; j < lines.length; j++) {
      let diff = 0,
        pos = -1;
      for (let k = 0; k < lines[i].length; k++) {
        if (lines[i][k] !== lines[j][k]) {
          diff++;
          pos = k;
        }
      }

      if (diff === 1) {
        return lines[i].slice(0, pos) + lines[i].slice(pos + 1);
      }
    }
  }

  return "";
}

const text = fs.readFileSync(inputPath, "utf-8").trim();
console.log(p1(text));
console.log(p2(text));
