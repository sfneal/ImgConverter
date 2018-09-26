import unittest
import os
import shutil
from ImgConverter.converter import Convert2Image


directory = os.path.join(os.path.dirname(__file__), 'data')
destination = os.path.join(directory, 'converted')
if os.path.exists(destination):
    shutil.rmtree(destination)
    os.mkdir(destination)


class TestConverter(unittest.TestCase):
    def test_pdf2png(self):
        pdf = os.path.join(directory, 'charts.pdf')
        new_imgs = Convert2Image(destination).convert(pdf)

        for img in new_imgs:
            self.assertTrue(os.path.exists(img))

    def test_psd2png(self):
        psd = os.path.join(directory, 'plan.psd')
        new_psds = Convert2Image(destination).convert(psd)

        for img in new_psds:
            self.assertTrue(os.path.exists(img))

    def test_jpg2png(self):
        jpg = os.path.join(directory, 'photo.jpg')
        new_jpgs = Convert2Image(destination).convert(jpg)

        for img in new_jpgs:
            self.assertTrue(os.path.exists(img))


if __name__ == '__main__':
    m = unittest.main()
