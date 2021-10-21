def somma(a,b):
  #prova
  x=a+1
  y=b+1
  return (x+y)

import dis
f=somma
dis.dis(f)
print(dis.code_info(f))