const input = require("fs").readFileSync("dev/stdin").toString().trim();

let [a, b] = input.split(" ");

a = Number(a.split("").reverse().join(""));
b = Number(b.split("").reverse().join(""));

if (a > b) console.log(a);
else console.log(b);
