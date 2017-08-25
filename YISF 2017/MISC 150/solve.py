data = open('C:/test/encoded_flag.txt', 'rb').read()

flag = []
for i in range(20):
    flag.append(chr(ord(data[i])^52))


for i in range(5):
    flag[i] = (chr(ord(flag[i])-0x10))

for i in range(5, 10):
    flag[i] = (chr(ord(flag[i])+0x20))

for i in range(10, 15):
    flag[i] = (chr(ord(flag[i])/0x2))

for i in range(15, 20):
    flag[i] = (chr(ord(flag[i])^0xaa))

print ''.join(flag)
