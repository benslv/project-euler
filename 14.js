let maxChain = 0;
let maxChainNumber = 0;

for (let i = 1; i < 1000000; i++) {
	let n = i;
	let chain = 1;
	while (n != 1) {
		if (n % 2 == 0) {
			n /= 2;
		} else {
			n = 3 * n + 1;
		}
		chain += 1;
	}

	if (chain > maxChain) {
		maxChain = chain;
		maxChainNumber = i;
	}
}

console.log(maxChainNumber, maxChain);
