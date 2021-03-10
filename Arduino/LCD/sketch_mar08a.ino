#include <LiquidCrystal.h> // Kütüphane ekleme işlemini bu kodla yapmış oluyoruz.

LiquidCrystal lcd(12, 11, 5, 4, 3, 2); // kablo bağlantılarımızı programa



void setup() {

lcd.begin(16, 2); // LCDmize göre bir satır ve sütun sayısını gireceğiz. Genellikle LCD ekran 16x2 olur.

lcd.print("deneme"); // Ekranda gözükecek yazıyı buraya yazarız

}

void loop() {

lcd.setCursor(0, 1); // Yazı yazıldıktan sonra imlecimizi 2.satıra indirmiş olduk.

lcd.print(millis()/1000); // Programı ilk açtığımız süreden, şimdiye kadar geçen süreyi belirtir.

}
