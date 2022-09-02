const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map((x) => Number(x));

const tmp = Array.from({ length: 6 }, () => 0);

for (const x of input) tmp[x - 1]++;

const case1 = tmp.indexOf(3) >= 0;
const case2 = tmp.indexOf(2) >= 0;

if (case1) console.log(10000 + (tmp.indexOf(3) + 1) * 1000);
else if (case2) console.log(1000 + (tmp.indexOf(2) + 1) * 100);
else console.log(Math.max(...input) * 100);
