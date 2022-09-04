const input = require("fs").readFileSync("dev/stdin").toString().trim();

const arr = Array.from({ length: 26 }, () => -1);

for (let i = 0; i < input.length; i++) {
  const loc = input.charCodeAt(i) - 97;
  if (arr[loc] === -1) {
    arr[loc] = i;
  }
}

const res = arr.join(" ");

console.log(res);
