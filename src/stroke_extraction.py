import numpy as np
import cv2

class StrokeExtractor:

    def __init__(self, input_image):
        if input_image is None:
            raise ValueError
        self.input_image = input_image#cv2.adaptiveThreshold(
            #input_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 5)
        self.stroke_history = self.input_image.copy()
        self.stroke_history[self.stroke_history != 0] = 1
        self.processing_index = 0

    def find_top_left_most_pixel(self):
        for y in range(self.processing_index, self.stroke_history.shape[0], 1):
            for x in range(self.stroke_history.shape[1]):
                if self.stroke_history[y,x] == 1:
                    return (y, x)


    def scan_8_pixel_neighbourhood(self, pixel):
        neighbours = list()
        neighbourhood = self.stroke_history[pixel[0] - 1: pixel[0] + 2, pixel[1] - 1: pixel[1] + 2]
        neighbours = np.argwhere(neighbourhood)
        return tuple(zip(*neighbours))

    def hide_pixel(self, pixel):
        self.stroke_history[pixel] = 0

    def extract_strokes(self):
        while True:
            top_left_most_pixel = self.find_top_left_most_pixel()
            self.hide_pixel(top_left_most_pixel)
            neighbours = self.scan_8_pixel_neighbourhood(top_left_most_pixel)
            if len(neighbours) > 1:

            else:

        coords = self.scan_8_pixel_neighbourhood(pixel)
        print(coords)


def extractStrokes(src):
    strokeExtractor = StrokeExtractor(src)
    strokeExtractor.extract_strokes()


