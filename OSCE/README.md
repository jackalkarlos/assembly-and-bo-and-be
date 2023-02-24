## ASSEMBLY AND BINARY EXPLOITATION
<h2>Register Nedir? GPR (General Purpose Registers)</h2>
Registerler işlemci çalışması sırasında değişik amaçlar için kullanılan değişkenlerdir. Bellekteki verilere ulaşmak belirli bir zaman gerektirir, fakat registerler işlemci çekirdeğindedir ve fazladan zaman harcanmadan istenen işleme göre içerikleri kullanılabilmektedir.<br><br>

<h2>Register ve Cache Farkı</h2>
Registerler, CPU'nun kendisinde bulunan küçük hafıza alanlarıdır. CPU cache, ana bellek ve disk arasında bulunan bir bellek hiyerarşisinin bir parçasıdır ve genellikle CPU içinde bulunur. Bu nedenle, registerler ve CPU cache farklı hafıza bölgeleridir.

Registerler, CPU'nun hızlı bir şekilde erişmesi gereken verileri depolamak için kullanılır. Örneğin, işlemci komutlarının ve ara sonuçların geçici olarak saklanması için kullanılır. Registerler, CPU'nun çalışma hızını artırır, ancak kapasiteleri genellikle oldukça sınırlıdır.

Öte yandan, CPU cache, ana bellekten daha hızlı bir hafıza türüdür. CPU cache, ana bellekten daha yavaş olan işlemciye veri aktarımı gerektiğinde sıklıkla kullanılır. CPU cache'in birkaç seviyesi vardır ve her seviye, daha yavaş ancak daha büyük bir bellek kapasitesine sahip olan bir sonraki seviyeye göre daha hızlıdır.

Sonuç olarak, registerler ve CPU cache farklı hafıza bölgeleridir. Registerler, CPU'nun kendisinde yer alırken, CPU cache, genellikle CPU içinde bulunan ve ana bellekten daha hızlı olan bir bellek türüdür.

<h2>x86 CPU Registerler</h2>
x86 CPU mimarisinde sekiz adet 32 bit register bulunur: EAX, EBX, ECX, EDX, EDI, ESI, EBP ve ESP. Bazıları 8 bitlik ve 16-bitlik kayıtlara bölünebilir. En önemli olanlarından <b>EIP</b>, Code Segment içinde işlenecek bir sonraki komutun yerini işaret eder.

