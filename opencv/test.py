import cv2 
img= cv2.imread('C:\\Users\\Ananya Verma\\Desktop\\python 3011\\opencv\\image.png',1)


height, width = img.shape[:2]
cv2.imshow("original img -- {} x{}".format(height,width),img)
(xs,xe,ys,ye)=map(int,input().split())


cropped_img=img[xs:xe,ys:ye]
cv2.imshow("cropped image --",cropped_img)

# print(img)
cv2.waitKey(0)
cv2.destroyAllWindows()
