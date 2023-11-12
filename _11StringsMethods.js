let name_use1 = "";
name_use1 = 'ESWAR'
console.log(name_use1.toLowerCase());

name_use1 = "eswar";
console.log(name_use1.toUpperCase());

name_use1 = "eswar";
console.log(name_use1.startsWith("e"));
console.log(name_use1.endsWith("r"));
console.log(name_use1[0]);
console.log(name_use1[name_use1.length-1]);
console.log(name_use1 + name_use1);

console.log(name_use1.split(""))

name_use1 = [ 'e', 's', 'w', 'a', 'r' ];
console.log(name_use1.join(""))

name_use1 = "     hai    this      "
console.log(name_use1.split(" ").join(""))

console.log(name_use1.trim(" "));
console.log(name_use1.indexOf("a"));
console.log(name_use1.includes("a"));
console.log(name_use1.lastIndexOf("a"));