const permute = (inputArray, size) => {
  const result = [];
  const prev = [];
  const dfs = (arr) => {
    if (arr.length === inputArray.length - size) result.push([...prev]);
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
  dfs(inputArray, size);
  return result;
};
