import numpy as np
import cv2
import os

og_img = cv2.imread("static/images/evenmorecells.jpg") 

#convert og image into gray
gray_img = cv2.cvtColor(og_img, cv2.COLOR_BGR2GRAY) 

#blur gray image
medianBlur_img = cv2.medianBlur(gray_img, 5) 

#contrast stretching parameters
r1 = 25
s1 = 0
r2 = 150
s2 = 255

#function to contrast stretch each pixel
def contrastStretch(pixel): 
    if (0 <= pixel and pixel <= r1):
        return (s1 / r1) * pixel
    elif (r1 < pixel and pixel <= r2):
        return ((s2 - s1) / (r2 - r1)) * (pixel - r1) + s1
    else:
        return ((255 - s2) / (255 - r2)) * (pixel - r2) + s2

contrastStretch_vec = np.vectorize(contrastStretch) #vectorized function returns an (image) array
contrastStretch_img = contrastStretch_vec(medianBlur_img) #contrast stretches median blurred image
contrastStretch_img = contrastStretch_img.astype(np.uint8) #pixel values are fitted within range 0 to 255

#Otsu's thresholding
_, threshold = cv2.threshold(contrastStretch_img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

#find contours
contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#contours that are too short are not considered
min_contour_length = 20 #depends on size of cells in image
filtered_contours = []
for contour in contours:
    contour_length = len(contour)
    if min_contour_length <= contour_length:
        filtered_contours.append(contour)

#draw contours on the gray image
contour_img = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR)
cv2.drawContours(contour_img, filtered_contours, -1, (255, 0, 255), 2)
#cv2.imwrite("static/processedImage.jpg", contour_img)

#count and print number of cells/contours
cell_count = len(filtered_contours)
#print("Number of cells:", cell_count)

#display the gray image with contours
cv2.imshow("Blood Cells", og_img)
cv2.waitKey(0)
#cv2.imshow("Blue Enhanced", blue_enhanced)
#cv2.waitKey(0)
cv2.imshow("Gray", gray_img)
cv2.waitKey(0)
cv2.imshow("Median Blur", medianBlur_img)
cv2.waitKey(0)
cv2.imshow("Contrast Stretch", contrastStretch_img)
cv2.waitKey(0)
cv2.imshow('Contour Image', contour_img)
cv2.waitKey(0)

