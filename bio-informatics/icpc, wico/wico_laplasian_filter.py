import cv2
from   matplotlib import pyplot as plt
import numpy as np

imageFile = 'lplasian.png'
imgGray = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)
plt.axis('off')

plt.imshow(imgGray, cmap = "gray", interpolation='bicubic')
plt.show()

imageFile = 'X_ray1.jpg'
imgGray = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)

plt.figure(figsize=(6,6))
plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
plt.imshow(imgGray, cmap = 'gray')
##plt.axis('tight')
plt.axis('off')
plt.savefig('X_Ray.jpg')
plt.show()

#Gaussian Blur
src = cv2.imread('X_ray1', cv2.IMREAD_GRAYSCALE)
image = cv2.imread('x_ray1.jpg').astype(np.float32) / 255
noised = (image + 0.2 * np.random.rand(*image.shape).astype(np.float32))
noised = noised.clip(0, 1)
plt.imshow(noised[:,:,[2,1,0]])
gauss_blur = cv2.GaussianBlur(noised, (7, 7), 0)

plt.imshow(gauss_blur[:, :, [2, 1, 0]])

plt.show()
#laplasian
img  = cv2.imread('gauss.png', cv2.IMREAD_GRAYSCALE)
laplacian = cv2.Laplacian(img,cv2.CV_8U,ksize=5)
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.imshow(img,cmap = 'gray')
plt.show()


src = cv2.imread('X_Ray.jpg', cv2.IMREAD_GRAYSCALE)
dst = cv2.equalizeHist(src)
cv2.imshow('dst',  dst)
cv2.waitKey()    
cv2.destroyAllWindows()

plt.title('Grayscale histogram of X_Ray.jpg')

hist1 = cv2.calcHist(images=[src], channels=[0], mask=None,
                    histSize=[256], ranges=[0, 256])
plt.plot(hist1, color='b', label='hist1 in src')

hist2 = cv2.calcHist(images=[dst], channels=[0], mask=None,
                    histSize=[256], ranges=[0, 256])
plt.plot(hist2, color='r', alpha=0.7, label='hist2 in dst')
plt.legend(loc='best')
plt.show()

src = cv2.imread("X_Ray1.jpg")
roi = cv2.selectROI(src)
print("roi=", roi)
img =src[roi[3]:roi[3]+roi[3],
        roi[3]:roi[3]+roi[3]]
cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()
output = roi= (776, 296, 600, 536)

emd1, lowerBound, flow = cv2.EMD(S1, S2, cv2.DIST_L1)
print('EMD(S1, S2, DIST_L1) =',  emd1)

emd2, lowerBound, flow = cv2.EMD(S1, S2, cv2.DIST_L2)
print('EMD(S1, S2, DIST_L2) =',  emd2)

emd3, lowerBound, flow = cv2.EMD(S1, S2, cv2.DIST_C) 
print('EMD(S1, S2, DIST_C) =',  emd3)

plt.plot(H1, color='r', label='H1')
plt.plot(H2, color='b', label='H2')
plt.legend(loc='best')
plt.show()

#output
EMD(S1, S2, DIST_L1) = 18.341209411621094
EMD(S1, S2, DIST_L2) = 18.341209411621094
EMD(S1, S2, DIST_C) = 18.341209411621094

# canny 
cv2.imshow('src',  src)
cv2.imshow('blur', blur)
lap = cv2.Laplacian(src, cv2.CV_32F)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(lap)
print('lap:', minVal, maxVal, minLoc, maxLoc)
dst = cv2.convertScaleAbs(lap)
dst = cv2.normalize(dst, None, 0, 255, cv2.NORM_MINMAX)
cv2.imshow('lap',  lap)
cv2.imshow('dst',  dst)

lap2 = cv2.Laplacian(blur, cv2.CV_32F)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(lap2)
print('lap2:', minVal, maxVal, minLoc, maxLoc)
dst2 = cv2.convertScaleAbs(lap2)
dst2 = cv2.normalize(dst2, None, 0, 255, cv2.NORM_MINMAX)

cv2.imshow('lap2', lap2)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()
