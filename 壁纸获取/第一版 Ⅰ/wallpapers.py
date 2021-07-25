from requests import get


url = "http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"
root = "http://cn.bing.com"

json = get(url=url).json()

img_url = root + json["images"][0]["url"]

img_name = json["images"][0]["copyright"]
index = img_name.find("(")
img_name = img_name[:index - 1] + ".png"

img = get(url=img_url).content

with open(img_name, "wb") as file_obj:
    file_obj.write(img)

input("下载完成！按回车键退出")
