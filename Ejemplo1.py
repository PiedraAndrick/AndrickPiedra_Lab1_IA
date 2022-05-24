# -*- coding: utf-8 -*-
"""
Created on Sun May 22 14:07:05 2022

@author: piedr
"""
def vacuum_world():
    #Costo inicial
    costo = 0
    
    #Definimos los estados iniciales de las habiaciones
    estado_habitacion1 = input("Estado actual de la Habitacion 1 : ") #Ingreso del estado de la primera habitacion
    estado_habitacion2 = input("Estado actual de la Habitacion 2 : ") #Ingreso del estado de la segunda habitacion
    estado_habitacion3 = input("Estado actual de la Habitacion 3 : ") #Ingreso del estado de la tercera habitacion
    
    #Creamos una lista de los estados iniciales
    lista_habitaciones_estados_originales = [estado_habitacion1,estado_habitacion2,estado_habitacion3]
    
    #Definimos el estado global 
    estado_global = {'Habitacion 1': estado_habitacion1 , 'Habitacion 2': estado_habitacion2,'Habitacion 3': estado_habitacion3}
    print("Estado Global:" + str(estado_global))
    
    #Definimos los estados finales de las habiaciones
    estadoActual_habitacion1 = input("Actualizar estado de habitacion 1: ") #Ingreso del estado requerido para la habitacion
    estadoActual_habitacion2 = input("Actualizar estado de habitacion 2 : ") #Ingreso del estado requerido para la habitacion
    estadoActual_habitacion3 = input("Actualizar estado de habitacion 3 : ") #Ingreso del estado requerido para la habitacion
    
    #Creamos la lista de los estados a los cuales se debe actualizar
    lista_habitaciones_estados_actalizar = [estadoActual_habitacion1,estadoActual_habitacion2,estadoActual_habitacion3]
    
    #Bucle FOR que recorre la lista de las habitaciones de los estados originales
    # y se compara con los estados actualizados 
    print("*****ACONDICIONANDO HABITACIONES*****")
    for i in range(0,len(lista_habitaciones_estados_originales)):
        if lista_habitaciones_estados_originales[i] == '0':
            # Habitacion esta Caliente     
          print("Habitacion "+ str(i)+" en estado caliente")
          if lista_habitaciones_estados_actalizar[i] == '0':
              print("Habitacion "+ str(i)+" ya esta calida")
          else:
              print("Enfriando Habitacion "+ str(i))
              estado_global['Habitacion '+str(i+1)] = '1' 
              costo += 1
        else: 
            #Habitacion esta fria
          print("Habitacion "+ str(i)+" en estado frio")  
          if lista_habitaciones_estados_actalizar[i] == '1':  
              print("Habitacion "+ str(i)+" ya esta fria")
          else:
              print("Calentando Habitacion "+ str(i))
              estado_global['Habitacion '+str(i+1)] = '0' 
              costo += 1
                    
         # Finalizando Acondicionamiento
    print("Estado actual de las habitaciones: "+"\n Frio = 0 / Caliente = 1")
    for key, value in estado_global.items():
        print(str(key)+" en estado "+str(value))
    print("Medida de desempeño: " + str(costo))
          
vacuum_world()