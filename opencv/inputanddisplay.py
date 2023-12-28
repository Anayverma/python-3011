import cv2
# read an image 
img = cv2.imread("C:\\Users\\Ananya Verma\\Desktop\\python 3011\\opencv\\image.png")

# signal to digital conversion 
# imageg to numbers -- 0s ands 1s for grayscale and 0-255 in color
# display the image
cv2.imshow("image", img)

# retend the image in screen 
cv2.waitKey(10000)

# terminate the window
cv2.destroyAllWindows()
