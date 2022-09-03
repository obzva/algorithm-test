const input = "assa";

function solution(input) {
  const str = input.toUpperCase();

  let [i, j] = [0, str.length - 1];

  while (i < j) {
    if (str[i] !== str[j]) {
      console.log("NO");
      return;
    }
    i++;
    j--;
  }
  console.log("YES");
}

function solution2(input) {
  const str = input.toUpperCase();

  const reverseStr = str.split("").reverse().join("");

  console.log(str === reverseStr ? "YES" : "NO");
}

console.log(solution2(input));
