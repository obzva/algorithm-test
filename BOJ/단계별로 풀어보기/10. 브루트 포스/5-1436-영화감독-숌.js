const input = require("fs").readFileSync("dev/stdin").toString().trim();

const N = Number(input);

function isTarget(str) {
  let cnt = 0;
  for (let i = 0; i < str.length; i++) {
    if (str[i] === "6") {
      cnt++;
      if (cnt === 3) return true;
    } else {
      cnt = 0;
    }
  }
  return false;
}

function solution(N) {
  if (N === 1) return 666;
  let number = 666;
  let cnt = 1;
  while (cnt < N) {
    number++;
    const str = String(number);
    if (isTarget(str)) cnt++;
  }
  return number;
}

console.log(solution(N));
