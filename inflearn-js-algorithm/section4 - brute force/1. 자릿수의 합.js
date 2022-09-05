const input = [128, 460, 603, 40, 521, 137, 123];

function solution(arr) {
  const sums = arr.map((x) =>
    String(x)
      .split("")
      .map((e) => Number(e))
      .reduce((prev, curr) => prev + curr, 0)
  );

  const max = Math.max(...sums);

  const maxs = arr.filter((x, i) => sums[i] === max);

  const res = Math.max(...maxs);

  return res;
}

function solution2(arr) {
  let res = 0;
  let max = Number.MIN_SAFE_INTEGER;

  for (let i = 0; i < input.length; i++) {
    const sum = String(arr[i])
      .split("")
      .map((e) => Number(e))
      .reduce((prev, curr) => prev + curr, 0);

    if (sum > max) {
      res = arr[i];
      max = sum;
    } else if (sum === max) {
      res = res >= arr[i] ? res : arr[i];
    }
  }
  return res;
}

console.log(solution2(input));
