const input = [
  [5, 28],
  [6, 6],
  [2, 2],
  [4, 3],
  [4, 5],
  [10, 3],
];

function solution(arr) {
  let res = 0;

  const N = arr[0][0];
  const budget = arr[0][1];

  let list = arr.slice(1);
  list.sort((a, b) => a[0] + a[1] - (b[0] + b[1]));

  let remain = budget;
  let i = 0;
  while (remain >= list[i][0] + list[i][1]) {
    remain -= list[i][0] + list[i][1];
    i++;
    res++;
  }

  list = list.slice(i).map((x) => x[0] / 2 + x[1]);
  list.sort((a, b) => a - b);

  let j = 0;
  while (remain >= list[j]) {
    remain -= list[j];
    j++;
    res++;
  }

  return res;
}

console.log(solution(input));
