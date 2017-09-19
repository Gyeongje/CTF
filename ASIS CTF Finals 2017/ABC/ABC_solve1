import hashlib

c = 0
for i in range(2):
    for j in range(c, 65535):
        h = "%04x" % j
        sha = hashlib.sha1(h).hexdigest()
        if sha[0:4] == h:
            print "str%d = " % (i + 1) + h
            c = j + 1
            break

# result = 57d9 b53a
