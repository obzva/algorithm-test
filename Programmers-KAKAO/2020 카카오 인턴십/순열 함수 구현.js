/**
 * @param a: array
 * @returns {*[]}
 */
const permute = (a) => {
  const result = [];
  const prev = [];
  const dfs = (arr) => {
    if (arr.length === 0) result.push([...prev]);
    else {
      for (let i = 0; i < arr.length; i++) {
        const newArr = [...arr];
        prev.push(arr[i]);
        newArr.splice(i, 1);
        dfs(newArr);
        prev.pop();
      }
    }
  };
  dfs(a);
  return result;
};

console.log(permute([1, 2, 3]));
