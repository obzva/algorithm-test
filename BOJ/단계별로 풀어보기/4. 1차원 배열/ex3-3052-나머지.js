const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

const numbers = input.map((x) => Number(x));

const tmp = [];

for (let i = 0; i < 10; i++) {
  const remainder = numbers[i] % 42;
  if (tmp.indexOf(remainder) < 0) tmp.push(remainder);
}

console.log(tmp.length);
