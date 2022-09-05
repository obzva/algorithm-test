const input = require("fs").readFileSync("dev/stdin").toString().trim();

const N = Number(input);

function solution(N) {
  for (let i = 1; i < N; i++) {
    const sum =
      i +
      String(i)
        .split("")
        .map((x) => Number(x))
        .reduce((prev, curr) => prev + curr, 0);
    if (sum === N) return i;
  }
  return 0;
}

console.log(solution(N));
