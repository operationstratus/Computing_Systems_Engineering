alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

'''
# Mux16
for i in range(16):
    print(f"Mux(a=a[{i}], b=b[{i}], sel=sel, out=out[{i}]);")
'''

'''  
# And16
for i in range(16):
    print(f"And(a=a[{i}], b=b[{i}], out=out[{i}]);")
'''    

'''
# Mux4Way16
for i in range(16):
    print(f"//Mux4Way abcd bit {i}")
    print(f"Mux(a=a[{i}], b=b[{i}], sel=sel[1], out=Muxab{i});")
    print(f"Mux(a=d[{i}], b=c[{i}], sel=sel[1], out=Muxdc{i});")
    print(f"Mux(a=Muxab{i}, b=Muxdc{i}, sel=sel[0], out=out[{i}]);\n")
'''

'''
# Add16
bits = 16
print("FullAdder(a=a[0], b=b[0], c=false, sum=out[0], carry=carry0);")
for i in range(1, bits):
    print(f"FullAdder(a=a[{i}], b=b[{i}], c=carry{i-1}, sum=out[{i}], carry=carry{i});")
'''

'''
#16BitRegister
bits = 16
for i in range(bits):
    print(f"Bit(in=in[{i}], load=load, out=out[{i}]);")
'''

'''
#Dmux8Way16:
bits = 2
ways = 8
inName = "in"
outName = "DmuxOut"
selName = "address"
code = ""
#alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(bits):
    code += f"DMux8Way(in={inName}[{i}], sel={selName}, "
    for j in range(2):
        var = alphabet[j].upper()
        code += f"{alphabet[j]}=DMuxOut{var}{i}" + (not j==ways-1)*", "
    code += ");\n"

print(code)
'''

'''
#RAM8
bits = 16
ways = 8
code = ""

code += "//DMux8Way för att skicka 'load'-signalen till det Register som ska vara mottaglig för ny data" + "\n"
code += "DMux8Way(in=load, sel=address, "
for j in range(ways):
    code += f"{alphabet[j]}=load{j}" + (not j == ways-1)*", "
code += ");" + "\n\n"

code += "//8x Register som får 'load'-signal från DMuxen\n"
for j in range(ways):
    code += f"Register(in=in, load=load{j}, out=out{j});" + "\n"


code += "\n" + "//Mux8Way16 för att adressen ska kunna välja utsignalen från rätt Register" + "\n" + "Mux8Way16("
for j in range(ways):
    code += f"{alphabet[j]}=out{j}, "
code += "sel=address, out=out);"

'''

'''#RAM
bits = 16
ways = 8
code = ""
subchip = "RAM4K" # vårt subchips som vi stackar i chipet
address_pins = 12

code += f"//DMux8Way för att skicka 'load'-signalen till det {subchip} som ska vara mottaglig för ny data\n"
code += "//OBS, vi delar upp 'address'-signalen i två delar:\n"
code += f"//De första tre bitarna går till DMux8Way för att 'load'-signalen ska till rätt {subchip}\n"
code += f"//De sista {address_pins-3} bitarna går till 'address'-pinnarna på varje {subchip}\n"
code += "DMux8Way(in=load, sel=address[0..2], "
for j in range(ways):
    code += f"{alphabet[j]}=load{j}" + (not j == ways-1)*", "
code += ");" + "\n\n"

code += f"//8x {subchip} som får 'load'-signal från DMuxen\n"
for j in range(ways):
    code += f"{subchip}(in=in, load=load{j}, address=address[3..{address_pins-1}], out=out{j});" + "\n"


code += "\n" + f"//Mux8Way16 för att adressen ska kunna välja utsignalen från rätt {subchip}" + "\n" + "Mux8Way16("
for j in range(ways):
    code += f"{alphabet[j]}=out{j}, "
code += "sel=address[0..2], out=out);"

'''

'''#RAM16K
bits = 16
ways = 4
code = ""
subchip = "RAM4K" # vårt subchips som vi stackar i chipet
address_pins = 14

code += f"//DMux{ways}Way för att skicka 'load'-signalen till det {subchip} som ska vara mottaglig för ny data\n"
code += "//OBS, vi delar upp 'address'-signalen i två delar:\n"
code += f"//De första 2 bitarna går till DMux{ways}Way för att 'load'-signalen ska till rätt {subchip}\n"
code += f"//De sista {address_pins-2} bitarna går till 'address'-pinnarna på varje {subchip}\n"
code += f"DMux{ways}Way(in=load, sel=address[0..1], "
for j in range(ways):
    code += f"{alphabet[j]}=load{j}" + (not j == ways-1)*", "
code += ");" + "\n\n"

code += f"//{ways}x {subchip} som får 'load'-signal från DMuxen\n"
for j in range(ways):
    code += f"{subchip}(in=in, load=load{j}, address=address[2..{address_pins-1}], out=out{j});" + "\n"


code += "\n" + f"//Mux{ways}Way16 för att adressen ska kunna välja utsignalen från rätt {subchip}" + "\n" + f"Mux{ways}Way16("
for j in range(ways):
    code += f"{alphabet[j]}=out{j}, "
code += "sel=address[0..1], out=out);"
'''
print(code)


















