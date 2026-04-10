// https://adventofcode.com/2017/day/1

const fs = require("fs");
const path = require("path");

const inputPath = path.join(__dirname, "input.txt");
if (!fs.existsSync(inputPath)) {
  throw new Error("input.txt not found");
}

function p1(text) {
  let sum = 0;

  for (let i = 0; i < text.length; i++) {
    const next = text[(i + 1) % text.length];

    if (text[i] === next) {
      sum += Number(text[i]);
    }
  }

  return sum;
}

function p2(text) {
  let sum = 0;

  const half = text.length / 2;

  for (let i = 0; i < text.length; i++) {
    const match = text[(i + half) % text.length];

    if (text[i] === match) {
      sum += Number(text[i]);
    }
  }

  return sum;
}

const text = fs.readFileSync(inputPath, "utf-8").trim();
console.log(p1(text));
console.log(p2(text));
