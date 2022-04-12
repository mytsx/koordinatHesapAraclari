#-*-coding:utf-8-*-

"""
#example coordinate.txt file format:
longitude latitude
34.74438707266386,37.95004226164669
34.74620956220372,37.94962770732636
34.74613562649268,37.94602404889023
34.7465906726874,37.94601729276115
34.74654907757348,37.94426059117788
34.74473213134179,37.94442273448536
34.74352824172858,37.94885641418389
"""

import requests, json

from kml_to_xml import *
from xml_to_json import *

# kml_to_xml(os.path.join(os.getcwd(), "ocak_koordinatları.kml"))
# xml_to_json(os.path.join(os.getcwd(), "ocak_koordinatları.xml"))

with open('ocak_koordinatları.json') as json_file:
    data = json.load(json_file)
# print(data)

coord = data['kml']['Document']['Folder']['Placemark'][-1]['Polygon']['outerBoundaryIs']['LinearRing']['coordinates']
coord = [c for c in coord.split(",0") if c != ""]
print(coord)
file = open("coordinate.txt", "w+")
for coor in coord:
      print(coor.strip(), file=file, flush=True)
file.close()
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