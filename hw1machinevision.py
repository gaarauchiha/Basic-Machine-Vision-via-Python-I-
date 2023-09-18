
import cv2 as cv
import matplotlib.pyplot as plt

camman=cv.imread("C:/Users/ASUS  N551JW/Desktop/machine vision/cameraman.jpg")
cv.imshow("cameraman",camman)
cam1=camman.copy()
cam10=cam1[:,:,:] & 0b11111110
cv.imshow("lastbit",cam10)


cam2=camman.copy()
cam3=camman.copy()
cam4=camman.copy()
cam5=camman.copy()
cam6=camman.copy()
cam7=camman.copy()

cam20=cam2[:,:,:] & 0b11111100
cam30=cam3[:,:,:] & 0b11111000
cam40=cam4[:,:,:] & 0b11110000
cam50=cam5[:,:,:] & 0b11100000
cam60=cam6[:,:,:] & 0b11000000
cam70=cam7[:,:,:] & 0b10000000

cv.imshow("last 2bit",cam20)
cv.imshow("last 3bit",cam30)
cv.imshow("last 4bit",cam40)
cv.imshow("last 5bit",cam50)
cv.imshow("last 6bit",cam60)
cv.imshow("last 7bit",cam70)

plt.figure()
plt.subplot(4,2,1)
plt.imshow(camman)
plt.subplot(4,2,2)
plt.imshow(cam10)
plt.subplot(4,2,3)
plt.imshow(cam20)
plt.subplot(4,2,4)
plt.imshow(cam30)
plt.subplot(4,2,5)
plt.imshow(cam40)
plt.subplot(4,2,6)
plt.imshow(cam50)
plt.subplot(4,2,7)
plt.imshow(cam60)
plt.subplot(4,2,8)
plt.imshow(cam70)
plt.show()




import cv2 as cv
import matplotlib.pyplot as plt

logo=cv.imread("C:/Users/ASUS  N551JW/Desktop/machine vision/logo.bmp")
camman=cv.imread("C:/Users/ASUS  N551JW/Desktop/machine vision/cameraman.jpg")

cam1=camman.copy()
cv.imshow("logo",logo)
logo1=logo.copy()
graylogo=cv.cvtColor(logo1,cv.COLOR_BGR2GRAY)
grylogo1=graylogo.copy()
width , height = graylogo.shape


for i in range(width):
    for j in range(height):
        grylogo1[i,j]=grylogo1[i,j]/255
        


for i in range(width):
    for j in range(height):
        cam1[:,:,:]=grylogo1[i,j] | cam1[:,:,:]

plt.figure()
plt.subplot(3,2,1)
plt.imshow(graylogo)
plt.subplot(3,2,2)
plt.imshow(cam1)
plt.show()

