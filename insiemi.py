print("********INSIEMI************")

l1=['a','b','c','d','e']
l2=['b','c','f','g']
l3=['b','f']

# ottengo insiemi a partire da liste
s1 = set(l1)
s2 = set(l2)
s3 = set(l3)

s4 = (s1|s2) #unione di s1 e s2  
s5 = s4-s3 #escludo dall'unione gli elementi di s3
print("s1:",s1)
print("s2:",s2)
print("s3:",s3)
print("s4:",s4)
print("s5:",s5)

###########################
str1 = "La capra è sotto La panca ma ha molta fame"
str2 = "La capra ha mangiato il cavolo nell'orto"
str3 = "La capra è sopra La panca"

l1 = str1.split()
l2 = str2.split()
l3 = str3.split()

set1 = set(l1)
set2 = set(l2)
set3 = set(l3)

print("set1=",set1)
print("set2=",set2)
print("set3=",set3)

set4 = set1 & set2 & set3 #intersezione dei 4 insiemi
print("set4=",set4)

set5 = (set1-set2-set3)|(set2-set1-set3)|(set3-set1-set2) #elementi unici in ognuno dei 3 insiemi
print("set5=",set5)