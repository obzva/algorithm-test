let N = Number(require("fs").readFileSync("dev/stdin").toString().trim());
let target = N;

let res = 0;

while (target !== N || res === 0) {
  res++;
  N = (N % 10) * 10 + ((Math.floor(N / 10) + (N % 10)) % 10);
}

console.log(res);
