import * as fs from "fs";
import * as path from "path";
import { fileURLToPath } from "url";

const filePath = fileURLToPath(import.meta.url);
const inputPath = path.join(path.dirname(filePath), "input.txt");

interface Claim {
  id: number;
  left: number;
  top: number;
  width: number;
  height: number;
}

function parseClaim(line: string): Claim {
  const match = line.match(/#(\d+) @ (\d+),(\d+): (\d+)x(\d+)/);

  return {
    id: parseInt(match![1]),
    left: parseInt(match![2]),
    top: parseInt(match![3]),
    width: parseInt(match![4]),
    height: parseInt(match![5]),
  };
}

function p1(text: string): number {
  const claims = text.split(/\r?\n/).filter(Boolean).map(parseClaim);
  const grid = new Map<string, number>();

  for (const claim of claims) {
    for (let x = claim.left; x < claim.left + claim.width; x++) {
      for (let y = claim.top; y < claim.top + claim.height; y++) {
        const key = `${x},${y}`;

        grid.set(key, (grid.get(key) ?? 0) + 1);
      }
    }
  }

  return Array.from(grid.values()).filter((v) => v > 1).length;
}

function p2(text: string): number {
  const claims = text.split(/\r?\n/).filter(Boolean).map(parseClaim);
  const grid = new Map<string, number>();

  for (const claim of claims) {
    for (let x = claim.left; x < claim.left + claim.width; x++) {
      for (let y = claim.top; y < claim.top + claim.height; y++) {
        const key = `${x},${y}`;
        grid.set(key, (grid.get(key) ?? 0) + 1);
      }
    }
  }

  for (const claim of claims) {
    let valid = true;
    for (let x = claim.left; x < claim.left + claim.width; x++) {
      for (let y = claim.top; y < claim.top + claim.height; y++) {
        if (grid.get(`${x},${y}`) !== 1) {
          valid = false;
          break;
        }
      }
      if (!valid) break;
    }

    if (valid) return claim.id;
  }

  return -1;
}

const text = fs.readFileSync(inputPath, "utf-8").trim();
console.log(p1(text));
console.log(p2(text));
