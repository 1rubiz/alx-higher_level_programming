#!/usr/bin/python3
for i in range(0, 99):
    if i < 10:
        print(f"0{i} = {hex(i)}")
    else:
        print(f"{i} = {hex(i)}")
