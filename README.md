# Buffer-Overflow-Notes
1 -  İlk önce kali üzerinde bulunan <b>generic_send_tcp</b> komutunu kullanarak ve bir spike dosyası oluşturarak, hizmetteki herhangi bir komutta buffer overflow olup olmadığını kontrol edecek  bir istek gönderiyoruz.

"generic_send_tcp" Kali'de buffer overflow fuzzing için kullanılır. Sunucular içindir ve bir <b>"spike"</b> dosyasına ihtiyaç duyar. 

Spike dosyası kod listesidir. Programın hangi komut veya instruction üzerine fuzzing deneyeceğini belirlemek için yazılır. Basit bir dildir.<br>
Örneğin:<br>
```
s_readline();
s_string("STATS ");
s_string_variable("A");
```
Örnek komut:
```
generic_send_tcp 10.0.2.15 9999 fuzz.spk 0 0
```
Sunucu çöktükten ve çöktüğüne emin olduktan sonra nerde çökertebildiğimizi bulabilmek için <b>Manual Fuzzing</b> yapmamız gerekmekte.
1. Adım için paylaştığım kodu düzenleyip çalıştırdıktan sonra sunucu çöktüğünde CTRL+C yapıyoruz. Ve bize "<b>tahminen</b>" nerede çöktüğünü gösteriyor. Değerleri kod içerisinde sürekli 100 ile arttırdığımız için kesin bir yer bulması mümkün değil. Bunun için bir sonraki adımageçiyoruz.
NOT: Kodların içindeki TRUN örnektir. Her binary ve server için değişkenlik gösterir.

2 <b>-/usr/share/metasploit-framework/tools/exploit/pattern_create.rb</b> -> Fuzzing ile kaç karakterde çöktüğünü bulduktan sonra o değere yakın bir değerde pattern üretmek için.

Çöken değere yakın bir değer ile bir pattern üretiyoruz.  Eğer 2300de çöktüysek,
```
./pattern_create.rb -l 2500
```
Pattern'i 2. adımdaki kod ile gönderiyoruz.  Sunucu çöktükten sonra, Debugger üzerinde EIP'ye yazılan karakterlerin hex değerlerini not ediyoruz.

3 -```└─# ./pattern_offset.rb -l 2500 -q 386F4337```
"-l" değeri payload'ın uzunluğu, "-q" değeri EIP'ye yazılan değer.

Çıktıdan kaçıncı karakterde çöktüğünün bilgisini alıyoruz.

4 - Test: Paylaştığım kodda, çökerten karakter sayısı kadar "A", ve cidden yazılıp yazılmadığını denemek için 4 adet "B" gönderiyoruz. Hexadecimal üzerinde "42" olarak ifade edilen B değerinin Debugger'da EIP değerine yazıldığını görüyoruz.

#GDB
● disassemble main - look at the assembly code of the main function
 ● break *0x12345678 - set a breakpoint at address 0x12345678
 ● x 0x12345678 - examine/print the content of address 0x12345678
 ● x/xw 0x12345678 - print the content of address 0x12345678 as hex word
 ● x/s 0x12345678 - print the content of address 0x12345678 as a string
 ● run - run/restart the program you are debugging
 ● continue - continue execution after you stopped at a breakpoint
 ● quit - exit gdb
 
#General
HEAP

STACK
Yerel değişkenler, fonksiyonlar içerisinde yapılan işlemler kaydedilir. Ram kaç GB olursa olsun, işletim sisteminin mimarisine göre belirli bir yer ayrılır. Stack bu limiti aşamaz. 

DATA
Global değişkenler ve statik değişkenler kaydedilir. Yaşam döngüsüne bağlı kalmayan değişkenlerdir.

TEXT
Assembly Instructions

int x; -> Local Değişken, Stack
int *y;
(int*)malloc(sizeof(int)); -> Heapte bir yer aç ve adres ata. Stack içerisinde sadece adresi tutulur. malloc yer ayırma fonksiyonudur. sizeof int'in boyutunu alır ve malloc ile int'in boyutu kadar bir yer ayırır.

Extended Stack Pointer
Buffer
Extended Base Pointer
Extended Instruction Pointer -> SCOPE
