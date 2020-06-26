nums = [];
for (let i = 1; i <= 100; i++) {
	nums.push(i);
}

sumSquares = nums.reduce((a, b) => a + b * b, 0);

squaresSum = Math.pow(
	nums.reduce((a, b) => a + b, 0),
	2,
);

console.log(squaresSum - sumSquares);
