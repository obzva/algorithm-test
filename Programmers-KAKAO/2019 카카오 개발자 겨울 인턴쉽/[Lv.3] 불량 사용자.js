function solution(user_id, banned_id) {
  const match = (userId, bannedId) => {
    bannedId = bannedId.replace(/\*/g, ".");
    const regExp = new RegExp("^(" + bannedId + ")$");
    return regExp.test(userId);
  };

  let answer = new Set();
  const dfs = (bIdx, path) => {
    if (bIdx === banned_id.length) {
      answer.add(path.join(""));
      return;
    }
    for (let i = 0; i < user_id.length; i++) {
      if (match(user_id[i], banned_id[bIdx]) && path[i] === 0) {
        const newPath = [...path];
        newPath[i] = 1;
        dfs(bIdx + 1, newPath);
      }
    }
  };
  dfs(0, new Array(user_id.length).fill(0));
  return answer.size;
}
