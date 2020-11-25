#include <stdio.h>
int main(){
    printf("sayacin ilk okuma degerini giriniz:");int fr;scanf("%d", &fr);
    printf("sayacin ikinci okuma degerini giriniz:");int sr;scanf("%d", &sr);
    printf("Kullanim turunu giriniz:(Mesken:0,isyeri:1)");int typ;scanf("%d", &typ);
    if (typ == 1){
        printf("Kullanim turunuz Isyeri\nSarfiyatiniz..:%d Faturaniz..:%d", sr-fr, (sr-fr)*2);
    }else{
        int m = 1, n = sr-fr;
        for (int i = 0; i < sr-fr; i++){
            if (i <= 50){
                m+=1;
            }
            if (i > 50 && i < 100){
                m+=2;
            }
            if (i >= 100){
                m+=3;
            }
        }
        printf("Kullanim turunuz Mesken\nSarfiyatiniz..:%d Faturaniz..:%d", sr-fr, m);
    }
    return 0;
}
//19110011024