
import os
import shutil


def varmi(dir, file):
    result = False
    os.chdir(dir)
    if file in os.listdir("."):
        result = True
    return result
    
def kml_to_xml(filePath, savedir = ""):
    if not filePath.endswith(".kml"):
        return "Kml Dosyası Değil!!!"
    k = "D:\\"; filename = filePath.split("\\")[-1].split(".")[0]
    if savedir == "":
        for i in filePath.split("\\")[1:-1]:
            k = os.path.join(k, i) # dosyanın bulunduğu klasör
        try:
            saveFileName = f"\\{filename}.xml"; syc = 0
            while True:
                if varmi(k, saveFileName[1:]):
                    saveFileName = f"\\{filename}{syc}.xml"; syc +=1
                else:
                    break # kaydedilecek dosya ismi ile aynı isimde bir dosya yoksa durdur
            dist = os.path.join(k+saveFileName)
            shutil.copyfile(src = filePath, dst=dist)
            # print(dist, " dosya kaydedildi.")
        except:
            print("hata")
    else:
        pass
        
# kml_to_xml(os.path.join(os.getcwd(), "ocak_koordinatları.kml"))