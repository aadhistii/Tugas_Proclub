'''
Nama    : Adhistianita Safira Husna
NIM     : 1301213039
Kelas   : IF-45-09
'''

print("\n=== Half Pyramid Pattern ===\n")

[print("* "*i) for i in range(1, 6)]

print("\n=== Half Inverted Pyramid Pattern ===\n")

[print("* "*i) for i in range(5, 0, -1)]

print("\n=== Half Pyramid Pattern Mirrored ===\n")

[print(("* "*i).rjust(10," ")) for i in range(1, 6)]

print("\n=== Full Pyramid Pattern ===\n")

[print(("* "*i).center(10," ")) for i in range(1, 6)]

print("\n=== Full Pyramid Pattern ===\n")

[print(("* "*i).center(10," ")) for i in range(5, 0, -1)]