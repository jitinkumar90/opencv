import cv2
image=cv2.imread("ram.jpeg",0)
if image is not None:
    cv2.imshow("mahadev",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("no image found")