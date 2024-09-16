print("Valor de X:")
X = float(input())
print("Valor de Y:")
Y = float(input())  

if X != 0 and Y != 0:
    if X > 0 and Y > 0:
        print("Q1")
    elif X > 0 and Y < 0:
        print("Q4")
    elif X < 0 and Y > 0:
        print("Q2")
    elif X < 0 and Y < 0:
        print("Q3") 
elif X != 0 and Y == 0: 
    print("EIXO X")
elif X == 0 and Y != 0:
    print("EIXO Y") 
else:
    print("ORIGEM")    