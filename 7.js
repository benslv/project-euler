// const sieve = require("./utils/sieve.js");

// let n = 2;

// while (sieve.sieve(n).length < 6) {
// 	n *= 2;
// }

// console.log(sieve.sieve(n)[10000]);

let n = 2;
let primes = [];

const isPrime = (num) => {
	for (let i = 2; i < num; i++) {
		if (num % i == 0) return false;
	}
	return true;
};

while (primes.length < 10001) {
	if (isPrime(n)) primes.push(n);
	n += 1;
}

console.log(primes[10000]);
