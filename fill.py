"""
Füllfarbe

Die Funktionen width() und height() liefern die Breite/Höhe der Fläche.
"""

newPage("A4Landscape")

rect(0, 0, width(), height())

fill(1, 0, 0)

oval(0, 0, 500, 500)

"""
Mit der Funktion fill() stellst du die Füllfarbe ein. Ohne Angabe ist sie immer schwarz.

fill(0) # schwarz
fill(1) # weiss
fill(0.5) # grau
fill(random()) zufällige Graustufe
fill(1, 0, 0) rot
fill(1, 0, 1) rot/blau gemisch

- Kannst du Blau als Hintergrundfarbe  einstellen?
"""