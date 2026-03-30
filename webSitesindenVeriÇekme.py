import requests
from bs4 import BeautifulSoup

url = requests.get("https://www.kisamasallar.com/kategori/cocuk-hikayeleri/")

print(url)
if url.status_code==200:
    print("siteden veri çekilebilir")
else:
    print("siteden veri çekilmez")

#a = url.content
#a = url.text
a = url.encoding
print(a)

x = BeautifulSoup(url.content, "html.parser")
#print(x.prettify())
#print(x.title)
# print(x.title.name)
# print(x.html)
# print(x.body)
# print(x.head.title)   #sitenin başlığını yazdırır.
# print(x.head.title.text)  

# print(x.find("p"))


# print(x.find_all("p"))


# for i in x.find_all("p"):   #<p> ile başlayanları alır
#     print(i.text)
#     print("-"*100)


# print(x.find_all("h2"))  #başlıkları ifade eder.

# print(x.find("h2").text)


div_cek = x.find("h2",{"class":"post-title"}).a    #a ile simgelenmiş kısımları alır
#print(div_cek.get("href"))   #sadece bağlantıyı çekmiş olduk
print(div_cek.text) 




