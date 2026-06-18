import cv2
image=cv2.imread("ram.jpeg")
if image is not None:
    cropped=image[10:130,10:102]
    cv2.imshow("cropped image",cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("ji")