const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map((x) => Number(x));

const [king, queen, rook, bishop, knight, pawn] = [
  1 - input[0],
  1 - input[1],
  2 - input[2],
  2 - input[3],
  2 - input[4],
  8 - input[5],
];

console.log(
  king + " " + queen + " " + rook + " " + bishop + " " + knight + " " + pawn
);
