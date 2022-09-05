const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);

const specs = input.slice(1).map((x) => x.split(" ").map(Number));

// const N = 5;
//
// const specs = [
//   [55, 185],
//   [58, 183],
//   [88, 186],
//   [60, 175],
//   [46, 155],
// ];

function solution(N, specs) {
  let res = Array.from({ length: N }, () => 1);

  for (let i = 0; i < N; i++) {
    for (let j = i + 1; j < N; j++) {
      if (specs[i][0] > specs[j][0] && specs[i][1] > specs[j][1]) {
        res[j]++;
      } else if (specs[i][0] < specs[j][0] && specs[i][1] < specs[j][1]) {
        res[i]++;
      }
    }
  }

  res = res.join(" ");
  return res;
}

console.log(solution(N, specs));
