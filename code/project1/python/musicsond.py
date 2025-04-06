def inputthing( textname : str) -> None:
    usingtext = open(textname, "w")
    list = []
    while True:
        nextmusicname = None
        print("input the phonetic name")
        print("format : ( phonetic name（ simplified or staff notation ), octave )")
        print("press Q to finish")
        nextmusicname = str(input(" >>>|| input data : "))
        if nextmusicname == "Q":
            break
        else:
            list.append(nextmusicname)
    usingtext.write(str(list))
    usingtext.close()

    
inputthing("/Users/yihaichen/Desktop/mycomputer/code/project1/python/Generatefiles/musicsongpython.txt")
