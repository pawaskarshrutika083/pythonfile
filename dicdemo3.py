d={"a":10,"b":20,"c":50}
v=d.pop("b")
print(v)
print(d)

x=d.popitem()
print(d)

d1={"a":10,"b":20,"c":50,"d":70}
d2=d1
print(d1)
print(d2)
d1["x"]=32
print(d1)
print(d2)
d3=d1.copy()
d1["z"]=44
print(d1)
print(d2)
print(d3)