//for (var, whileloop, execuation)

for (var i = 0; i <= 10; i++) {
 console.log(i);}

//  var i happens before the loop starts, then i < 5 happens while the loop is running, and then i++ happens after and what we actually wanted to change, and then starts again to make sure that i<5; and then stops

for (var i = 0; i < 5; i++) {
  console.log("Number is "+i);
}

// This is similar to a while loop; we have some inital condition, the while condition and then what we want do after the loop runs.


var word = "ABCDEFGHIJK"

for (var i = 0; i < word.length; i++) {
  console.log(word[i]);
}
// Guess solution -
// A then AB then ABC then ABCD
// My guess was wrong; it just wrote out 1 letter for each line.


// Skipping every other letter

var word ="ABABABABAB"

for (var i = 0; i < word.length; i=i+2) {
  console.log(word[i]);
}
// I guessed that it would print Bs 5 times; but I was wrong, it printed A 5 times, it displayed (5) (in circle) with A next to it.
