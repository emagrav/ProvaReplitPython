from turtle import Screen, Turtle

myWin = Screen()
uga = Turtle()

uga.pencolor("blue")
uga.forward(100)
uga.right(90)

uga.pencolor("red")
uga.forward(100) #traccia linea
uga.right(90) #ruota di 90°

uga.pencolor("blue")
uga.forward(100)
uga.right(90)

uga.pencolor("red")
uga.forward(100)
uga.right(90)

'''
uga.reset() #pulisce lo schermo, penna al centro e imposta le variabili ai valori predefiniti
uga.clear() #cancella lo schermo
tracerflag(bool) #abilita o meno la funzione di tracciatura che è più lenta con l'animazione della freccia
degrees() #imposta a gradi l'unità di misura degli angoli
radians() #imposta a radianti l'unità di misura degli angoli
up()
down()
fill(flag)
write(text[,move]) 
circle(radius[,extent])
goto((x,y))
'''
uga.clear()

uga.pencolor("blue")
uga.forward(100)
uga.right(60)

uga.pencolor("red")
uga.forward(100) #traccia linea
uga.right(60) #ruota di 90°

uga.pencolor("blue")
uga.forward(100)
uga.right(60)

uga.pencolor("black")
uga.forward(100)
uga.right(60)

uga.pencolor("green")
uga.forward(100)
uga.right(60)

uga.pencolor("purple")
uga.forward(100)
uga.right(60)

myWin.exitonclick()

############
start=Turtle()

for i in range(50):
  start.forward(50)
  start.right(100)

start.done()
