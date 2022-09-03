let res = "";

const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

const C = Number(input[0]);

for (let i = 1; i <= C; i++) {
  const splitInput = input[i]
    .trim()
    .split(" ")
    .map((x) => Number(x));

  const [N, scores] = [splitInput[0], splitInput.slice(1)];

  const mean = scores.reduce((prev, curr) => prev + curr, 0) / N;

  let cnt = 0;

  for (let j = 0; j < N; j++) {
    if (scores[j] > mean) cnt++;
  }

  res += String(((cnt / N) * 100).toFixed(3)) + "%\n";
}

console.log(res.trim());
