//iife function
(function()
{
    console.log("eswar")
})()

//anonymous functions 
let solve = function(a,b)
{
    return a*b
}

console.log(solve(2,3));

//arrow functions
let solveAgain = (a,b)=>{
    return a*b
}
console.log(solveAgain(5,8))

//arrow function in single line
let solveThird = (a,b) => a*b;

console.log(solveThird(8,4))