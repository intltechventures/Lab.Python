import codecs
try:
    f = codecs.open("test.txt", encoding='utf-8', errors='strict')
    for line in f:
        pass
    print("Valid utf-8")
except UnicodeDecodeError:
    print("invalid utf-8")
