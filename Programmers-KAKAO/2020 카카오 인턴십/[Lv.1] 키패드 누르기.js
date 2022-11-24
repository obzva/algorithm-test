function solution(numbers, hand) {
  const coords = {
    1: [0, 0],
    2: [0, 1],
    3: [0, 2],
    4: [1, 0],
    5: [1, 1],
    6: [1, 2],
    7: [2, 0],
    8: [2, 1],
    9: [2, 2],
    0: [3, 1],
  };
  let currLeft = [3, 0];
  let currRight = [3, 2];
  let answer = "";
  for (let i = 0; i < numbers.length; i++) {
    const num = numbers[i];
    if (num === 1 || num === 4 || num === 7) {
      answer += "L";
      currLeft = coords[num];
    } else if (num === 3 || num === 6 || num === 9) {
      answer += "R";
      currRight = coords[num];
    } else {
      const coord = coords[num];
      const distLeft =
        Math.abs(coord[0] - currLeft[0]) + Math.abs(coord[1] - currLeft[1]);
      const distRight =
        Math.abs(coord[0] - currRight[0]) + Math.abs(coord[1] - currRight[1]);
      if (distLeft < distRight) {
        answer += "L";
        currLeft = coord;
      } else if (distLeft > distRight) {
        answer += "R";
        currRight = coord;
      } else {
        if (hand === "right") {
          answer += "R";
          currRight = coord;
        } else {
          answer += "L";
          currLeft = coord;
        }
      }
    }
  }
  return answer;
}
