from scipy.misc import imread
from scipy.misc import imresize
from skimage.transform import resize
from scipy.misc import imsave
from rgb2gray import rgb2gray

for line in open('coords.txt'):
    split_line = line.split()
    filename = split_line[0]
    image = imread('uncropped/' + filename)
    coords = split_line[1].split(',')
    x1, y1 = int(coords[0]), int(coords[1])
    x2, y2 = int(coords[2]), int(coords[3])
    print image.shape 
    cropped = image[y1:y2][x1:x2]
    print cropped.shape
    grayscale = rgb2gray(cropped)
    scaled = resize(grayscale, (32, 32))
    imsave('processed/' + filename, scaled)
