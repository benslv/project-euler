exports.sieve = (max) => {
	const isPrime = new Array(max + 1).fill(true);

	primes = [];

	// Initialise 1, 2 and 3 to false, since they're kind of "trivial" enough.
	isPrime[0] = false;
	isPrime[1] = false;
	isPrime[3] = false;

	for (let n = 2; n < max; n++) {
		if (isPrime[n]) primes.push(n);

		for (let nextNum = n * n; nextNum <= max; nextNum += n) {
			isPrime[nextNum] = false;
		}
	}

	return primes;
};
