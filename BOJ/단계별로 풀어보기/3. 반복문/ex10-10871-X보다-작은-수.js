const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [N, X] = input[0].split(" ").map((x) => Number(x));

const numbers = input[1].split(" ").map((x) => Number(x));

let res = "";
for (let i = 0; i < N; i++) {
  if (numbers[i] < X) res += String(numbers[i]) + " ";
}

console.log(res.trim());
