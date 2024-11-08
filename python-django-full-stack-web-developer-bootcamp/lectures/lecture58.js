// Exercise 1 - Use a for loop to print out the word Hello 5 times; do with with a while loop and a for loop
var word = "Hello"
var i = 0

while (i<5) {
  console.log(word);
  i++
}


// For Statement

var word ="hello"

for (var i = 0; i < word.length; i++) {
  console.log(word);
}


// Exercise 2 - Print odd numbers from 1 to 25; use while and for loop

var i = 0

while (i<25) {
  i++
  console.log(i);
    if (i%2 !== 0) {
        i++
    }

}

// For statement
for (var i = 0; i < 25; i++) {
  if (i%2 ===0) {
      i++
  }
  console.log(i);
}
