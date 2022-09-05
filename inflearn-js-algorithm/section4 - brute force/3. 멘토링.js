const input = [
  [3, 4, 1, 2],
  [4, 3, 2, 1],
  [3, 1, 4, 2],
];

function solution(arr) {
  const N = arr[0].length;
  const M = arr.length;

  let res = 0;

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (i === j) continue;
      let match = true;
      for (let k = 0; k < M; k++) {
        if (arr[k].indexOf(i + 1) > arr[k].indexOf(j + 1)) match = false;
      }
      // console.log(`(${i + 1}, ${j + 1}): ${match}`);
      if (match) res++;
    }
  }
  return res;
}

console.log(solution(input));
