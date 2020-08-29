#Python code to finding, cropping and saving faces found in input images
import face_recognition as fr
from PIL import Image
image = fr.load_image_file("./known_people/intel.JPG")

face_loc = fr.face_locations(image)

#face_loc is an array containing the co-ordinates of each fcace
#Image.show(face_loc)

print("Found {} faces in this photograph.".format(len(face_loc)))

count = 0
for face_location in face_loc:
	#get co-ordinates and pass this to top,left,right and bottom
	top, right, bottom, left = face_location
	print("A face is detected at this location: Top {},Left {},Bottom {}, Right {}".format(top,left,bottom, right))
	
	#accessing actual face location
	face_image = image[top:bottom, left:right]
	pil_img = Image.fromarray(face_image)
	pil_img.save(str(count) + '.jpg')
	#cv2.imwrite("Result.jpg",pil_img)
	pil_img.show() #Optional
	count = count + 1
