const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map((x) => Number(x));

const [H, M] = input;

// const minute = 60 * H + M;
//
// const day = 60 * 24;
//
// const augMinute = minute - 45;
//
// if (augMinute >= 0) {
//   const newH = Math.floor(augMinute / 60);
//   const newM = augMinute % 60;
//   console.log(newH + " " + newM);
// } else {
//   const newH = Math.floor((day + augMinute) / 60);
//   const newM = (day + augMinute) % 60;
//   console.log(newH + " " + newM);
// }

if (M >= 45) console.log(H, M - 45);
else {
  if (H) console.log(H - 1, 60 + M - 45);
  else console.log(23, 60 + M - 45);
}
