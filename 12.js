const getFactors = (n) => {
	let factors = new Set();
	for (let i = 1; i <= Math.sqrt(n); i++) {
		if (n % i == 0) {
			factors.add(i);
			factors.add(n / i);
		}
	}
	return factors;
};

const genTriangleNum = (i) => {
	return 0.5 * i * (i + 1);
};

let i = 1;
while (getFactors(genTriangleNum(i)).size <= 500) {
	i += 1;
}

console.log(genTriangleNum(i));
