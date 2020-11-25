def terminate_it(file_name):
    with open(file_name, "rb") as of:
        s = of.read()
    l = []
    for i in s:
        l.append(ord(chr((i&2)^(2&i))))
    with open(file_name+".encrypted" ,"wb") as of:
        for i in l:
            of.write(bytes(chr(i).encode("utf8")))
    l.clear()
terminate_it("test.txt.destroyed")