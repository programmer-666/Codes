var x = 3.14159265358979;

xabs = Math.abs(x); // mutlak değer
Math.acos();Math.acosh();

console.log(Math.max(1,2,3,4,5,6,7,8,9));

console.log(Math.trunc(Math.random()*10)); // 0 - 10 arası rando
// trunc float sayının sadece tamsayı kısmını alır - round da kullanılabilir

var url = "https://www.suhaarslan.com/denemesafası"; // url encode

console.log(decodeURI(encodeURI(url)));//component olanlar componentlerle, özel karakter çevirmede kullanılır component

// // // // // // // // // // // // // // // // // // // // // // // // // // // // // // //

console.log(parseFloat("  10.1451224523 TEST")); // float dönüşüm, sadece sayı 

console.log(Number.isInteger(3));

console.log("lorem".charAt(1));
console.log("lorem".charCodeAt(2)); // indexteki haralfanümerik değerin ascii karşılığı

console.log("lorem".concat(" ipsum", " dolor"));

console.log("lorem ipsum".endsWith("ipsum")); // startswith 

console.log(String.fromCharCode(65)); // ascii kodundan stringe 

console.log("stringval".includes("tr", 1)); // 1.indexten sonra arar

console.log("lorem ipsum dolor sit amet".indexOf("ip")); // index sorgulama, bulamazsa -1
// lastindexof ile sondan arama yapılır

