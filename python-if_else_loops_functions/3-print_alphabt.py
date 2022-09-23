#!/usr/bin/python3
for alpha_letters in range(97, 123):
    if alpha_letters in [101, 113]:
        continue
    print("{}".format(chr(alpha_letters)), end="")
