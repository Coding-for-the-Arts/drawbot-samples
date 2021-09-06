"""
Text

Mit der Funktion text() kannst du Text schreiben.
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

DrawBot hat kann gut mit Text umgehen.
Wenn du mehr zu den möglichen Einstellungen im Zusammenhang mit Text/Fonts wissen möchtest, findest du in der Dokumentation viel Infos:
drawbot.com/content/text.html
"""