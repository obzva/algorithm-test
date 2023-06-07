// my solution
// /**
//  * @param {number[]} nums
//  * @param {number} target
//  * @return {number[]}
//  */
// var twoSum = function (nums, target) {
//   const numPairs = nums.map((n, i) => [n, i]).sort((a, b) => a[0] - b[0]);
//   const n = numPairs.length;
//   let head = 0;
//   let tail = n - 1;
//   while (head < tail) {
//     const sum = numPairs[head][0] + numPairs[tail][0];
//     if (sum < target) {
//       head++;
//     } else if (sum > target) {
//       tail--;
//     } else {
//       return [numPairs[head][1], numPairs[tail][1]];
//     }
//   }
// };

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  const map = new Map();
  for (let i = 0; i < nums.length; i++) {
    if (map.has(target - nums[i])) {
      return [map.get(target - nums[i]), i];
    }
    map.set(nums[i], i);
  }
};
