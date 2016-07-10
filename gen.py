import math
import random

#Fuck around with these values to change the color of the image

R_START = 192
R_END = 117
R_RANDOMNESS = 20

G_START = 70
G_END = 51
G_RANDOMNESS = 20

B_START = 41
B_END = 161
B_RANDOMNESS = 20

points=[]

r_dif = R_END - R_START
g_dif = G_END - G_START
b_dif = B_END - B_START



for y in range(28):
    points.append([])
    for x in range(45):
        if(y % 2 == 0):
            i = x*46.1880-46.1880
        else:
            i = x*46.1880-23.940
        j = y*40
        
        points[y].append([i,j])

svgStr="<svg viewBox='0 0 1920 1080' width='1920' height='1080' xmlns='http://www.w3.org/2000/svg'>\n"
x=0
for rows in points[:-1]:
    y=0
    for columns in rows[:-1]:
        d = (math.sqrt((x / 26.0) ** 2 + (y / 43.0) **2))
        r = str(int(R_START + r_dif * d + R_RANDOMNESS * (2 * random.random() - 1 ) ** 2))
        g = str(int(G_START + g_dif * d + G_RANDOMNESS * (2 * random.random() - 1 ) ** 2))
        b = str(int(B_START + b_dif * d + B_RANDOMNESS * (2 * random.random() - 1 ) ** 2))
        color = "style='fill:rgb(" + r + "," + g + "," + b + ");'" 
        if(x % 2 == 1):
            svgStr+="<polygon points='" + str(points[x][y][0]) + ","+ str(points[x][y][1]) + " " + str(points[x][y + 1][0]) +"," + str(points[x][y + 1][1]) + " " + str(points[x + 1][y + 1][0]) + "," +str(points[x + 1][y + 1][1]) + "' " + color + " />\n"
            if(y>0):
                svgStr+="<polygon points='" + str(points[x][y][0]) + "," + str(points[x][y][1]) + " " + str(points[x + 1][y][0]) + "," + str(points[x + 1][y][1]) + " " + str(points[x + 1][y + 1][0]) + "," + str(points[x + 1][y + 1][1]) + "' " + color + " />\n"
        else:
            svgStr+="<polygon points='" + str(points[x][y][0]) + ","+ str(points[x][y][1]) + " " + str(points[x + 1][y][0]) +"," + str(points[x + 1][y][1]) + " " + str(points[x][y + 1][0]) + "," +str(points[x][y + 1][1]) + "' " + color + " />\n"
            if(y>0):
                svgStr+="<polygon points='" + str(points[x][y][0]) + "," + str(points[x][y][1]) + " " + str(points[x+1][y-1][0]) + "," + str(points[x+1][y-1][1]) + " " + str(points[x+1][y][0]) + "," + str(points[x+1][y][1]) + "' " + color + " />\n"
        y+=1
    x+=1
svgStr+="</svg>"
svg=open("out2.svg","w")
svg.write(svgStr)
svg.close()
