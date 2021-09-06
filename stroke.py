"""
Linienfarbe

Die Funktion stroke() stellt die Linienfarbe ein.
"""

newPage(1000, 1000)

fill(None)
stroke(0, 0, 1)

strokeWidth(2)

line((0, 0), (width(), height()))
oval(100, 100, 800, 800)

"""
Mit dem Wert "None" als Argument von fill() oder stroke() kannst du eine Farbe «abschalten».
"""
