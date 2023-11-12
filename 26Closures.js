function outer()
{
    let count = 1;
    return function inner()
    {
        return count=count+1;
    }
}

inner = outer();

console.log(inner())


/*
function outer()
{
    let count = 1;
    
    console.log(count)
    function inner()
    {
        return count=count+1;
    }
    console.log(inner());
    console.log(count)
}

outer(); */