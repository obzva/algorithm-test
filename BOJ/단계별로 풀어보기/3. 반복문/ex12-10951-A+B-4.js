const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

const N = input.length;

let res = "";
for (let i = 0; i < N; i++) {
  const [a, b] = input[i].split(" ").map((x) => Number(x));
  res += String(a + b) + "\n";
}

console.log(res.trim());
