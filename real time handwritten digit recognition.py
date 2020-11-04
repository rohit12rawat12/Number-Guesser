import cv2
import tensorflow as tf
import numpy as np

drawing = False # true if mouse is pressed
ix,iy = -1,-1

# resizing the array to 28x28
def prepare(npArray):
	IMG_SIZE = 28
	grayArray = cv2.cvtColor(npArray, cv2.COLOR_BGR2GRAY)
	resizedImage = cv2.resize(grayArray, (IMG_SIZE, IMG_SIZE))
	return resizedImage

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img,(x,y),10,(0,0,0),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

img = np.empty((200,200,3), np.uint8) # creating a array of size 200x200
img[:,:,:] = 255 # filling the array by vale 255, so that when we visualize the img array then it will be white in color

while(1):
	cv2.namedWindow('image')
	cv2.setMouseCallback('image',draw_circle) #getting callbacks from mouse

	while(1):
	    cv2.imshow('image',img)
	    key = cv2.waitKey(1) & 0xFF
	    if key == ord('q') or key == 27:
	        break

	if key == 27:
		break
	arr = img.copy()

	cv2.destroyAllWindows()

	# loading the model
	model = tf.keras.models.load_model("Model.model")
	new_array = (255-prepare(arr))/255.0

	prediction = model.predict([[new_array]])
	print(np.argmax(prediction))
	
	img[:,:,:] = 255 # resetting the window