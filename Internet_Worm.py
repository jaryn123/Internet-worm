import requests
from bs4 import BeautifulSoup

#request the web OBJ (By Module : requests)
header={
    "Cookie":"route=65389440feb63b53ee0576493abca26d; Hm_lvt_82932fc4fc199c08b9a83c4c9d02af11=1643363219,1643363261; Hm_lpvt_82932fc4fc199c08b9a83c4c9d02af11=1643363261; SECKEY_ABVK=RDTRFgbeLMXnxI6X7xkn6h+m5u+iKS8WfS4z4yX6+9g=; BMAP_SECKEY=9lBZfXoX4MPmDfubXRpd7d6y-63q7RB195V07mQpEYosgWZbbggpVgyYBEGeMhGL3OcZ3uuIcblujzrayyO-rOxr2UX6uXL4PEuiIIQh2E5BB-u40A7f2Wf_vDsl11ZzAQjwTo_jj-ZX1JxqDW06tWMAKhAQNJRbtUH3kiJmCUvII_zRV3NamULTBYWiFwC4F8Rpg_OPYl2H4CZH75faXA",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76",
}

##test WEB API
url="https://ys.endata.cn/BoxOffice/Ranking"
url2="https://www.phb123.com/city/renkou/rk.html"
res=requests.get(url2,headers=header)   ###requests.post(url,data,headers)
text=res.text #POST GET PUT DEL
print(res.status_code)  ###200 300 400 500

#analysis the web (By Module : BeautifulSoup)
main_page=BeautifulSoup(text,"html.parser") #html Parser
# print(main_page)

#Find the Table Contents
# table=main_page.find("table", attrs={"class":"el-table__body"}) # fing: find only one label
table=main_page.find('table',attrs={'class':'rank-table'})

trs=table.find_all('tr')  #find_all: find all labels
# print(table)

for tr in trs:
    lst=tr.find_all("td")
    if len(lst)!=0:
        for td in lst:
            res=td.text
            print(res)




