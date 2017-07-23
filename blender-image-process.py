'''
http://qiita.com/nacasora/items/cf0e27d38b09654cf701
'''
import bpy
import numpy as np
from PIL import Image, ImageFilter

# blimg = bpy.data.images['Lenna.png']
# width, height = blimg.size

'''accece used data image'''
# width, height = blimg.size
# print(width, height)

'''set and get pixil info'''
# # get pixil info
# # R,G,B,A 1 pixil
# print(blimg.pixels[0], blimg.pixels[1], blimg.pixels[2], blimg.pixels[3])
# # R,G,B,A 2 pixil
# print(blimg.pixels[4], blimg.pixels[5], blimg.pixels[6], blimg.pixels[7])
#
# # set pixil info
# blimg.pixels[0] = 1.0
# blimg.pixels[1] = 0.0
# blimg.pixels[2] = 0.0
# blimg.pixels[3] = 1.0
# # => set red of 1 pixil

'''set and get pixil array'''
# # get array all pixil info
# pxs = list(blimg.pixels[:])
#
# for i in range(0, width*height*4, 4):
# 	pxs[i]   = 1.0 # R
# 	pxs[i+1] = 0.0 # G
# 	pxs[i+2] = 0.0 # B
# 	pxs[i+3] = 1.0 # A
#
# # set all array to add process
# blimg.pixels = pxs

'''set and get pixil array-'''
# pxs0 = blimg.pixels[:]
# pxs = [0] * len(pxs0)
# # or
#pxs = [0] * (width * height * 4)
#
# for i in range(0, width*height*4, 4):
# 	pxs[i]   = pxs0[i] * 0.5   # R
# 	pxs[i+1] = pxs0[i+1] * 0.5 # G
# 	pxs[i+2] = pxs0[i+2] * 0.5 # B
# 	pxs[i+3] = pxs0[i+3]	   # A
#
# blimg.pixels = pxs

'''set pixil value of coodenate'''
# pxs = list(blimg.pixels[:])
#
# for y in range(10, 40):
# 	for x in range(10, 20):
#		# conform converse image of  x,y
# 		if 0<=x and x<width and 0<=y and y<height:
# 			i = (y*width+x)*4
# 			pxs[i]   = 1.0 # R
# 			pxs[i+1] = 1.0 # G
# 			pxs[i+2] = 1.0 # B
# 			pxs[i+3] = 1.0 # A
#
# blimg.pixels = pxs

'''BoxBlur'''
# # <!> do 1.0 alpha value image
# pxs0 = blimg.pixels[:]
# pxs = [0] * len(pxs0)
#
# def inside(x,y):
# 	return 0<=x and x<width and 0<=y and y<height
#
# size = 5
# for y in range(height):
# 	for x in range(width):
# 		i = (y*width+x)*4
# 		r=0
# 		g=0
# 		b=0
# 		n=0
# 		for v in range(y-size, y+size+1):
# 			for u in range(x-size, x+size+1):
# 				if inside(u,v):
# 					j = (v*width+u)*4
# 					r += pxs0[j]
# 					g += pxs0[j+1]
# 					b += pxs0[j+2]
# 					n += 1
# 		pxs[i]   = r/n
# 		pxs[i+1] = g/n
# 		pxs[i+2] = b/n
# 		pxs[i+3] = 1.0
#
# blimg.pixels = pxs

'''output another name'''
# imagename = 'BPY Output.png'
# width	 = 32
# height	= 32
# blimg  = bpy.data.images.new(imagename, width, height, alpha=True)
# blimg.pixels = [1.0]*(width*height*4)

'''array pixil to transform numpy array'''
# arr = np.array(blimg.pixels[:])

'''do active NumPy'''
# # substitute 0 all R element
# arr[0::4] = 0.0
#
# blimg2 = bpy.data.images.new('B', width, height, alpha=True)
# blimg2.pixels = arr

'''again Box Blur'''
# W, H = blimg.size
#
# a = np.array(blimg.pixels[:])
# b = np.ndarray(len(a))
# a.resize(H, W*4)
# b.resize(H, W*4)
#
# a_R = a[::, 0::4]
# a_G = a[::, 1::4]
# a_B = a[::, 2::4]
# b_R = b[::, 0::4]
# b_G = b[::, 1::4]
# b_B = b[::, 2::4]
#
# size = 5
# for y in range(H):
# 	y0 = max(0, y-size)
# 	y1 = min(H-1, y+size)
# 	for x in range(W):
# 		x0 = max(0, x-size)
# 		x1 = min(W-1, x+size)
# 		n = (y1-y0)*(x1-x0)
# 		b_R[y][x] = np.ndarray.sum(a_R[y0:y1, x0:x1]) / n
# 		b_G[y][x] = np.ndarray.sum(a_G[y0:y1, x0:x1]) / n
# 		b_B[y][x] = np.ndarray.sum(a_B[y0:y1, x0:x1]) / n
#
# # Alpha == 1.0
# b[::, 3::4] = 1.0
# b = b.flatten()
#
# blimg2 = bpy.data.images.new('B', W, H, alpha=True)
# blimg2.pixels = b

'''use to transform path file'''
def save_as_png(img, path):
	s = bpy.context.scene.render.image_settings
	prev, prev2 = s.file_format, s.color_mode
	s.file_format, s.color_mode = 'PNG', 'RGBA'
	img.save_render(path)
	s.file_format, s.color_mode = prev, prev2

blimg = bpy.data.images['Lenna.png']
W,H   = blimg.size

temppath = 'd:/temp/bpytemp.png'
# 一時ファイルに保存(Blender)
save_as_png(blimg, temppath)
# 一時ファイルから読み込み(PIL)
pimg = Image.open(temppath)
# PILのフィルタを適用する(ガウシアンブラー)
pimg2 = pimg.filter(ImageFilter.GaussianBlur(radius=5))
# 一時ファイルに保存(PIL)
pimg2.save(temppath)
# 一時ファイルから読み込み(Blender)
blimg2 = bpy.data.images.load(temppath)
blimg2.name = 'B'
