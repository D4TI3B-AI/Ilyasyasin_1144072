import time
start_time = time.time()
print('menghitung nilai ( angka1 - angka2 ) - ( angka3 * angka4')
a = raw_input('masukan angka A : ')
b = raw_input('masukan angka B : ')
c = raw_input('masukan angka C : ')
d = raw_input('masukan angka D : ')

if a == 'hiji':
	a=1
if a == 'dua':
	a=2
if a == 'tilu':
	a=3
if a == 'opat':
	a=4
if a == 'lima':
	a=5	
if a == 'genep':
	a=6
if a == 'tujuh':
	a=7
if a == 'dalapan':
	a=8
if a == 'salapa':
	a=9
if a == 'enol':
	a=0

if b == 'hiji':
	b=1
if b== 'dua':
	b=2
if b == 'tilu':
	b=3
if b == 'opat':
	b=4
if b == 'lima':
	b=5	
if b == 'genep':
	b=6
if b == 'tujuh':
	b=7
if b == 'dalapan':
	b=8
if b == 'salapa':
	b=9
if b == 'enol':
	b=0	

if c == 'hiji':
	c=1
if c== 'dua':
	c=2
if c == 'tilu':
	c=3
if c == 'opat':
	c=4
if c == 'lima':
	c=5	
if c == 'genep':
	c=6
if c == 'tujuh':
	c=7
if c == 'dalapan':
	c=8
if c == 'salapa':
	c=9
if c == 'enol':
	c=0	

if d == 'hiji':
	d=1
if d== 'dua':
	d=2
if d == 'tilu':
	d=3
if d == 'opat':
	d=4
if d == 'lima':
	d=5	
if b == 'genep':
	d=6
if d == 'tujuh':
	d=7
if d == 'dalapan':
	d=8
if d == 'salapa':
	d=9
if d == 'enol':
	d=0	

jumlah = (a - b) / (c * d)
print('hasil penjumlahan',jumlah)
print("time : %s detik " % (time.time() - start_time))




