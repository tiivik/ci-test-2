import os
from skimage.color import rgb2gray
from skimage import io

original = io.imread("image.jpg")
grayscale = rgb2gray(original)

io.imsave("image_gray.jpg", grayscale)