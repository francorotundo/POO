def f(x):
    respuesta = 0 #1

    for i in range(1000):  #1000
        respuesta+=1 
    
    for i in range(x): #x
        respuesta += x
    
    for i in range(x):  #2X**2
        for j in range(x): ##x.x 
            respuesta += 1 ###1
            respuesta += 1 ###1

    return respuesta #1

    #conteo de operaciones ---> 1002 + x +2x**2

