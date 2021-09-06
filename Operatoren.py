"""
Kannst du das Quadrat einmitten?

Tipp:
Die Funktionen width() und height() liefern die Höhe und Breite der Hintergrundläche.
"""

newPage("A4")

print("Breite:", width())
print("Höhe:", height())

posX = 0
posY = 0
side = 300

fill(1, 0, 0)
rect(posX, posY, side, side)

"""
Operatoren:
===========
+ Addition
- Subtraktion
* Multiplikation
/ Division, Resultat mit Kommastelle
// Division, ohne Rest (abgerundetes Resultat)
% Modulo: Rest der Division
"""
