x=input().lower()
v=""

if "a" in x:
    v+="a" 
if "e" in x:
    v+="e"
if "i" in x:
    v+="i"
if "o" in x:
    v+="o"
if "u" in x:
    v+="u"
   
if v=="":
    print("none")
else:
    print(v)
