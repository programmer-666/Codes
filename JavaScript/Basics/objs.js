var firstObj = {
    id : 1,
    code : "0x3884",
    info_id : function (){
        return this.id;
    } 
};

firstObj.info_code = function(){
    return this.code;
};

console.log(firstObj.info_id(), firstObj.info_code(), firstObj['code']);

for (i in firstObj){
    console.log(i);
}

var secondObj = firstObj;
secondObj.id = 2; secondObj.code = "0x32b";
console.log(secondObj);

var arrowlambdalike = (x) => Math.pow(x, 2);

console.log(arrowlambdalike(2));

// new ile fonksiyonlar nesne olarak kullanılabilirler

function p2(x){
    this.xn = x;
}

var n = new p2(3);

console.log(n.xn);