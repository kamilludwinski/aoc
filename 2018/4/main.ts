import * as fs from "fs";
import * as path from "path";
import { fileURLToPath } from "url";

const filePath = fileURLToPath(import.meta.url);
const inputPath = path.join(path.dirname(filePath), "input.txt");

function p1(text: string): number {
  const lines = text.split(/\r?\n/).filter(Boolean).sort();
  const guardSleep = new Map<number, number[]>();
  let currentGuard = 0;
  let sleepStart = 0;
  for (const line of lines) {
    if (line.includes("Guard")) {
      const match = line.match(/Guard #(\d+)/);
      currentGuard = parseInt(match![1]);
      if (!guardSleep.has(currentGuard)) {
        guardSleep.set(currentGuard, new Array(60).fill(0));
      }
    } else if (line.includes("falls asleep")) {
      const match = line.match(/:(\d+)\]/);
      sleepStart = parseInt(match![1]);
    } else if (line.includes("wakes up")) {
      const match = line.match(/:(\d+)\]/);
      const sleepEnd = parseInt(match![1]);
      const sleep = guardSleep.get(currentGuard)!;
      for (let i = sleepStart; i < sleepEnd; i++) {
        sleep[i]++;
      }
    }
  }
  let maxGuard = 0,
    maxSleep = 0;
  for (const [guard, sleep] of guardSleep) {
    const total = sleep.reduce((a, b) => a + b, 0);
    if (total > maxSleep) {
      maxSleep = total;
      maxGuard = guard;
    }
  }
  const sleep = guardSleep.get(maxGuard)!;
  const minute = sleep.indexOf(Math.max(...sleep));
  return maxGuard * minute;
}

function p2(text: string): number {
  const lines = text.split(/\r?\n/).filter(Boolean).sort();
  const guardSleep = new Map<number, number[]>();
  let currentGuard = 0;
  let sleepStart = 0;
  for (const line of lines) {
    if (line.includes("Guard")) {
      const match = line.match(/Guard #(\d+)/);
      currentGuard = parseInt(match![1]);
      if (!guardSleep.has(currentGuard)) {
        guardSleep.set(currentGuard, new Array(60).fill(0));
      }
    } else if (line.includes("falls asleep")) {
      const match = line.match(/:(\d+)\]/);
      sleepStart = parseInt(match![1]);
    } else if (line.includes("wakes up")) {
      const match = line.match(/:(\d+)\]/);
      const sleepEnd = parseInt(match![1]);
      const sleep = guardSleep.get(currentGuard)!;
      for (let i = sleepStart; i < sleepEnd; i++) {
        sleep[i]++;
      }
    }
  }
  let maxGuard = 0,
    maxMinute = 0,
    maxCount = 0;
  for (const [guard, sleep] of guardSleep) {
    for (let i = 0; i < 60; i++) {
      if (sleep[i] > maxCount) {
        maxCount = sleep[i];
        maxGuard = guard;
        maxMinute = i;
      }
    }
  }
  return maxGuard * maxMinute;
}

const text = fs.readFileSync(inputPath, "utf-8").trim();
console.log(p1(text));
console.log(p2(text));
