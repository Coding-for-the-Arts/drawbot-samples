"""
Random Printmuster
"""
size(10,10)



for i in range(10):
    x = random()*10
    y = random()*5
    randomSize = random()*3
    if x > 2:
        fill(None)
        stroke(random(),random(), random())
        strokeWidth(2)
        oval(x,y,randomSize, randomSize)
    else:
         rect(x,y,randomSize, randomSize)