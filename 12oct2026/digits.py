words = "hello world @123"
d = 0
for i in words:
    if i.isdigit():
        d = d+1
print(d)