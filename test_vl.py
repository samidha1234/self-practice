my_dicy= {1:'a',2:'b',3:'c'} 
k=list(my_dicy.keys())
v=list(my_dicy.values())
out_dic={}
for i in range(0,len(my_dicy)):
    out_dic[v[i]]=k[i]
print(out_dic)
print(out_dic['c'])

# status code
# Mohan patil
# a function 1 return 
#              return None