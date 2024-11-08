// alert("Hello"); This is just to check if the file is linked correctly.

// var hot = false;
// var temp = 60;
// First we declare the variables, then we can add comparisons or logic to it.

// First if-statement, this is just a silly test.
//  if (condition) {
//   console.log("I ran");
//  }

// Real if-statement - This if statement, is checking if the temp is 80+, if so then write text, if not, then nothing.
// if (temp > 80) {
//   console.log("Temp is greater than 80");
// }

// -------- //

// var hot = false;
// var temp = 100;
// Second time we are setting the variables

// Reassigning a variable in Javascript; hot is now considered to be true, if the temp is greater than 80; if not then the reassignment doesn't occure.
// if (temp > 80) {
//   hot = true;
// }
// console.log(hot);
// This output is false, because the temp is not greater than 80. Since the variable temp was now changed, the output is true.


// if-else statement; If condition 1 is true; then run first console, else run second console. Else is only if the first statement is false, then run that code.
// if (temp>80) {
//  console.log("Hot outside"); 
// } else { console.log("Its not very hot today!");
// }
// You can change the temp variable to 50 degress to see what the console will log.
  // If the first statement isn't true, then will the else statement run, and the else statement doesn't have a condition because it's not an else-if. As well as it being a false statement; if temp>80 then run first code, else (if it's false) then run the second code.

// ----------- //

// Else-If statements: We can use this to check for multiple conditions; I'm resetting the variables and recreating the if-else-if statement; you can change the variable and the console output will change base on the if-else-if-statements.
// var hot = false;
// var temp =  50;

// if (temp>80) {
//   console.log("hot outside!");
// } else if(temp <= 80 && temp >= 50) {
//   console.log("Average temp outside");
// } else if (temp < 50 && temp >= 32) {
//   console.log("it's pretty cold out!");
// } else{console.log("It is very cold out!");
// }

// This is a ham and cheese store stock check


var ham = 0;
var cheese = 0;

var report = "blank";

if (ham >= 10  && cheese >= 10) {
  report = "Strong Sales of both Ham and Cheese"
}else if (ham === 0 && cheese === 0) {
  report = "Nothing Sold!"
}else {
  report = "We had some sales of items"
}

console.log(report);
