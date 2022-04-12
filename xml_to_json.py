

import xmltodict
import os
import json

def varmi(dir, file):
    result = False
    os.chdir(dir)
    if file in os.listdir("."):
        result = True
    return result
        
def xml_to_json(filePath, savedir = ""):
    if not filePath.endswith(".xml"):
        return "Xml Dosyası Değil!!!"
    with open(filePath, encoding="utf-8") as xml_file: #"abc.xml", 

        data_dict = xmltodict.parse(xml_file.read(), encoding="utf-8")
        print(data_dict)
        json_data = json.dumps(data_dict)#.encode('utf-8').decode('unicode-escape')
        
        xml_file.close()
    
    k = "D:\\"; filename = filePath.split("\\")[-1].split(".")[0] # dosya adı
    if savedir == "":
        for i in filePath.split("\\")[1:-1]:
            k = os.path.join(k, i) # dosyanın bulunduğu klasör
        try:
            saveFileName = f"\\{filename}.json"; syc = 0
            while True:
                if varmi(k, saveFileName[1:]):
                    saveFileName = f"\\{filename}{syc}.json"; syc +=1
                else:
                    break # kaydedilecek dosya ismi ile aynı isimde bir dosya yoksa durdur
            dist = os.path.join(k+saveFileName)
            writeFile= open(dist, "w+", encoding="utf8")
            
            print(json_data, file=writeFile, flush=True)
            # print(dist, " dosya kaydedildi.")
        except:
            print("hata")
    else:
        pass

# xml_to_json(os.path.join(os.getcwd(), "ocak_koordinatları.xml"))
