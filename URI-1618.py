n = int(input())
x = []

for i in range (n):

    s = input()
    
    ax, ay, bx, by, cx, cy, dx, dy, rx, ry = (int(x) for x in s.split())

    if (rx >= ax and rx <= bx and rx >= dx and rx <= cx and ry >= ay and ry <= dy and ry >= by and ry <= cy):
        print("1")
    else:
        print("0")