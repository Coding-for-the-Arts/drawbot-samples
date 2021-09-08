"""
Text
"""

newPage("A4")

font("Hobeaux-Bold")
# OT-Features des gewählten Fonts auflisten
print(listOpenTypeFeatures(fontNameOrPath=None))
fontSize(100)
openTypeFeatures(ss02=True) # alternatives y
text("Python FTW", (40, 400))

"""
- Kannst du deinen Namen mit deiner Lieblingsschrift schreiben?

Wenn du mehr über die Möglichkeiten mit Text/Fonts
in DrawBot wissen möchtest, findest du in der
Dokumentation weitere Infos: drawbot.com/content/text.html
"""