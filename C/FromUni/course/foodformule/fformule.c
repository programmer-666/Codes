#include <stdio.h>
#include <stdlib.h>
#include <math.h>


void main(){
    unsigned char b = 3, o = 2, O = 2, l = 2, k = 1, a = 3, d = 2, z = 3, m = 3, h = 2;

    float foodpoint = pow( ((((pow(b, 3)+pow(O, 3)+pow(l, 2))/(pow(3, (1/b*O*l))))*((pow(z, 4)+pow(m, 3)+pow(h, 4)+pow(d, 5))/(pow(4, (1/z*m*h*d)))))*pow(k, 3)*pow(o, -1)), -0.1);
    printf("%f", foodpoint);
    /*
    b - Yemek cesidi
    o - Yag orani
    O - Tipi
    l - Tadi
    k - Kokusu
    a - Agizda biraktigi his
    d - Pisme orani
    z - Aci orani
    m - Malzeme orani
    h - Hamur orani
    */
}