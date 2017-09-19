import hashlib

s = '69fc8b9b1cdfe47e6b51a6804fc1dbddba1ea1d9'
bf_table = "0123456789ABCDEFGHjJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$^*():_-<>?{}"

for a in bf_table:
    for b in bf_table:
        for c in bf_table:
            for d in bf_table:
                sha = hashlib.sha1('9' + a + b + c + d + 'b').hexdigest()
                if sha == s:
                    print '9' + a + b + c + d + 'b'
                    exit(1)
# 9:-*)b
