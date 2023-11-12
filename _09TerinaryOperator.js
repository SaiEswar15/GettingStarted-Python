let age = 18

let result = age<18 ? "not allowed" : "allowed";

console.log(result);

//write using a function 

function validateAge()
{
    return age<18 ? "not allowed" : "allowed"
}

let answer = validateAge();