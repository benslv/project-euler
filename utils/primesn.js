module.exports.primesN = (n) => {
	let range = [];
	for (let i = 0; i < n; i++) {
		if (isPrime(i)) range.push(i);
	}

	return range;
};

const isPrime = (factor) => {
	for (let i = 3; i < Math.sqrt(factor); i++) {
		if (factor % i == 0) return false;
	}
	return true;
};
