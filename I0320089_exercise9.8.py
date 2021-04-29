#Mengonversi list kedalam array.array
li = [10, 20, 30, 40, 50]
C = array.array('i')
C.fromlist(li)
type(C)
<type 'array.array'>
for nilai C:
    print("&d" % nilai, end='')