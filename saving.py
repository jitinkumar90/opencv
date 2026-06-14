import cv2
image=cv2.imread("ram.jpeg")
if image is not None:
    cv2.imwrite("raghav.jpg",image)
    if success:
        print("radhe radhe")
    else:
        print("hi")
else:
    print("lala")
