import os


def file_search(filename, a):
    f1 = open(filename, 'rb')
    f2 = open("C:/sum/%d" % a + '.png', 'wb')
    for j in range(0, os.path.getsize(filename)):
        data = f1.read(1)
        f2.write(data)
    f1.close()
    f2.close()

if __name__ == "__main__":
    # a = ["덽NG", "IEND췇`", 0]
    for i in range(100,778):
        filename = "C:/!!!Broken_PNG/%d/%d" % (i, i) +'.png'
        file_search(filename, i)
        '''c = 1
        check = 0
        a = [0, 0]
        while (1):
            filename = "C:/!!!Broken_PNG/%d/%d" % (i, c)
            f = open(filename, 'rb')
            data = f.read()
            if (data.find("PNG") > -1) and (check == 0):
                a[0] = c
                c = 0
                check = 1
                file_search(filename, i)
            elif ((data.find("IEND") == -1) and (a[0] != c)) and check == 1:
                a[1] = c
                c = 0
                check = 2
                file_search(filename, i)
            elif (data.find("IEND") > -1) and (check == 2):
                file_search(filename, i)
                f.close()
                break
            c += 1'''
