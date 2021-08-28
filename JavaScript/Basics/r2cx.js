/*
try{
    console.log('try');
    x
}catch(ex){
    console.log('cat');
    console.log(ex);
}finally{
    console.log('fin');
}

try{
    throw "common issue";
}catch(ex){
    console.log(ex);
}*/

/*
 var ary = [];
 ary[0] = [1,2,3];
 console.log(ary.length+" "+"lorem ipsum dolor sit amet".length); // 2. harf uzunluğu

 console.log(ary[0][1]);*/
/*
 var x = [1,2,3,4,5,6];
 var y = [7,8,9,0];

 x = x.concat(y, x);

 console.log(x);*/

//console.log(" ".constructor);
//console.log([].constructor);
/*
var x = [1,2,3,4,5,6,7];
console.log(x);

//x.copyWithin(2); // 3.elemana 1.elemanı kopyalar
//x.copyWithin(0, 2); // 2 den sonrasını 0 a yazar
x.copyWithin(0, 1, 3); // 1-3 arasını 0 a yazar
console.log(x);*/
/*
var ary = [1,2,3,4,5,6,7,8,9,0];

var i  = ary.entries();
console.log(i.next().value[0])

function check(ary){
    return ary < 51; // hepsi 51 den küçük mü
}

console.log(ary.every(check)); */

var x = [1,2,3,4,5,6,7,8,9,0];
/*
x.fill(null, 3, 4);

console.log(x);*/

//function check(x){
//    return x < 5;
//}

//console.log(x.filter(check));
/*
function show(i){
    return i > 4; // numaradan küçük olanın numarasını göster
}

console.log(x[x.findIndex(show)])*/

/*
x.forEach(function (print){
    console.log(print);
})
*/

//const nary = Array.from("apple"); //* * * işe yarar

//console.log(x.includes(3, 2)) // 3 değerine sahip eleman 2.indexte mi
/*
console.log(x.indexOf(2, 0)); // ikinci parametre ile 0.indexten sonra 2 değerine sahip elemanı ara ve dur, bulursa index numarası döner
// lastindexof ile tersten arama

console.log(Array.isArray(x));

x.join(' - '); // ayraç

console.log(x);*/

/*
for (i of x.keys()){
    console.log(i+" "+x[i]);
}
*/

/*
console.log(x.map(function carp(i){
    return i*2;
}));*/
/*
x.pop(); // dizideki son elemanı siler
x.push(0); // dizi sonuna parametre olarak verilen değeri ekler
console.log(x);*/
/*
console.log(x.reduce(function calc(x,y){
    return x+y; // dizideki elemanları toplar
}, 0)); // sonuca ekler
*/

//x.reverse() // ters
/*
console.log(x);
x.shift(); //unshift tam tersi .unshift(5,4, 'string');
x.shift();
console.log(x);

for (a of x){
    console.log(a);
}
*/
/*
var y = x.slice(1,5);
console.log(y);*/
/*
function find(val, index){
    return val > 3 || index == 1;
}

console.log(x.some(find)); // dizi uzunluğu kadar kontrol edilir
*/
/*
function sirala(a,b){
    return a-b;
}*/
var ary = [2,4,9,6,12,0,7]
//ary.sort(sirala);
//console.log(ary);
/*

ary.splice(1, 0, 6);// 2.parametre kaç tane elemanın kaldırılacağı değer 
console.log(ary);*/

ary.join("");
ary.toString();
console.log(ary, typeof(ary));

if (generator.start()){
    console.log('İşlem Başladı');
}

if (generator.stop()){
    process.exit(0);
}