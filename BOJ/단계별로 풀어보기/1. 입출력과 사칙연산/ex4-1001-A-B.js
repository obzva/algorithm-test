const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .split(" ")
  .map((x) => Number(x));

const [num1, num2] = input;

console.log(num1 - num2);
