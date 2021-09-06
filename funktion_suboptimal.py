"""
Funktionen

Funktionen erkennst du an der Klammer an ihrem Ende. Beispiele: print(), random()
Du kannst auch deine eigenen Funktionen schreiben.
"""

def multiChar(c, n):
    # liefert eine Zeichenkette aus
    # n Wiederholungen des Zeichens l
     return c * n

print(multiChar(3, "A"))

print(multiChar(10, "ABC"))

print(multiChar(randint(0, 100), "Hello"))

"""
Fragen:
    - Was machen c und n?
    - Was macht "return"?

Challenge:
    - Kannst du … ?
    - Wie könntest du … ?
"""