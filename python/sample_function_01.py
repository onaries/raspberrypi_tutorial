import random

def makeFace():
    face = ['(x_x)', '(O_O)', '(-_-#)', '(>_<)', '(^o^)', '=^y^=', '(`_^)']
    numFace = len(face)
    index = random.randint(0, numFace - 1)
    return face[index]

print(makeFace())

