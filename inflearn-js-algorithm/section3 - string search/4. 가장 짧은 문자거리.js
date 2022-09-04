const input = "teachermode e";

function solution(input) {
  const [str, target] = input.split(" ");
  let answer = "";
  for (let i = 0; i < str.length; i++) {
    if (str[i] === target) {
      answer += "0 ";
      continue;
    }
    let [j, k] = [i - 1, i + 1];
    let dist = 1;
    while (0 <= j || k < str.length) {
      if (str[j] === target || str[k] === target) {
        answer += String(dist) + " ";
        break;
      } else {
        j--;
        k++;
        dist++;
      }
    }
  }
  return answer.trim();
}

console.log(solution(input));

function solution2(input) {
  const [str, target] = input.split(" ");

  const N = str.length;

  const answer = [];

  let p = 1000;
  for (let i = 0; i < N; i++) {
    if (input[i] === target) {
      p = 0;
    } else p++;
    answer.push(p);
  }

  p = 1000;
  for (let i = 0; i < N; i++) {
    if (input[N - 1 - i] === target) {
      p = 0;
    } else p++;
    answer[N - 1 - i] = Math.min(answer[N - 1 - i], p);
  }
  return answer.join(" ");
}

console.log(solution2(input));
