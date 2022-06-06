Z=[]
k=[]
def Fun(inp):
    st=[]
    for i in range (len(inp)):
        st.append(chr(ord(inp[i])))
    return(''.join(st))
def FuN(inp):
    for i in range(len(inp)):
        if(i<11):
            Z.append(chr(ord(inp[i])+3))
            print(Z)
        else:
            Z.append(chr(ord(inp[i])+2))
            print(Z)     
    return(''.join(Z))

X=input("Enter input:")
k=FuN(Fun(X))
print(k)



# flag = "z3z$K|bs|:k2part2it6oo5t"