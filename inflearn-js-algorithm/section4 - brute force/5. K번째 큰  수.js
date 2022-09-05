const input = [
  [10, 3],
  [13, 15, 34, 23, 45, 65, 33, 11, 26, 42],
];

function solution(arr) {
  const [N, K] = arr[0];
  const numbs = arr[1];
  numbs.sort((a, b) => b - a);

  // brute force is unnecessary
  const r1 = numbs[1] - numbs[2];
  const r2 = numbs[3] - numbs[4];

  if (r1 > r2) return numbs[0] + numbs[1] + numbs[4];
  else return numbs[0] + numbs[2] + numbs[3];
}

console.log(solution(input));
