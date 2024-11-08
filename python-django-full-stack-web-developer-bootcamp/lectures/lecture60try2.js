// Checking to see if there is a spy among us

// Variables
var first = prompt("What is your first name?")
var last = prompt("What is your last name?")
var age = prompt ("What is your age?")
var height = prompt("What is your height?")
var pet = prompt("what is your pet name?")


// Boolean control to check if they are a spy
var name = null;
var ageck = null;
var hc = null;
var pc = null;
// these could have been false, but null would make sure they don't run.

// control flow check
// name
if (first[0] === last[0]) {
    name = true;
}

//age Check
if (age>20 && age < 30) {
  ageck = true;
}

// height Check
if (height >= 170) {
  hc = true;
}

// pet Check
if ((pet[pet.length - 1]) === 'y') {
  pc = true;
}
// Okay I understood this now; took a few tries, the variable pet[0], would equal to the first letter of the pet, but then pet[pet.length - 1] will give the last letter of the pet variable and then check to see if it's a y

// Checking if they are a spy
if (name && ageck && hc && pc) {
  console.log("Welcome Spy");
} else {
  console.log("Nothing to see here");
}



// I did not enter else statements as they are not needed; if the Boolean are not true, then they will remain at null.
