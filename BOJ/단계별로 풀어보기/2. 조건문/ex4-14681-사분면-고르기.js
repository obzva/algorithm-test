const input = require("fs")
  .readFileSync(0)
  .toString()
  .trim()
  .split("\n")
  .map((x) => Number(x));

const [x, y] = input.map((x) => Number(x));

if (x * y > 0) {
  if (x > 0) console.log(1);
  else console.log(3);
} else {
  if (x > 0) console.log(4);
  else console.log(2);
}
