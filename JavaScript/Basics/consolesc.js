if (2 == "2"){
    console.log(true);
}

if (2 === "2"){
    console.log(true);
}

var i = 0;
while (i < 10) {
    console.log(i);
    i+=1;
}

var i = 0;
do{
    console.log(i);
    i++;
}while(i < 3)

for (var i = 0;i < 10; i++) {
    console.log(i);   
}

var obj = {x: 3.14, y: 15, z: 22};
for (i in obj){
    console.log(i+" "+obj[i]);
} 

var ary = [1,2,3,6,9,0]
for (i of ary){
    console.log(i);
}

for (var i = 0;i<10;i++){
    if (i == 6){
        break;
    }
    console.log(i);
}

debugger;
console.log('end');