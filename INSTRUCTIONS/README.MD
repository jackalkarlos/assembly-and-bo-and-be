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
jl jumpmebabe ; Eğer eax, ebx'den küçükse atlama yap. Küçük olduğu için atlama gerçekleşecektir.
```

## jle -> Asıl değer karşılaştırılan değerden küçükse veya eşitse atlama yapar.

```
mov eax, 10
mov ebx, 10
cmp eax, ebx
jle ohnobabeijumped ; Eğer eax, ebx'den küçük veya eşitse atlama yap. Eşit olduğu için atlama gerçekleşecektir.
```

## jg ->  Asıl değer karşılaştırılan değerden büyükse atlama yapar.
```
mov eax, 15
mov ebx, 10
cmp eax, ebx
jg areyoujumpingdaddy ; Eğer eax, ebx'den büyükse atlama yap. Büyük olduğu için atlama gerçekleşecektir.
```

## jge -> Asıl değer karşılaştırılan değerden küçükse veya eşitse atlama yapar.
```
mov eax, 10
mov ebx, 10
cmp eax, ebx
jge becareful ; Eğer eax, ebx'den büyükse veya eşitse atlama yap. Eşit olduğu için atlama gerçekleşecektir.
```

## je, jz -> Her iki instructionda eğer değerler eşitse atlama yapar.
```
mov eax, 10
mov ebx, 10
cmp eax, ebx
je okokok ; Eğer eax, ebx eşitse atlama yap. Eşit olduğu için atlama gerçekleşecektir.
```
```
mov eax, 10
mov ebx, 10
cmp eax, ebx
jz okokok ; Eğer eax, ebx eşitse atlama yap. Eşit olduğu için atlama gerçekleşecektir.
```
## jo -> Eğer overflow varsa atlama yap.
```
mov eax, 2
add eax, 2147483647
jo wtfdaddyareuoverflowing ; Integer overflow meydana geldiği için atlama gerçekleşecektir.
```
## jno -> Overflow yoksa atlama yap.
```
mov eax, 1
add eax, 2
jno label ; Overflow olmadığı için atlama gerçekleşecektir.
```
Jump if Carry (jc): Taşıma (carry) durumu olduğunda atlama yapar.
Jump if No Carry (jnc): Taşıma (carry) durumu olmadığında atlama yapar.
Jump if Sign (js): İşaret (negative) durumu olduğunda atlama yapar.
Jump if No Sign (jns): İşaret (negative) durumu olmadığında atlama yapar.
Jump if Parity (jp veya jpe): Çiftlik (parity) durumu olduğunda atlama yapar.
Jump if No Parity (jnp veya jpo): Çiftlik (parity) durumu olmadığında atlama yapar.
