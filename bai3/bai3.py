import cv2

path = "./test/test.png"

#anh den trang
b_w = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

cv2.imwrite('./result/blackwhite.png',b_w)



img = cv2.imread(path,-1)

#bien doi sang  b g r a
b,g,r,a = cv2.split(img)

cv2.imwrite('./result/BChannel.png',b)
cv2.imwrite('./result/GChannel.png',g)
cv2.imwrite('./result/RChannel.png',r)
cv2.imwrite('./result/AChannel.png',a)


img=cv2.merge((b,g,r,a))
#khoi phuc anh 
cv2.imwrite('./result/MergedOutput.png',img)
