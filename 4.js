palindromes = [];

for (let i = 100; i < 1000; i++) {
	for (let j = 100; j < 1000; j++) {
		prod = i * j;
		if (prod.toString() === prod.toString().split("").reverse().join("")) {
			palindromes.push(prod);
		}
	}
}

// console.log(palindromes);
console.log(Math.max(...palindromes));
