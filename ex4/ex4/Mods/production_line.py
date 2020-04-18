from random import randrange
from cv2 import cv2
import time
import imutils


class Production_line:
    temporary_image = None

    def __init__(self, image):
        self.__image = image

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, value):
        self.__image = value

    def Step1(self):
        changed = imutils.adjust_brightness_contrast(self.load_production_image(), brightness=30)
        print("Zwiększam kontrast o 30pkt.")
        self.save_change(changed)
        self.show_changed_image(changed)

    def Step2(self):
        changed = cv2.bitwise_not(self.load_production_image())
        print("Odwracam kolory.")
        self.save_change(changed)
        self.show_changed_image(changed)

    def Step3(self):
        changed = imutils.adjust_brightness_contrast(self.load_production_image(), brightness=-30)
        print("Zmniejszam kontrast o 30pkt.")
        self.save_change(changed)
        self.show_changed_image(changed)

    def save_copy(self):
        cv2.imwrite("changed.jpg", self.__image)

    @staticmethod
    def show_changed_image(changed):
        cv2.imshow("Changed image", changed)
        cv2.waitKey(0)
        time.sleep(0)
        cv2.destroyWindow("Changed image")

    @staticmethod
    def load_production_image():
        prod_image = cv2.imread("changed.jpg")
        return prod_image

    @staticmethod
    def save_change(changed):
        cv2.imwrite("changed.jpg", changed)

    def add_step(self, x):
        self.save_copy()
        cv2.imshow("Your Image", self.__image)
        cv2.waitKey(0)
        time.sleep(0)
        print("Zapisuję kopię i rozpoczynam modyfikację.")
        for i in range(x):
            dice = randrange(1, 4)
            if dice == 1:
                self.Step1()
            elif dice == 2:
                self.Step2()
            elif dice == 3:
                self.Step3()

        print("Kończę obróbkę. Twój plik znajduje się w głownym folderze projektu o nazwie x.changed.")
