const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

const n = Number(input[0]);

for (let i = 1; i <= n; i++) {
  const [A, B] = input[i].split(" ").map((x) => Number(x));
  console.log(A + B);
}
