from PIL import Image
import random


def openImage(img):
	im = Image.open(img)
	return im

def randomPixel(w,h,radius_range):
	choosen_pixel =[]
	max_raidus = radius_range[1]
	for i in range(8000):
		random_x = random.randint(max_raidus,w - max_raidus)
		random_y = random.randint(max_raidus,h - max_raidus)
		random_r = random.randint(radius_range[0],radius_range[1])
		choosen_pixel.append((random_x,random_y,random_r))
	return choosen_pixel

def pointllism(im,choosen_pixel):
	for point in choosen_pixel:
		x = point[0]
		y = point[1]
		r = point[2]
		pix = im.getpixel((x,y))
		for i in range(r):
			for j in range(r):
				im.putpixel((x+i,y+j),pix)
				im.putpixel((x-i,y-j),pix)
	im.show()

def main():
	im = openImage("plant.jpg")
	im.show()
	w,h = im.size
	radius_range = (3,10)
	choosen_pixel = randomPixel(w,h,radius_range)
	pointllism(im,choosen_pixel)

main()	