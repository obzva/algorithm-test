const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

const n = Number(input.shift());

const x = Number(input.pop());

const arr = input[0].split(" ").map(Number);

arr.sort((a, b) => a - b);

let start = 0;
let end = n - 1;
let res = 0;

while (start < end) {
  const tmpSum = arr[start] + arr[end];
  if (tmpSum === x) {
    res++;
    start++;
    end--;
  } else if (tmpSum < x) {
    start++;
  } else {
    end--;
  }
}

console.log(res);
