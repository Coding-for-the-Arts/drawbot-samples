newPage(1000, 1000)

dia = 100

for yFactor in range(10):
    posY = yFactor * dia
    for xFactor in range(10):
        posX = xFactor * dia
        
        d = random() * dia
        x = posX + (dia - d)/2
        y = posY + (dia - d)/2
        oval(x, y, d , d)