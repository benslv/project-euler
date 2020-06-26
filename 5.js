n = 1;

// Create and populate an array of digits 1 to 20 inclusive;
nums = [];
for (let i = 1; i <= 20; i++) {
	nums.push(i);
}

// Increment through possible values of n until one is found satisfying the `every` function.
let found = false;
while (!found) {
	found = nums.every((i) => n % i == 0);

	if (!found) {
		n += 1;
	}
}

console.log(n);
