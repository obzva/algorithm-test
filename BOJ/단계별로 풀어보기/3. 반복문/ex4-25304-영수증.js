const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

const X = Number(input[0]);
const N = Number(input[1]);

const goods = input.slice(2);
let sum = 0;
for (let i = 0; i < N; i++) {
  const [a, b] = goods[i].split(" ").map((x) => Number(x));
  sum += a * b;
}

console.log(sum === X ? "Yes" : "No");
