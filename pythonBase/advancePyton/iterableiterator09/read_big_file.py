def readline(f, newline):
    buf = ""
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline):]
        chunk = f.read(4096 * 10)
        if not chunk:
            yield buf
            break
        buf += chunk


with open("index.txt") as f:
    for line in readline(f, "{|}"):
        print(line)
