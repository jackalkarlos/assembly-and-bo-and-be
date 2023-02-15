## ASSEMBLY AND BINARY EXPLOITATION
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
