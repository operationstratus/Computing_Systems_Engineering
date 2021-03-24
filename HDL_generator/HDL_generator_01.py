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


# Mux4Way16
for i in range(16):
    print(f"//Mux4Way abcd bit {i}")
    print(f"Mux(a=a[{i}], b=b[{i}], sel=sel[0]], out=Muxab{i});")
    print(f"Mux(a=d[{i}], b=c[{i}], sel=sel[0]], out=Muxdc{i});")
    print(f"Mux(a=Muxab{i}, b=Muxdc{i}, sel=sel[1]], out=out[{i}]);\n")
