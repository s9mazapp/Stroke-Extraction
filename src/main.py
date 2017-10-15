from stroke_extraction import extractStrokes
import cv2

img = cv2.imread('../test.bmp', cv2.IMREAD_GRAYSCALE)
extractStrokes(img)