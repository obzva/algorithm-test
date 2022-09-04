const input = "KKHSSSSSSSE";

function solution(input) {
  let str = input + " ";
  let tmp = str[0];
  let cnt = 1;
  let res = "";
  for (let i = 1; i < str.length; i++) {
    if (str[i] === tmp) {
      cnt++;
    } else {
      res += cnt === 1 ? tmp : tmp + String(cnt);
      tmp = str[i];
      cnt = 1;
    }
  }
  return res;
}

console.log(solution(input));
