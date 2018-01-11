from scipy.misc import imread
from scipy.misc import imresize
from skimage.transform import resize
from scipy.misc import imsave
from rgb2gray import rgb2gray
import os

for line in open('test_subset_actors.txt'):
    split_line = line.split()
    last_name = split_line[1].lower()
    id_ = split_line[2]
    file_extension = split_line[4].split('.')[-1]
    filename = last_name + id_ + '.' + file_extension
    if os.path.isfile("uncropped/" + filename):
        try:
            image = imread('uncropped/' + filename)
            coords = split_line[5].split(',')
            x1, y1 = int(coords[0]), int(coords[1])
            x2, y2 = int(coords[2]), int(coords[3])
            cropped = image[y1:y2][x1:x2]
            grayscale = rgb2gray(cropped)
            scaled = resize(grayscale, (32, 32))
            imsave('processed/' + filename, scaled)
        except IOError:
            continue
        except ValueError:
            continue
