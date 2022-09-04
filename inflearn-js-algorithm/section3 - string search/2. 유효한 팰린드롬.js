const input = "found7, time: study; Yduts; emit, 7Dnuof";

function solution(input) {
  const alphabets = input.toUpperCase().replaceAll(/[^A-Z]/g, "");

  if (alphabets === alphabets.split("").reverse().join("")) return "YES";
  else return "NO";
}

console.log(solution(input));
