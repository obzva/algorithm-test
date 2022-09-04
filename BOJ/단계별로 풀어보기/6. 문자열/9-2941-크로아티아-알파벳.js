// const input = require("fs").readFileSync("dev/stdin").toString().trim();

const input = "ljes=njak";

function solution(input) {
  let res = 0;

  let i = 0;
  while (i < input.length) {
    if (input[i] === "c") {
      if (input[i + 1] === "=" || input[i + 1] === "-") {
        res++;
        i += 2;
      } else {
        res++;
        i++;
      }
    } else if (input[i] === "d") {
      if (input[i + 1] === "z" && input[i + 2] === "=") {
        res++;
        i += 3;
      } else if (input[i + 1] === "-") {
        res++;
        i += 2;
      } else {
        res++;
        i++;
      }
    } else if (input[i] === "l" && input[i + 1] === "j") {
      res++;
      i += 2;
    } else if (input[i] === "n" && input[i + 1] === "j") {
      res++;
      i += 2;
    } else if (input[i] === "s" && input[i + 1] === "=") {
      res++;
      i += 2;
    } else if (input[i] === "z" && input[i + 1] === "=") {
      res++;
      i += 2;
    } else {
      res++;
      i++;
    }
  }

  return res;
}

console.log(solution(input));

function solution2(input) {
  let str = input;
  const specialChar = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="];
  for (let i = 0; i < specialChar.length; i++) {
    str = str.replaceAll(specialChar[i], "1");
  }
  return str.length;
}

console.log(solution2(input));
