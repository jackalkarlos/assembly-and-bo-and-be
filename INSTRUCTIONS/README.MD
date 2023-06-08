## push -> Yığına Ekleme. (Genelde Ekrana Yazdırma İçin Kullanılıyor.):
```
mov eax, "I will print it"
push eax
```
## mov -> Veri Kopyalama.
```
mov eax, "Move me!"; move me stringi eax'a taşındı
mov ebx, eax; eax içindeki değer ebx'e taşındı
```
## cmp -> Karşılaştırma (boolean)
```
mov eax, 1
mov ebx, 1
cmp eax, ebx; true
```
## add -> Ekleme.
```
mov eax, 1
add eax, 1
add eax, 1; eax artık 3
```
## sub -> Çıkarma.
```
mov eax, 1
sub eax, 1; eax artık 0
```
## jl -> Asıl değer karşılaştırılan değerden küçükse atlama yapar.
```
mov eax, 5
mov ebx, 10
cmp eax, ebx
jl jumpmebabe ; Eğer eax, ebx'den küçükse atlama yap
```

jle -> küçük eşit
jg -> büyüktür
jge -> büyük eşit
je ve jz -> eşitse
jo -> overflow varsa
jno -> overflow yoksa
Jump if Carry (jc): Taşıma (carry) durumu olduğunda atlama yapar.
Jump if No Carry (jnc): Taşıma (carry) durumu olmadığında atlama yapar.
Jump if Sign (js): İşaret (negative) durumu olduğunda atlama yapar.
Jump if No Sign (jns): İşaret (negative) durumu olmadığında atlama yapar.
Jump if Parity (jp veya jpe): Çiftlik (parity) durumu olduğunda atlama yapar.
Jump if No Parity (jnp veya jpo): Çiftlik (parity) durumu olmadığında atlama yapar.
