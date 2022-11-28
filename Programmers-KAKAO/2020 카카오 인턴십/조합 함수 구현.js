const combine = (inputArray, size) => {
  const result = [];
  const dfs = (prev, start, count) => {
    if (count === 0) result.push([...prev]);
    else {
      for (let i = start; i < inputArray.length; i++) {
        prev.push(inputArray[i]);
        dfs(prev, i + 1, count - 1);
        prev.pop();
      }
    }
  };
  dfs([], 0, size);
  return result;
};
