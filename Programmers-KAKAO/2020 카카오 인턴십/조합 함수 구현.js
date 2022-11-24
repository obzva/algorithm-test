/**
 *
 * @param a: array
 * @param n: the length of a combination
 * @return [[]]: combinations
 */
const combine = (a, n) => {
  const result = [];
  const dfs = (combination, start, k) => {
    if (k === 0) result.push([...combination]);
    else {
      for (let i = start; i < a.length; i++) {
        combination.push(a[i]);
        dfs(combination, i + 1, k - 1);
        combination.pop();
      }
    }
  };
  dfs([], 0, n);
  return result;
};
