"""
Random Starry Sky

"""
size(300,300)

fill(0)
rect(0,0,300,300)

for i in range (200):
    dia = random()*3
    fill(random())
    oval(random()*300,random()*300,dia, dia)
    
    
    
"""
Aufgabe: 
    - Platziere ein paar zufällig farbige Planeten am Nachthimmel
    
Bemerkung: 
    - random() liefert einen Wert zwischen 0.0 und 1.0, bsp. 0.32123...

"""
    
    