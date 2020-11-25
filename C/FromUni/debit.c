#include <stdio.h>
#include <string.h>
short num_compartment_control(int num){if (num%10==0){return 1;}else{return 0;}}
int main(){
    char card[16];// = "4015201030105555";
    int cc[16];int total = 0;
    printf("Kart numarasini giriniz= ");scanf("%s", card);
    while (strlen(card) < sizeof(card)/sizeof(char)){printf("Az karakter tekrar giriniz=");scanf("%s", card);}
    for (register short i = 0; i < sizeof(card)/sizeof(char); i++){cc[i] = (short)card[i] - '0';}
    for (register short x = 0; x < sizeof(cc)/sizeof(short); x++){switch (x%2){case 0:total+=cc[x]*2;break;default:total+=cc[x];break;}}
    if(cc[0] == 4){printf("VISA ");}else if (cc[0] == 5){printf("MASTER ");}
    if(num_compartment_control(total) == 1){printf("Kart GECERLI");}else{printf("KART GECERSIZ");}
    return 0;
}
//printf("%d", (*scc+1)+1);