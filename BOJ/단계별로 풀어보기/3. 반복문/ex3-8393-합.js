const input = Number(require("fs").readFileSync("dev/stdin").toString().trim());

let res = 0;

for (let i = 1; i <= input; i++) res += i;

console.log(res);
