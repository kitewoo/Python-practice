
pumMok=[['노트북/모니터/키보드','키보드/볼펜','사인펜/노트'],
        ['키보드/전자칠판','스케치북/노트북']]

a="/"
b=""
txt=[]

for i in pumMok:
    for j in i:
        for k in j:
            if k != a:
                b += k
            else:
                txt.append(b)
                b=""
        if len(b) != 0:
            txt.append(b)
            b=""

print(txt)