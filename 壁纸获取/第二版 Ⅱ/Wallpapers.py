from requests import get
from bs4 import BeautifulSoup as Bs
from re import findall as fd  # fd 会返回一个列表

page1 = get(url="https://cn.bing.com").text  # 国内版必应
page2 = get(url="https://cn.bing.com/?ensearch=1").text  # 国际版 bing

soup1 = Bs(page1, "html.parser")
soup2 = Bs(page2, "html.parser")

root_directory = "https://cn.bing.com"  # 必应网站的根目录

img_url1 = root_directory + soup1.head.link["href"]
img_url2 = root_directory + soup2.head.link["href"]

img1 = get(url=img_url1).content
img2 = get(url=img_url2).content

name1 = fd(pattern=r"\d+", string=img_url1)[0] + ".png"
name2 = fd(pattern=r"\d+", string=img_url2)[0] + ".png"

with open(name1, "wb") as file_obj1:
    file_obj1.write(img1)
with open(name2, "wb") as file_obj2:
    file_obj2.write(img2)
