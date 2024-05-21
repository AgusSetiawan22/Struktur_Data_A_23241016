# tabel kebenaran (logika bolean)
# and or not xor

# NOT 
print("**********Logka Not*********")
x = False
y = not x 
print("nilai dari x =", x)
print("nilai dari y =", y)

# and (hanya bernilai benar, ketika keduanya benar)
# jika ada satu aja yang salah, makah salah
x = False
y = False
z = x and y
print(z)

x = False
y = True
z = x and y
print( x, "and" , y, "=", z)

x = True
y = False
z = x and y
print( x, "and" , y, "=", z)
x = True
y = True
z = x and y
print( x, "and" , y, "=", z)


# or 
print("\n**********logika or*********")
x = False
y = False
Z = x or y
print( x, "or" , y, "=", z)

x = True
y = False
Z = x or y
print( x, "or" , y, "=", z)

x = False
y = True
Z = x or y
print( x, "or" , y, "=", z)

x = True
y = True
print( x, "or" , y, "=", z)

