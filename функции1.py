def show_text():
    print("""Don't compare yourself with anyone in this world…
if you do so, you are insulting yourself.
Bill Gates""")

show_text()

def show_range(a,b):
    if a>b: a,b=b,a
    for i in range(a,b+1):
        print(i,end="  ")

show_range(4,1)
print('\n')
def show_square(len,sym,bool):
    if bool==True:
        for i in range(len):
            print(sym*len)
    elif bool==False:
        for i in range(len):
            for j in range(len):
                if i==0 or j==0 or (i ==len-1) or (j==len-1):
                    print(sym,end="")
                else:
                    print("",end=" ")
            print("")

show_square(6,"*",False)

