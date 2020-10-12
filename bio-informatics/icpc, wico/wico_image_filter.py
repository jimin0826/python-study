from matplotlib import pyplot as plt
from skimage.feature import corner_harris, corner_subpix, corner_peaks
from skimage.io import imread
import time

image = imread('bulr.jpg')
image = rgb2gray(image)
#이미지에서 해리스 코너를 계산한다. 이것은 이미지에서 각각의 픽셀의 코너 측정 응답 값을 반환한다. 
corners = corner_harris(image)
#코너 응답 값을 이용하여 이미지에 있는 실제 코너를 계산한다.
coords = corner_peaks(corners, min_distance=5)
#이 함수는 코너가 엣지 점인지 아니면 고립된 점인지를 결정한다.
coords_subpix = corner_subpix(image, coords, window_size=13)
fig, ax = plt.subplots()
ax.imshow(image, interpolation='nearest', cmap=plt.cm.gray)
ax.plot(coords[:, 1], coords[:, 0], '.b', markersize=3)
ax.plot(coords_subpix[:, 1], coords_subpix[:, 0], '+r', markersize=15)
ax.axis((0, 1000, 1000, 0))# adjusting size for covered photo
plt.show()

#1
nPoints = 100000
pts1 = np.zeros((nPoints, 1), dtype=np.uint16)
pts2 = np.zeros((nPoints, 1), dtype=np.uint16)

cv2.setRNGSeed(int(time.time()))
cv2.randn(pts1, mean=(128), stddev=(10))
cv2.randn(pts2, mean=(110), stddev=(20))            

#2
H1 = cv2.calcHist(images=[pts1], channels=[0], mask=None,
                    histSize=[256], ranges=[0, 256])
##cv2.normalize(H1, H1, norm_type=cv2.NORM_L1)

H2 = cv2.calcHist(images=[pts2], channels=[0], mask=None,
                    histSize=[256], ranges=[0, 256])
##cv2.normalize(H2, H2, norm_type=cv2.NORM_L1)

#3
S1 = np.zeros((H1.shape[0], 2), dtype=np.float32)
S2 = np.zeros((H1.shape[0], 2), dtype=np.float32)
##S1[:, 0] = H1[:, 0]
##S2[:, 0] = H2[:, 0]
for i in range(S1.shape[0]):
    S1[i, 0] = H1[i,0]
    S2[i, 0] = H2[i,0]
    S1[i, 1] = i
    S2[i, 1] = i

