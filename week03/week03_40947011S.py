import json

def textReadAndPrint(txtFILE):
    """read the txtFILE and print hte content. """
    with open (txtFILE, encoding = "utf-8") as f:
        txtContent = f.read()
    return txtContent
#print(textReadAndPrint("./example/example.txt"))

def jsonFileWriter(jsonDICT, jsonFileName):
    """convert jsonDICT into a jsonFile and save it as jsonFileName."""
    with open (jsonFileName, mode = "w") as f:
        #json.dump(Write, Target, ascii ? )
        json.dump(jsonDICT, f, ensure_ascii = False)
    return None

if __name__ == "__main__":
    txtFilePath = "C:/Users/beckx/OneDrive/桌面/python/text_analyse/week03_40947011S.json"
    txt = textReadAndPrint(txtFilePath)
    print("txt檔：")
    print(txt)

    jsonDICT = {
    "name": {"zh":"", "en":""}, #json
    "birth": {"year":"", "month":"", "date":""},
    "job":"", #string
    "language":[], #list
    "education":[],
    "spouse":""
    }

    jsonDICT["name"]["zh"] = txt.split("\n")[0].split(" ")[1]
    jsonDICT["name"]["en"] = " ".join(txt.split("\n")[1].split(" ")[1:])
    jsonDICT["birth"]["year"] = txt.split("\n")[2].split(" ")[1]
    jsonDICT["birth"]["month"] = txt.split("\n")[2].split(" ")[3]
    jsonDICT["birth"]["date"] = txt.split("\n")[2].split(" ")[5]
    jsonDICT["job"] = txt.split("\n")[3].split("\t")[1]
    jsonDICT["language"] = txt.split("\n")[4].split(" ")[1].split("、")
    jsonDICT["education"] = txt.split("\n")[5].split(" ")[1].split("、")
    jsonDICT["spouse"] = txt.split("\n")[6].split(" ")[1].split("（")[0]
    print("json檔：")
    print(jsonDICT)
    jsonFileName = "week03_40947011S.json"
    jsonFileWriter(jsonDICT, jsonFileName)

    jsonDICT["job"] = txt.split("\n")[3].split("\t")[1]
    jsonDICT["language"] = txt.split("\n")[4].split(" ")[1].split("、")
    jsonDICT["education"] = txt.split("\n")[5].split(" ")[1].split("、")
    jsonDICT["spouse"] = txt.split("\n")[6].split(" ")[1].split("（")[0]
    print("json檔：")
    print(jsonDICT)
    jsonFileName = "week03_40947011S.json"
    jsonFileWriter(jsonDICT, jsonFileName)
