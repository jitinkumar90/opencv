import cv2
image=cv2.imread("ram.jpeg")
if image is not None:
    resizedimage=cv2.resize(image,(200,200))
    cv2.imshow("resize",resizedimage)
    cv2.imshow("original",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("no image founded")