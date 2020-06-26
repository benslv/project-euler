const isPythagoras = (a, b, c) => {
	return a ** 2 + b ** 2 === c ** 2;
};

for (let a = 1; a < 1000; a++) {
	for (let b = a; b < 1000 - a; b++) {
		c = 1000 - a - b;
		if (c < b) break;
		if (isPythagoras(a, b, c)) {
			console.log(a * b * c);
		}
	}
}
