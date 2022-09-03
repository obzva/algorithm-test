const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);

let res = "";

for (let i = 1; i <= N; i++) {
  const [a, b] = input[i].split(" ").map((x) => Number(x));
  res +=
    "Case #" +
    String(i) +
    ": " +
    String(a) +
    " + " +
    String(b) +
    " = " +
    String(a + b) +
    "\n";
}

console.log(res.trim());
