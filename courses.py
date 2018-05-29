import requests
from bs4 import BeautifulSoup
anaUrl="http://registration.boun.edu.tr"

r1=requests.get("http://registration.boun.edu.tr/scripts/schdepsel.asp")
soup1=BeautifulSoup(r1.content,"html.parser")
linkler = soup1.find_all("a")
linkSayisi=len(linkler)
sayac=0
dersAdi=[]
dersUrlsi=[]
for link in linkler:
    dersAdi.append(link.text)
    duzeltmeUrl=link.get("href")
    duzeltmeUrl =duzeltmeUrl.replace("donem=","donem=2018/2019-1")
    dersUrlsi.append(duzeltmeUrl)
    print(link.get("href"))
    sayac+=1
    if (sayac==linkSayisi-1):
        break

# ders adı ve urllerini aldık, şimdi her bir ders için bilgileri çekme zamanı
import codecs

i=len(dersAdi)
k=0
dosya=open("reiz.txt","a",encoding="utf-8")
while (k<i):
    print(str(dersAdi[k])+" ***********************************************************************")
    dosya.write(str(dersAdi[k])+"*******************************************\n")
    reiz= requests.get("http://registration.boun.edu.tr"+dersUrlsi[k])
    
    kaynakHtml =BeautifulSoup(reiz.content,"html.parser")
    listeler=kaynakHtml.find_all("tr", {"class":"schtd2"})
   
    print(str(len(listeler))+" tane ders var reiz bölümümüzde")
    for liste in listeler:
        dersBilgisi=liste.find_all("td")
        
        print(dersBilgisi[0].text+dersBilgisi[2].text+dersBilgisi[3].text+dersBilgisi[5].text+dersBilgisi[6].text+dersBilgisi[7].text+dersBilgisi[8].text)
        dosya.writelines(dersBilgisi[0].text+dersBilgisi[2].text+dersBilgisi[3].text+dersBilgisi[5].text+dersBilgisi[6].text+dersBilgisi[7].text+dersBilgisi[8].text+"\n")
        for bilgi in dersBilgisi:
            dosya.write(bilgi.text)
            if(bilgi==len(dersBilgisi)-1):
                dosya.write("+++")
    k+=1
    
dosya.close()
