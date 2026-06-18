import cv2
image=input("enter the image address")
image=cv2.imread(image)
if image is not None:
    yourinput=input("you would like to save or show the picture")
    if(yourinput=="save"):
        cv2.imwrite("newone.jpeg",image)
    elif(yourinput=="show"):
        cv2.imshow("image showing",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
     print("no input found")
else:
    print("no image founded")