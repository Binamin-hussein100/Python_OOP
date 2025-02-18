// variables

// age
let age = 12
// keyword var_name value
const speed = 16

// Datatypes
// numbers
// strings 
let lname = "John Doe"

console.log(lname.toUpperCase())
// Booleans
let isActive = true || false 


// integers
let num1 = 10
let num2 = 15.4
console.log(typeof(num1), typeof(num2))
// Array

let listy = [1,2,true, [1,2,3,4]]
// objects

let student = {
    name:"John",
    age:15
}

student.name
// null ==> absence of a value
let age1 = null

// let plate = 1002


// `The plate is ${plate}`

// functions

// sequence
// reusable
// syntax , Parameters, keyword, {}, fn Name, return,body,arg, invocation

function getName(fname){
    // function body
    return `This is the ${fname} `
    console.log(fname)
}

console.log(getName("John Doe1"))

