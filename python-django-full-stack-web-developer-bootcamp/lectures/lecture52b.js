var lbs = prompt("Please enter a weight in Pounds")
var kgs = lbs * 0.453592
alert(lbs + " is " +  kgs +" kilograms")
console.log("Conversaion Completed")

var kgs2 = prompt("Please enter a weight in kilograms")
var lbs2 = kgs2 / 0.453592
alert(kgs2 +" is " + lbs2 + " pounds")
console.log("Conversaion Completed 2")

alert(lbs +" was the first weight in pounds, " + kgs+" was the first kilogram conversion. " + kgs2 + " is the second conversion and in pounds that is "+ lbs2)
