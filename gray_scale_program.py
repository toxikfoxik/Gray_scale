import cv2

img = cv2.imread(r'C:\Users\mkwlodarz\Desktop\Real-ESRGAN\results\nice_out.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
cv2.imshow('Grayscale', gray_img)
cv2.waitKey(0) 