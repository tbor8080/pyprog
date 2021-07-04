# Function -> test.py
# For Event Handle
def OnKeyPress(e):
    # Debug Print
    # print(e.keysym,e.keycode,e.char)
    if e.keycode==65651:# command + s
        # Debug Print
        # print("command+s > save", textWidget.get("1.0","end"))
        # saveFile
        saveFile("sample.txt", textWidget.get("1.0","end"))

# FileSave
def saveFile(file_name,data,encoding='utf-8'):
    with open(file_name, "a", encoding=encoding) as fp:
        fp.write(data)