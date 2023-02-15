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
BYTES: Byte'lar, 8 bitten oluşurlar. İlk görselde EAX'ın önce 16 bit olarak AX'a sonrasında, 8 bit olarak AL ve AH'ye bölünebildiğinden bahsetmiştik. AL ve AH 8 bittir. <br>
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

<b>NOT: "mov ecx, eax" talimatı, eax kaydındaki değeri doğrudan ecx kaydına kopyalar, mov ecx, [eax] talimatı ise eax kaydının gösterdiği bellek adresindeki değeri ecx kaydına kopyalar.</b><br>

![image](https://user-images.githubusercontent.com/88983987/219168433-d3bfc301-7f0b-4e5d-8bc6-33c4990d10e0.png)

<br>
Benzer bir MOV hareketinin Pseudo C kodu:

![image](https://user-images.githubusercontent.com/88983987/219170624-f4a716ec-ab28-4cc2-91be-ffb582655420.png)

Parantez içinde belirtilen (örn: mov ecx, [eax]) talimatlar, kaydın kendi değerini değil, kaydın gösterdiği bellek adresindeki değeri kopyalar.

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
