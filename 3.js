num = 600851475143;
factors = [];

for (let i = 0; i < Math.sqrt(num); i++) {
	if (num % i == 0) {
		factors.push(i);
	}
}

console.log(factors);

const isPrime = (factor) => {
	for (let i = 3; i < Math.sqrt(factor); i++) {
		if (factor % i == 0) return false;
	}
	return true;
};

console.log(factors.filter((f) => isPrime(f)));
