//node index.js

//variables
let name = "node";
console.log(name);
console.log("Hello World!");

//constant variables
const Name = "constant";
Name = "hello";
console.log(Name);

// let age = 17;
// if (age < 5) {
//   console.log("Baby");
// } else if (age >= 5 && age <= 12) {
//   console.log("Child");
// } else if (age > 12 && age <= 18) {
//   console.log("Teenager");
// } else {
//   console.log("Adult");
// }

//data types
let x = 34;
console.log(`The value of x is ${x}`);

//static type and dynamic type
let str = "I am a string.";
console.log(typeof str); //output:string
str = 34;
console.log(typeof str); //output:number
let nam = "object";
let age = 20;
let isApproved = true;
let firstname = undefined;
let color = null;
//arrays
// let arr = [1, 2, 3];
// console.log(arr[0]); //output:1
// console.log(arr[1]); //output:2

//objects
let person = {
    name: "John",
    age: 36,
};
console.log(person.name); //output: John