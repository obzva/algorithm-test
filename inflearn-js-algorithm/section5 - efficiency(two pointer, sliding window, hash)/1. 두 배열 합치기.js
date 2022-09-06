const N = 3;
const arr1 = [1, 3, 5];
const M = 5;
const arr2 = [2, 3, 6, 7, 9];

let p1 = 0,
  p2 = 0;
let res = [];

while (p1 < N && p2 < M) {
  if (arr1[0] <= arr2[0]) {
    res.push(arr1.shift());
    p1++;
  } else {
    res.push(arr2.shift());
    p2++;
  }
}

if (arr1.length === 0) {
  res.push(...arr2);
} else {
  res.push(...arr1);
}

console.log(res);
