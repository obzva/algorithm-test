const input = Number(require("fs").readFileSync("dev/stdin").toString().trim());
for (let i = 1; i <= 9; i++) {
  console.log(input, "*", i, "=", input * i);
}
