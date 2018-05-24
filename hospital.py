import parser
# import xml.etree.ElementTree as ET
import urllib.request
import urllib.parse
import xmltodict
import json
from datetime import datetime


url = "http://apis.data.go.kr/B551182/hospAsmRstInfoService/getRcperHospAsmRstList?"
key = "serviceKey=" + "sjDf4KxuUWYlp2LX1z%2FSo4GkyIn%2BaKcGyxmo1uK06%2FMYvTEUyDIswZK42AijclDKjZTFkVuB0C81bwVLBUP3BQ%3D%3D"

addr = "&addr=" + "울산광역시 남구 돋질로 150 (달동)"
asmGrd = "&asmGrd=" + "3"
asmItmCd="&asmltmCd=" + "14"
clCd = "&clCd="+"28"
clCdNm = "&clCdNm=" + "요양병원"
sgguCd= "&sgguCd=" + "260001"
sgguCdNm= "&sgguCdNm=" + "울산남구"
sidoCd= "&sidoCd=" + "260000"
sidoCdNm="&sidoCdNm=" + "울산"
yadmNm = "&yadmNm=" + "태안요양병원"
ykiho = "&ykiho" + "JDQ4MTYyMiM4MSMkMSMkNCMkOTkkNTgxMzUxIzExIyQxIyQzIyQ4OSQzNjEyMjIjNzEjJDEjJDgjJDgz"
#type = "&_returnType=json"

api_url = url + key + addr + asmGrd + asmItmCd + clCd + clCdNm + sgguCd + sgguCdNm + sidoCd + sidoCdNm + yadmNm +ykiho#+ type

data = urllib.request.urlopen(api_url).read().decode('utf8')
data_json = json.loads(data)
