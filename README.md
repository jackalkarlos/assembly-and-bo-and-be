# Buffer-Overflow-Notes
1 -  İlk önce <b>generic_send_tcp</b> komutunu kullanarak ve bir spike dosyası oluşturarak port'a doğrudan komutu çökertip çökertemediğimize dair bir komut gönderiyoruz.

"generic_send_tcp" Kali'de buffer overflow fuzzing için kullanılır. Serverler içindir. Spike dosyasına ihtiyaç duyar. 

Spike dosyası örnek bir kod listesidir.
örneğin:
s_readline();
s_string("STATS ");
s_string_variable("A");

Çökertebildiğimize emin olduktan sonra nerde çökertebildiğimizi bulabilmek için <b>Manual Fuzzing</b> yapmamız gerekmekte.
1. Adım için paylaştığım kodu çalıştırdıktan sonra sunucu çöktüğünde CTRL+C yapıyoruz. Ve bize nerede çöktüğünü gösteriyor. Fakat değerleri sürekli 100 ile arttırdığımız için kesin bir yer bulması mümkün değil. Bunun için 2. adıma geçiyoruz.
NOT: Kodların içindeki TRUN örnektir. Her binary ve server için değişkenlik gösterir.

2 <b>-/usr/share/metasploit-framework/tools/exploit/pattern_create.rb</b> -> Fuzzing ile kaç karakterde çöktüğünü bulduktan sonra o değere yakın bir değerde pattern üretmek için.

Çöken değere yakın bir değer ile bir pattern üretiyoruz.  Eğer 2300de çöktüysek,

<b>./pattern_create.rb -l 2500</b>

Pattern'i 2. adımdaki kod ile gönderiyoruz.  Debugger üzerinde EIP'ye yazılan karakterleri not ediyoruz.

3 - <b>└─# ./pattern_offset.rb -l 2500 -q 386F4337</b>
"-l" değeri payload'ın uzunluğu, "-q" değeri EIP'ye yazılan değer.

Çıktıdan kaçıncı karakterde  çöktüğünün bilgisini alıyoruz.

4 - Test: Paylaştığım kodda, çökerten karakter sayısı kadar "A", ve cidden yazılıp yazılmadığını denemek için 4 adet "B" gönderiyoruz. Hexadecimal üzerinde "42" olarak ifade edilen B değerinin Debugger'da EIP değerine yazıldığını görüyoruz.
