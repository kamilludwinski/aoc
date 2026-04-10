// https://adventofcode.com/2017/day/3

const fs = require("fs");
const path = require("path");

const inputPath = path.join(__dirname, "input.txt");

function p1(text) {
  const n = parseInt(text.trim());
  let layer = 0;

  while ((2 * layer + 1) ** 2 < n) layer++;
  const sideLength = 2 * layer;
  const maxNum = (2 * layer + 1) ** 2;
  const midpoints = [0, 1, 2, 3].map((i) => maxNum - layer - sideLength * i);
  const steps = layer + Math.min(...midpoints.map((midpoint) => Math.abs(n - midpoint)));

  return steps;
}

function p2(text) {
  const n = parseInt(text.trim());
  const grid = { "0,0": 1 };

  let x = 0,
    y = 0,
    dx = 1,
    dy = 0,
    step = 1,
    turn = 0,
    len = 1;

  while (true) {
    for (let i = 0; i < 2; i++) {
      for (let j = 0; j < len; j++) {
        x += dx;
        y += dy;
        let sum = 0;

        for (let xx = -1; xx <= 1; xx++) {
          for (let yy = -1; yy <= 1; yy++) {
            sum += grid[`${x + xx},${y + yy}`] || 0;
          }
        }

        grid[`${x},${y}`] = sum;
        if (sum > n) return sum;
      }

      [dx, dy] = [-dy, dx];
    }

    len++;
  }
}

const text = fs.readFileSync(inputPath, "utf-8");
console.log(p1(text));
console.log(p2(text));
