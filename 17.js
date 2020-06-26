const numToWords = require("num-to-words").numToWords;

let str = "";

for (let i = 1; i <= 1000; i++) {
	str += numToWords(i, { ands: true });
}
console.log(str);
console.log(str.replace(/\-/g, "").replace(/\s/g, "").length);

// I shouldn't really have needed to use a third-part library here but I'm
// kind of lazy and really didn't fancy having to work out how to manually construct
// each number from scratch when something else could do it for me.
