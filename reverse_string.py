Sample_String="LetsUpgrade"
Sample_List=[]
new=""
for i in Sample_String:
    Sample_List.append(i)
for j in Sample_List[-1::-1]:
    new+="".join(j)
print(new)