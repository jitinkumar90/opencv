import cv2
hi =cv2.imread("ram.jpeg")
if hi is not None:
    w,h,c=hi.shape
    # print(f"Image loaded:\n height :{h}\nwidth :{w}\nchannel :{c}")
    print(w)
    print(c)
    print(h)

else:
    print("file not loaded")

