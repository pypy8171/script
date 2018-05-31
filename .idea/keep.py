
def LoadXMLFromFile():
    fileName  = str(inpu("please input file name to load:"))
    global xmlFD

    try:
        xmlFD = open(fileName)
    except IOError:
        print("invalid file name or path")
        return None
    else:
        try:
            dom = parse(xnmFD)
        except Exception:
            print("loading fail")
        else:
            print("XML document loading complete")
            return dom
    return None

def MoviesFree():
    if checkDocument():
        response_body.unlink()

def PrintDOMtoXML():
    if checkDocument():
        print(response_body.toxml())