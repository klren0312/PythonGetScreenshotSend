from PIL import Image
#打开当前路径的图片
im = Image.open('test.png')
#获取图像尺寸
w,h = im.size
print('original image size : %sx%s' %(w,h))
#缩放到50%
im.thumbnail(w//2,h//2)
print('Resize image to : %sx%s' % (w//2,h//2))
#把缩放后的图像用jpeg格式保存
im.save('test_ap.png','png')