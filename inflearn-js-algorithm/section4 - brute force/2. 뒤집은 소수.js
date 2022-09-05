function isPrime(x) {
  if (x === 1) return false;
  const squareRoot = Math.sqrt(x);
  for (let i = 2; i <= squareRoot; i++) {
    if (x % i === 0) return false;
  }
  return true;
}

const input = [32, 55, 62, 20, 250, 370, 200, 30, 100];

function solution(arr) {
  let res = "";

  for (let i = 0; i < arr.length; i++) {
    const reversed = Number(String(arr[i]).split("").reverse().join(""));
    if (isPrime(reversed)) res += String(reversed) + " ";
  }

  return res.trim();
}

console.log(solution(input));
