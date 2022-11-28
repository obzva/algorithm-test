function solution(expression) {
  const opOrders = permutation(["+", "-", "*"]);

  const expressionList = [];
  let prev = "";
  for (let i = 0; i < expression.length; i++) {
    if (isNaN(expression[i])) {
      expressionList.push(parseInt(prev));
      prev = "";
      expressionList.push(expression[i]);
    } else {
      prev += expression[i];
    }
  }
  expressionList.push(parseInt(prev));

  let answer = 0;
  for (let i = 0; i < opOrders.length; i++) {
    const opOrder = opOrders[i];
    const newList = [...expressionList];
    for (let j = 0; j < 3; j++) {
      const operation = opOrder[j];
      let k = 1;
      while (k < newList.length) {
        if (newList[k] === operation) {
          newList.splice(
            k - 1,
            3,
            evaluate(newList[k - 1], newList[k + 1], operation)
          );
        } else {
          k++;
        }
      }
    }
    answer = Math.max(answer, Math.abs(newList[0]));
  }
  return answer;
}

const permutation = (inputArray) => {
  const result = [];
  const prev = [];

  const permute = (arr) => {
    if (arr.length === 0) {
      result.push([...prev]);
    } else {
      for (let i = 0; i < arr.length; i++) {
        const newArr = [...arr];
        prev.push(newArr[i]);
        newArr.splice(i, 1);
        permute(newArr);
        prev.pop();
      }
    }
  };

  permute(inputArray);
  return result;
};

const evaluate = (num1, num2, operation) => {
  return operation === "+"
    ? num1 + num2
    : operation === "-"
    ? num1 - num2
    : num1 * num2;
};
