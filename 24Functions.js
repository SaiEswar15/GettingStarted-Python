// if we pass the array inside function will it be mutable

let arr = ["eswar", "sai"];

function changeArray(arr)
{
    arr.push("kumar")
}

changeArray(arr)
console.log(arr);

// if we pass the variables with numbers and strings inside function will it be mutable

let number = "eswar";

function changeNumber(arr)
{
    arr = "kumar"
}

changeNumber(number)
console.log(number);

//nested function 

function solve(str)
{
    str = "kumar"
    function solve2(str)
    {
        return "john"
    }
    return solve2(str)
}
value = "eswar"
console.log(solve(value));
console.log(value);

//global scope can be used inside the local scope

let count = 10

function identify()
{
    count++;
    console.log(count)
}

identify()