const N = Number(require("fs").readFileSync("dev/stdin").toString().trim());

for (let i = 0; i < N; i++) {
  console.log("*".repeat(i + 1));
}
