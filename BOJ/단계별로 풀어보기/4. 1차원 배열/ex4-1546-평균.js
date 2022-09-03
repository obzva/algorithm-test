const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);

const numbers = input[1].split(" ").map((x) => Number(x));

const maxNumber = Math.max(...numbers);

const sum = numbers.reduce((prev, curr) => prev + curr, 0);

console.log((sum / N / maxNumber) * 100);
