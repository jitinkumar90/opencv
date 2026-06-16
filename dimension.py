import cv2
image =cv2.imread("ram.jpeg")
if image is not None:
    w,h,c=image.shape
    # print(f"Image loaded:\n height :{h}\nwidth :{w}\nchannel :{c}")
    print(w)
    print(c)
    print(h)

else:
    print("file not loaded")

