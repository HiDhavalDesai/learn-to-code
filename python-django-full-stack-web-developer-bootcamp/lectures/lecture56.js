var x = 0;

while (x < 5) {
  console.log("x is currently:" + x);
  console.log("x is still less than 5, add 1 to x");
  x = x+1
}

// This code is saying that check the current value of x, if x is less than 5, then add 1 to x, then check x again.
// This keeps going until x < 5; that is when the loop ends.



// Adding a break

var x = 0;

while (x <5) {
 console.log("x is currently:" + x);
  if (x === 3) {
    console.log("x is equal to three!");
    break;
  }
 console.log("x is still less than 5, add 1 to x");
  x = x+1;
}


// Adding Break will stop the loop from continuing.
// What this code is saying, if X is equal to three, log this and then break out of the top level loop that you find this while keyword in.


var x = 0;

while (x <10) {
  x = x+2
  console.log(x);
if (x ===10 ) {
  break;
}
}

// This is one way to do it; but I don't think it's the correct way to do it.
// The correct way to do this is

var num = 1;

while (num<11) {
  num = num +1
  if (num%2 === 0) {
    console.log(num);
  }
}

// This means that we are checking the number divided by 2 to see if we can divide by it evenly, if we can then we display that number, if we can't then we don't display that number