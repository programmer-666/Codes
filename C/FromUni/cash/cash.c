/*
    # Cash Program #
    +Cash is a basic money transfer program.
*/
#include <stdio.h>
#include <stdlib.h>
// Prototypes
char controll(float *arg);
float send(float *arg, float val);
// Prototypes
// Globals
float tlost = 0;
// Globals
int main(){
    float *wallet[3]; // 4 wallets
    *wallet[0] = 32.322;
    *wallet[1] = 31.3;
    *wallet[2] = 44;
    *wallet[3] = 12.922;
    return 0;
}
// Functions
char controll(float *arg){
    /* Wallet Money Controll Function */
    if(*arg < 20)
        return -1;
    return 1;
}
float send(float *arg, float val){
    if(controll(arg)){
        tlost+=val;        
        return *arg-val;
    }
}
// Functions