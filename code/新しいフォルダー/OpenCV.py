import urllib.request as req
url = "http://www.wallpaper-box.com/cat/19201080/images/cat13.jpg"
req.urlretrieve(url."test.jpg")
import cv2
img = cv2.imread("test.jpg")
print(img)