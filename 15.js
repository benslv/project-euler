const solveRoutes = (n) => {
	let arr = [];
	let emptyArr = new Array(n).fill(0);

	for (let i = 0; i < n; i++) {
		arr.push([...emptyArr]); // Apparently I have to do this because otherwise JS treats ever array as a reference of each other instead of separate things.
	}

	for (let row = 0; row < arr.length; row++) {
		for (let col = 0; col < arr.length; col++) {
			if (col > 0) {
				arr[row][col] += arr[row][col - 1] === 0 ? 1 : arr[row][col - 1];
			}
			if (row > 0) {
				arr[row][col] += arr[row - 1][col] === 0 ? 1 : arr[row - 1][col];
			}
		}
	}

	return arr;
};

console.log(solveRoutes(21));
