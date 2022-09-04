const input = require("fs").readFileSync("dev/stdin").toString().trim();

let res = 0;

for (let i = 0; i < input.length; i++) {
  let code = input.charCodeAt(i) - 65;
  let number = 0;
  if (code < 15) {
    number = Math.floor(code / 3) + 2;
  } else {
    if (code === 15) number = 7;
    else {
      code = code - 16;
      number = Math.floor(code / 3) + 7;
      if (number > 9) number = 9;
    }
  }

  res += number + 1;
}

console.log(res);
