#include <stdio.h>

int main(){
    FILE *test = fopen("test.data", "r");
    char *text;
    char buffer[32];
    char buffer2[32];
    char mem[16];
    int id = 1121;
    char *str = "deneme";
    setbuf(test, mem); // fopen veya freopen ile açılan dosyalar için varsayılan olarak atanan bir arabellek değeri vardır. bu fonksiyon sayesinde bu arabelleği programcı kendisi atayabilir.
    clearerr(test); // Belirtilen dosya ile ilgili hata ve EOF bilgilerini temizler.
    feof(test); // İmlecin sonda olup olmadığını kontrol eder.
    ferror(test); // Dosyaya yapılan son erişimde yapılan hata varsa sıfırdan farklıo değer döner.
    fflush(test); // FILE nesnesi w ile açılmışsa tampon verisini yazar ve temizler. R ile açılmışsa tamponu temizler.
    fwrite(str, sizeof(int), 1, test); // toplu yazıda kullanılır -> size_t fwrite(const void *tampon, size_t s, size_t n, FILE* f); // s sekizli n eleman
    //fgetc(test); // FILE nesnesinden veri okur. -> use with 'w'
    //fputc(65, test); // Karakter yazar. [i0] -> use with 'w'
    //fputc(66, test); // Karakter yazar. [i1] -> use with 'w'
    //fputs("this is a text", test); // -> use with 'w'
    //fread(buffer, 1, 3, test); // (depolanan, her nesnenin byte cinsinden boyutu, nesne sayısı, akış) -> veri okur 'r'
    //printf("%s\n", buffer);
    fscanf(test, "%s %s", buffer, buffer2); // boşluk gelene kadar okur
    printf("%s %s\n", buffer,  buffer2);
    fseek(test, 3, 0); // imleci öteler, 0 başlangıç, 1 bulunduğu yere göre, 2 sona göre
    printf("%d", ftell(test)); // imlecin bulunduğu konumu gösterir
    fclose(test); // Açılmış FILE nesnesini sonlandırır.
    rename("a.out", "aout");
    //remove("aout"); // siler
    return 0;
}