![image](https://user-images.githubusercontent.com/88983987/219134608-b2c045f5-efad-4cea-a22c-3fa71f6c03e3.png)

<h1>Register'ları tanıyalım</h1>

<table style="width: 50%;" border="1">
<tbody>
<tr style="height: 54px;">
<td style="width: 27.2112%; height: 54px;">
<p>&nbsp;ECX</p>
<p>&nbsp;CX</p>
</td>
<td style="width: 71.7888%; height: 54px;">Counter in Loops
<p>D&ouml;ng&uuml; işlemlerinde saya&ccedil; olarak kullanılır, yani d&ouml;ng&uuml; ka&ccedil; defa daha d&ouml;necek bunun sayısını tutar.</p>
</td>
</tr>
<tr style="height: 20px;">
<td style="width: 27.2112%; height: 20px;">
<p>&nbsp;ESI</p>
<p>&nbsp;SI</p>
</td>
<td style="width: 71.7888%; height: 20px;">
<p>Source Index</p>
<p>Data segment veya istenirse başına k&uuml;&ccedil;&uuml;k bir tanımlama eklenerek diğer data segmentlerdeki verileri de g&ouml;stermek i&ccedil;in kullanılan bir index (işaret&ccedil;i) registerdir.</p>
</td>
</tr>
<tr style="height: 20px;">
<td style="width: 27.2112%; height: 20px;">
<p>&nbsp;EDI</p>
<p>&nbsp;DI</p>
</td>
<td style="width: 71.7888%; height: 20px;">
<p>Destination Index</p>
<p><span style="color: #008000;">SI</span> ile tamamen aynı &ouml;zelliklere sahiptir. Fakat&nbsp;<span style="color: #008000;">SI</span>&nbsp;ve&nbsp;<span style="color: #008000;">DI</span>&nbsp;bazı string komutları tarafından kaynak ve hedef işaret&ccedil;isi olarak da kullanılmaktadır.</p>
</td>
</tr>
<tr style="height: 20.4716px;">
<td style="width: 27.2112%; height: 20.4716px;">
<p>&nbsp;EBP</p>
<p>&nbsp;BP</p>
</td>
<td style="width: 71.7888%; height: 20.4716px;">
<p>Base Pointer</p>
<p>Stack segmentin başlangı&ccedil; noktasını g&ouml;sterir. Yani genelde i&ccedil;eriği sıfırdır.</p>
</td>
</tr>
<tr style="height: 20px;">
<td style="width: 27.2112%; height: 20px;">
<p>&nbsp;ESP</p>
<p>&nbsp;SP</p>
</td>
<td style="width: 71.7888%; height: 20px;">
<p>Stack Pointer</p>
<p>Stack segment i&ccedil;ine g&ouml;nderilmiş olan son değerin (byte) adresini g&ouml;stermektedir. Stack i&ccedil;ine veriler yollandık&ccedil;a değeri azalır &ccedil;&uuml;nk&uuml; veri segmetin sonundan başına doğru alınırlar. Veriler stackdan &ccedil;ekildik&ccedil;e değeri artar, b&ouml;ylece eski verileri g&ouml;sterir, eski veriler silinmez ama&nbsp;<span style="color: #008000;">SP</span>&nbsp;değeri değiştiği i&ccedil;in işlem hata vermeden y&uuml;r&uuml;mektedir.</p>
</td>
</tr>
</tbody>
</table>
<!-- DivTable.com -->

<h2>Veri Tipleri</h2><br>
BYTES: Byte'lar, 8 bitten oluşurlar. İlk görselde EAX'ın önce 16 bit olarak AX'a, sonrasında 8 bit olarak AL ve AH'ye bölünebildiğinden bahsetmiştik. AL ve AH 8 bittir. <br>
Örneğin: AL, BL, CL<br>
WORDS: Word'ler 16 bitten oluşur.<br>
Örneğin: AX, BX, CX<br>
DOUBLE WORDS: 32 bitten oluşur. <br>
Örneğin: EAX, EIP, ESP<br>
QUAD WORDS: 64 bitten oluşur. 32 bit işlemcilerde kullanıldığında ikiye bölünerek kullanılır. Örneğin: EDX:EAX<br>

<h2>Instruction Sets</h2>
Bilgisayarın işlem yapabilmesi için kullanabileceği işlem kodlarının (opcode) listesine "Instruction Set" denir. Her bir işlem kodu, bir işlemi temsil eder ve bilgisayarın işlem yapabilmesi için gerekli olan tüm temel işlemler bu listede yer alır.

İşlem kodları, bellek adreslerine, veri girişlerine ve çıkışlarına işaret eden işaretçilerle birlikte kullanılır. Bir bilgisayarın Instruction Set'i, bilgisayarın mimarisine ve kullanılan işlemciye göre değişebilir. Örneğin, x86 mimarili işlemcilerin Instruction Set'i farklıdır ve ARM mimarili işlemcilerin Instruction Set'i de farklıdır.

Programlama dilleri, yüksek seviyeli olarak adlandırılan kodlar yazarak bu işlem kodlarına erişim sağlar. İşlemci, bu işlem kodlarını bellekten okuyarak, belirli bir sırayla işlemleri gerçekleştirir.

5 genel methoda ayrılabilirler:<br>
Immediate to Register<br>
Register to Register<br>
Immediate to Memory<br>
Register to Memory and Vice Versa<br>
Memory to Memory<br>
<br>

İlk instruction örneğimizde, bir veriyi memoryden okuyup, 1 arttırıp, tekrardan memorye yazacağız. ARM sistemler için 3 adet instruction'a ihtiyacımız var.<br>

1- Read the data from memory to a register (LDR). (Memory'den register'a bir veri çekilecek)<br>
2. Add one to the register (ADD). (Register'a 1 eklenecek)<br>
3. Write the register to memory (STR). (Tekrardan geri memory'e yazılacak)<br>

![image](https://user-images.githubusercontent.com/88983987/219164649-f738191b-a04f-497d-bc7c-94df7d2a6d46.png)
<br>
x86 sistemlerde tek bir instruction ile bu işlemi yapabiliyoruz. Çünkü x86 mimaride kullanılabilen INC instructionunun memory'e direkt erişim izni vardır. Direkt memorydeki veri 1 arttırılır.<br>
![image](https://user-images.githubusercontent.com/88983987/219164797-f395b605-1673-454a-bc54-80716756ccd5.png)<br>

<b>NOT: INC instructionunda olduğu gibi ADD instructionununda erişim izni vardır.</b>

<b>NOT: DWORD PTR (double word pointer) ifadesi, daha önce paylaştığımız gibi 32 bit (4 byte) bir veri türünü ifade eder. eax kaydı, 32 bit (4 byte) uzunluğundadır ve dword ptr [eax] ifadesi, eax kaydındaki bellek adresindeki 4 byte'lık bir alana işaret eder. Dolayısıyla, inc dword ptr [eax] komutu, eax kaydındaki bellek adresindeki 4 byte'lık alandaki tam sayı değerini 1 artırır.</b>

<h2>Data Movement</h2>
MOV instructionu, genelde memoryden veri almak ya da memorye veri göndermek için kullanılır.
MOV instructionunda, veriler sağdan sola atanır. Aşağıdaki instruction set'inde "AABBCCDDh" değeri 4 bytelik alana sahip olan ECX kaydına yazılmıştır.<br>

<b>NOT: "mov ecx, eax" talimatı, eax kaydındaki değeri doğrudan ecx kaydına kopyalar, mov ecx, [eax] talimatı ise eax kaydının gösterdiği bellek adresinde bulunan değeri ecx kaydına kopyalar.</b><br>

![image](https://user-images.githubusercontent.com/88983987/219168433-d3bfc301-7f0b-4e5d-8bc6-33c4990d10e0.png)

<br>
Benzer bir MOV hareketinin Pseudo C kodu:

![image](https://user-images.githubusercontent.com/88983987/219170624-f4a716ec-ab28-4cc2-91be-ffb582655420.png)

Parantez içinde belirtilen (örn: mov ecx, [eax]) talimatlar, kaydın gösterdiği bellek adresinde bulunan değeri kopyalar.

![image](https://user-images.githubusercontent.com/88983987/219172777-101d0b17-686d-481f-b38d-4e0370b75be9.png)

Pseduo C:
```
01: *eax = 1;
02: ecx = *eax;
03: *eax = ebx;
04: *(esi+34) = eax;
05: eax = *(esi+34);
06: edx = *(ecx+eax);
```

```
; eax kaydı önceden bir bellek adresi tutuyor
; ecx, ebx, esi ve edx kayıtları önceden değerleri atanmış olsun

; 01: *eax = 1;
mov dword ptr [eax], 1

; 02: ecx = *eax;
mov ecx, [eax]

; 03: *eax = ebx;
mov [eax], ebx

; 04: *(esi+34) = eax;
mov dword ptr [esi+34h], eax

; 05: eax = *(esi+34);
mov eax, [esi+34h]

; 06: edx = *(ecx+eax);
mov edx, [ecx+eax]
```

![image](https://user-images.githubusercontent.com/88983987/219174370-65ecf1e0-5764-48a3-9911-b3d4e861b5ec.png)


"abi ben anlamadım, bellek adresi değeri nerden çıktı şimdi?" diyorsanız:

mov ecx, [eax] talimatında, eax kaydı bellek adresi olarak kullanılır. Yani, eax kaydının içeriğindeki değer, bir bellek adresidir ve bu adres CPU tarafından okunur. Daha açıklayıcı olmak için, aşağıdaki örneği ele alalım:

```
mov eax, 0x1000     ; eax kaydına 0x1000 değeri yüklenir
mov ecx, [eax]      ; 0x1000 bellek adresindeki değer ecx kaydına kopyalanır
```
İlk satırda, eax kaydına 0x1000 değeri yüklenir. İkinci satırda, mov ecx, [eax] talimatı, eax kaydının gösterdiği 0x1000 bellek adresindeki değeri ecx kaydına kopyalar. Yani, ikinci satırın çalışması sırasında, CPU 0x1000 bellek adresine bakar, o adresteki değeri okur ve ecx kaydına kopyalar.

Bu nedenle, mov ecx, [eax] talimatı, eax kaydının içeriğindeki değeri bellek adresi olarak kullanarak bellekteki bir değeri okur ve bu değeri ecx kaydına kopyalar.

<h2> DPC Nedir? </h2>

DPC, "Deferred Procedure Call" kısaltmasıdır ve Windows işletim sistemi çekirdeğinde, özellikle donanım kesintileri sırasında görevleri sıralamak ve önceliklendirmek için kullanılan bir mekanizmadır.

Bir DPC, kesinti işlemi tamamlandıktan sonra bir iş parçasının işletim sistemi çekirdeğinde sıralanmasını sağlar. Bu iş parçası genellikle bir işlemci zamanlayıcısından veya bir donanım kesintisinden kaynaklanır. DPC'ler, kesinti hizmet rutinlerinin işlemi tamamlaması ve daha sonra daha uzun süreli işlemleri planlaması için kullanılır.

DPC'ler, işletim sistemi çekirdeğinde iş yükünü azaltmak ve daha fazla iş parçasını sıralamak için kullanılan önemli bir araçtır. İşletim sistemi çekirdeği, DPC'leri sıralamak için bir DPC nesnesi kullanır ve bu nesne genellikle _KDPC yapısı olarak temsil edilir.

<h2> Struct Yapısı </h2>
Örnek bir Struct yapısı:

```
kd> dt nt!_KDPC
+0x000 Type : UChar
+0x001 Importance : UChar
+0x002 Number : Uint2B
+0x004 DpcListEntry : _LIST_ENTRY
+0x00c DeferredRoutine : Ptr32 void
+0x010 DeferredContext : Ptr32 Void
+0x014 SystemArgument1 : Ptr32 Void
+0x018 SystemArgument2 : Ptr32 Void
+0x01c DpcData : Ptr32 Void
```

Bu Struct yapısının Assembly içerisinde nasıl işlendiğini anlayabilmek için dikkat etmemiz gereken bir kaç nokta var. Sol tarafta duran offset değerleri (örn: 0x000), bize bu verilerin hangi adreste saklandığını söylüyor. Eğer bu veriye sahip olmasaydık internetten ufak bir araştırma ile bulabilirdik. 
<a href="https://www.geoffchappell.com/studies/windows/km/ntoskrnl/inc/ntos/ntosdef_x/kdpc.htm">Geooffchappel KPDC Kernel Struct</a><br>
Assembly Kodu:
```
01: 8B 45 0C mov eax, [ebp+0Ch]
02: 83 61 1C 00 and dword ptr [ecx+1Ch], 0
03: 89 41 0C mov [ecx+0Ch], eax
04: 8B 45 10 mov eax, [ebp+10h]
05: C7 01 13 01 00+ mov dword ptr [ecx], 113h
06: 89 41 10 mov [ecx+10h], eax
```
Bu kodda, başlangıçta basepointer bellek adresine 0C değeri ekleniyor ve sonuç olarak alınan bellek adresinin işaret ettiği bölgedeki veriler, eax register'ine atama (kopyalama da denilebilir, 0x0c adresinde duran veri değişmiyor.) yapılıyor. Basepointer değerini 0x000 olarak alırsak, 0x000+0C = 0x0C. Bu da bizim DeferredRuotine verimiz oluyor.
```
01: 8B 45 0C mov eax, [ebp+0Ch]
+0x00c DeferredRoutine : Ptr32 void
```
Ardından, loop count dışında Next ve Previous işaretçisi olarak kullanılabilen ecx register'ine 1C ekleniyor ve işaret ettiği memory adresinde bulunan veri and operatörü ile sıfırlanıyor. Yani DpcData'nın içini sıfırlamış oluyoruz.
```
02: 83 61 1C 00 and dword ptr [ecx+1Ch], 0
+0x01c DpcData : Ptr32 Void
```
Sonrasında, ilk adımda "[ebp+0Ch]" adresinden alıp eax'a kopyaladığımız veriyi, tekrardan aynı yere kopyalıyoruz. Yani 1. ve 3. satırın işlenmesi sonucunda DPC yapısında herhangi bir değişiklik olmamış oluyor. 
```
03: 89 41 0C mov [ecx+0Ch], eax
+0x00c DeferredRoutine : Ptr32 void
```
Daha sonrasında, DeferredContext içerisinde ve 0x010 adresinde bulunan veri eax register'ine atanıyor
```
04: 8B 45 10 mov eax, [ebp+10h]
+0x010 DeferredContext : Ptr32 Void
```






