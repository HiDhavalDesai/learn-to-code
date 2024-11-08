var first = prompt("Hello and Welcome, Please Enter your First Name")
var last = prompt("What is your last name?")
var age = prompt("How old are you?")
var height = prompt("How tall are you in centimeters?")
var pet = prompt("What is the name of your pet?")
alert("Thank You for the information!")

if (first[0] === last[0]) {
  console.log(first[0] + last[0]);
}
if (age > 20 && age <30 age != 20 && age !=30) {
  console.log(age);
}
if (height>=170) {
  console.log(height);
}

if (pet[4] === 'y') {
  console.log(pet[4]);
}


if (first[0] === last[0]){
   if (age > 20 && age <30 && age != 20 && age !=30) {
     if (height>=170){
       if (pet[4] === 'y') {
         console.log("Hello Comrad");
         // if (pet[pet.length-1] ==='y')
       }
     }
   }
} else {
  console.log("Nothing to see here");
}

// For a proper solution please see lecture60try2.js
