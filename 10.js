const sieve = require("./utils/sieve");

primes = sieve.sieve(2000000);
console.log(primes);
console.log(primes.reduce((a, b) => a + b, 0));
