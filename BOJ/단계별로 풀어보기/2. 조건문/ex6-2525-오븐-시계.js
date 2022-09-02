const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [A, B] = input[0].split(" ");
const C = input[1];

const [startH, startM] = [Number(A), Number(B)];
const [durationH, durationM] = [Math.floor(Number(C) / 60), Number(C) % 60];
let [endH, endM] = [startH + durationH, startM + durationM];

if (endM >= 60) {
  endH++;
  endM -= 60;
}

if (endH >= 24) endH -= 24;

console.log(endH, endM);
