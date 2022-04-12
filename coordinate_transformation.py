#-*-coding:utf-8-*-

"""
#example coordinate.txt file format:
longitude latitude
32.850814 39.910991
32.836825 39.924765
32.853683 39.941803
32.852578 39.940583
"""

import requests

try:
  file=open("coordinate.txt","r+",encoding="utf-8")
  coordinate=file.readlines() 

except FileNotFoundError:
  print("coordinate.txt not found!")
  exit()
zones = [23035, 23036, 23037,23038] # UTM-ZONES

s_srs = 4326
t_srs = 23036

file.seek(0) #The top row operation in the coordinate.txt file.
for coor in coordinate:
    x, y = coor.replace("\n", "").split(",")
    print(x, y)
    # serviceURL = f"http://127.0.0.1:5000/trans?x={x}&y={y}&s_srs={s_srs}&t_srs={t_srs}&callback=jsonpFunction"
    serviceURL = f"https://epsg.io/trans?x={x}&y={y}&s_srs={s_srs}&t_srs={t_srs}&callback=jsonpFunction"
    
    r = requests.get(serviceURL)
    r = r.text.replace("jsonpFunction(", "").replace(")", "")
    r = eval(f"{r}")
    print(f"y = {round(float(r['x']))}, x = {round(float(r['y']))}")

#   file.write(str(xcoor)+" "+str(ycoor)+" "+str(zcoor)+"\n")
    
# print ("The query is completed, new coordinate values are written to the existing file.")
# file.close()