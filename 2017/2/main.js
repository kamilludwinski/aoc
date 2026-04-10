// https://adventofcode.com/2017/day/2
const fs = require("fs");
const path = require("path");

const inputPath = path.join(__dirname, "input.txt");

function p1(text) {
  let sum = 0;

  text
    .trim()
    .split(/\r?\n/)
    .forEach((line) => {
      const nums = line.trim().split(/\s+/).map(Number);
      sum += Math.max(...nums) - Math.min(...nums);
    });

  return sum;
}

function p2(text) {
  let sum = 0;

  text
    .trim()
    .split(/\r?\n/)
    .forEach((line) => {
      const nums = line.trim().split(/\s+/).map(Number);

      for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
          if (nums[i] % nums[j] === 0) return (sum += nums[i] / nums[j]);
          if (nums[j] % nums[i] === 0) return (sum += nums[j] / nums[i]);
        }
      }
    });

  return sum;
}

const text = fs.readFileSync(inputPath, "utf-8");
console.log(p1(text));
console.log(p2(text));
