const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

function solution(input) {
  let res = 0;

  const words = input.slice(1);

  for (let i = 0; i < words.length; i++) {
    let isSequential = true;
    let tmp = [];
    for (let j = 0; j < words[i].length; j++) {
      if (tmp.includes(words[i][j]) && tmp[tmp.length - 1] !== words[i][j]) {
        isSequential = false;
        break;
      } else tmp.push(words[i][j]);
    }
    res = isSequential ? res + 1 : res;
  }

  return res;
}

console.log(solution(input));
