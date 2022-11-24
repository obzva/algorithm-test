function solution(s) {
  const sets = s
    .slice(2, s.length - 2)
    .split("},{")
    .map((x) => {
      return x.split(",");
    });

  const counter = new Map();
  for (let i = 0; i < sets.length; i++) {
    const set = sets[i];
    for (let j = 0; j < set.length; j++) {
      if (counter.has(set[j])) counter.set(set[j], counter.get(set[j]) + 1);
      else counter.set(set[j], 1);
    }
  }

  const answer = new Array(sets.length);
  counter.forEach((value, key) => {
    answer[-value + sets.length] = parseInt(key);
  });

  return answer;
}
