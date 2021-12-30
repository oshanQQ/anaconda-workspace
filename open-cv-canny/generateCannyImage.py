import cv2

path = "img/lena.jpg"
img_gray = cv2.imread(path, 0)
img_canny = cv2.Canny(img_gray, 100, 200)


cv2.imwrite("output/lena_edge.jpg", img_canny)

cv2.imshow("image", img_canny)