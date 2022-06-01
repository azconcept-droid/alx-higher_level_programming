#!/usr/bin/python3
for i in range(0, 100):
    if i % 11 == 0 or i % 10 == 0 or i > 90 or i == 21:
        continue
    if (i > 80 and i < 89) or (i > 70 and i < 77):
        continue
    if (i > 60 and i < 67) or (i > 50 and i < 57):
        continue
    if (i > 40 and i < 44) or (i > 30 and i < 34):
        continue
    if i == 89:
        break
    print('{:02d}'.format(i), end=", ")
print("89")
