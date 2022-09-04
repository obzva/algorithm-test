const input = "g0en2T0s8eSoft";

function solution(input) {
  const number = Number(input.replaceAll(/\D/g, ""));
  return number;
}

console.log(solution(input));

function solution2(input) {
  let answer = "";
  for (let i = 0; i < input.length; i++) {
    if (!isNaN(input[i])) answer += input[i];
  }
  answer = Number(answer);
  return answer;
}

console.log(solution2(input));
