import math
import random
points=[]

for y in range(28):
    points.append([])
    for x in range(45):
        if(y%2==0):
            i=x*46.1880-46.1880
        else:
            i=x*46.1880-23.940
        j=y*40
        #if (y!=0) and (y!=27):
            #j+=random.random()*10-5
        #i+=random.random()*10-5
        points[y].append([i,j])

svgStr="<svg viewBox='0 0 1920 1080' width='1920' height='1080' xmlns='http://www.w3.org/2000/svg'>\n"
x=0
for rows in points[:-1]:
    y=0
    for columns in rows[:-1]:
        if(x%2==1):
            svgStr+="<polygon points='" + str(points[x][y][0]) + ","+ str(points[x][y][1]) + " " + str(points[x][y+1][0]) +"," + str(points[x][y+1][1]) + " " + str(points[x+1][y+1][0]) + "," +str(points[x+1][y+1][1]) + "' style='fill:rgb(25," + str(int(23+150*(math.sqrt((x/26.0)**2 + (y/43.0)**2))+20*(2*random.random()-1)**2)) + ",150);' />\n"
            if(y>0):
                svgStr+="<polygon points='" + str(points[x][y][0]) + "," + str(points[x][y][1]) + " " + str(points[x+1][y][0]) + "," + str(points[x+1][y][1]) + " " + str(points[x+1][y+1][0]) + "," + str(points[x+1][y+1][1]) + "' style='fill:rgb(25," + str(int(23+150*(math.sqrt((x/26.0)**2 + (y/43.0)**2))+20*(2*random.random()-1)**2)) + ",150);' />\n"
        else:
            svgStr+="<polygon points='" + str(points[x][y][0]) + ","+ str(points[x][y][1]) + " " + str(points[x+1][y][0]) +"," + str(points[x+1][y][1]) + " " + str(points[x][y+1][0]) + "," +str(points[x][y+1][1]) + "' style='fill:rgb(2\
5," + str(int(23+150*(math.sqrt((x/26.0)**2 + (y/43.0)**2))+20*(2*random.random()-1)**2)) + ",150);' />\n"
            if(y>0):
                svgStr+="<polygon points='" + str(points[x][y][0]) + "," + str(points[x][y][1]) + " " + str(points[x+1][y-1][0]) + "," + str(points[x+1][y-1][1]) + " " + str(points[x+1][y][0]) + "," + str(points[x+1][y][1]) + "' style='fill:rgb(2\
5," + str(int(23+150*(math.sqrt((x/26.0)**2 + (y/43.0)**2))+20*(2*random.random()-1)**2)) + ",150);' />\n"
        y+=1
    x+=1
svgStr+="</svg>"
svg=open("out.svg","w")
svg.write(svgStr)
svg.close()
