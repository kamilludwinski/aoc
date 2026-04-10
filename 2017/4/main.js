// https://adventofcode.com/2017/day/4
const fs = require("fs");
const path = require("path");

const inputPath = path.join(__dirname, "input.txt");

function p1(text) {
  return text
    .trim()
    .split("\n")
    .filter((line) => {
      const words = line.split(/\s+/);
      return new Set(words).size === words.length;
    }).length;
}

function p2(text) {
  return text
    .trim()
    .split("\n")
    .filter((line) => {
      const words = line.split(/\s+/).map((w) => w.split("").sort().join(""));
      return new Set(words).size === words.length;
    }).length;
}

const text = fs.readFileSync(inputPath, "utf-8");
console.log(p1(text));
console.log(p2(text));
