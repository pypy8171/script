import urllib.request
import xml.etree.ElemantTree as etree


def main():
    tree = etree.parse('sample1.xml')
    root = tree.getroot()

    for a in root.findall('row'):
        print(a.findtext('TITLE'))
        print(a.findtext('START_DATE'))

if __name__ == "__main__":
    main()

class GetData:

    key =  'sjDf4KxuUWYlp2LX1z%2FSo4GkyIn%2BaKcGyxmo1uK06%2FMYvTEUyDIswZK42AijclDKjZTFkVuB0C81bwVLBUP3BQ%3D%3D'
    url= 'http://apis.data.go.kr/B551182/hospAsmRstInfoService/getRcperHospAsmRstList?'

    def main(self):
        data = urllib.request.urlopen(self.url).read()
        f = open("sample.xml","wb")
        f.write(data)
        f.close()

getData = GetData()
getData.main()