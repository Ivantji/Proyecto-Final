import math
from geometryy.geometry import Geometry


class Esfera(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        # Círculo 1
        radius1 = width / 0.5 #se calcula dividiendo el ancho (width) entre 0.5
        segments1 = 50 # el círculo 1 se divide en 50 segmentos
        center1 = [-width / 1, 0, 0] #sugiere que el centro del círculo 1 se encuentra a una distancia igual al ancho multiplicado por -1 en el eje x y a 0 en los ejes y y z.
        color1 = [1, 0, 0]# esto solo define el color
        #crean dos listas vacías
        circle1_positionData = []
        circle1_colorData = []

        for i in range(segments1): #segments1 es una variable que define la cantidad de segmentos o puntos que deseas en el círculo 1.
            angle = 2 * math.pi * i / segments1 #En cada iteración, se calcula el ángulo en radianes para el punto actual del círculo.
            #se calculan las coordenadas (x, y, z) del punto actual en el espacio 3D.
            x = center1[0] + radius1 * math.cos(angle)
            y = center1[1] + radius1 * math.sin(angle)
            z = center1[2]
            #Las coordenadas (x, y, z) calculadas en la iteración se agregan a la lista circle1_positionData como una lista [x, y, z]
            circle1_positionData.append([x, y, z])
            circle1_colorData.append(color1)

        # Círculo 2
        radius2 = width / 1
        segments2 = 25
        center2 = [width / 8, 1, 0]
        color2 = [0, 0, 1]

        circle2_positionData = []
        circle2_colorData = []

        for i in range(segments2):
            angle = 2 * math.pi * i / segments2
            x = center2[0] + radius2 * math.cos(angle)
            y = center2[1] + radius2 * math.sin(angle)
            z = center2[2]
            circle2_positionData.append([x, y, z])
            circle2_colorData.append(color2)

        positionData = circle1_positionData + circle2_positionData
        colorData = circle1_colorData + circle2_colorData

        self.addAttribute("vec3", "vertexPosition", positionData)
        self.addAttribute("vec3", "vertexColor", colorData)
        self.countVertices()
