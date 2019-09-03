import unittest
import os
import shutil
from looptools import Timer

from pathlib import Path

from ImgConverter.convert import Convert2Image


directory = os.path.join(os.path.dirname(__file__), 'data')
destination = os.path.join(directory, 'converted')


class TestConverter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if os.path.exists(destination):
            shutil.rmtree(destination)
        os.mkdir(destination)

    def _validate_img(self, img, target_format):
        self.assertTrue(os.path.exists(img))
        self.assertEqual('.' + target_format, Path(img).suffix)

    @Timer.decorator
    def test_png_to_jpg(self):
        png = os.path.join(directory, 'png.png')
        target_format = 'jpg'
        new_imgs = Convert2Image(destination, target_format).convert(png)

        for img in new_imgs:
            self._validate_img(img, target_format)

    @Timer.decorator
    def test_pdf_to_jpg(self):
        source = os.path.join(directory, 'pdf.pdf')
        target_format = 'jpg'
        new_imgs = Convert2Image(destination, target_format).convert(source)

        for img in new_imgs:
            self._validate_img(img, target_format)

    @Timer.decorator
    def test_psd_to_png(self):
        source = os.path.join(directory, 'psd.psd')
        target_format = 'png'
        new_imgs = Convert2Image(destination, target_format).convert(source)

        for img in new_imgs:
            self._validate_img(img, target_format)

    @Timer.decorator
    def test_psd_to_jpg(self):
        source = os.path.join(directory, 'psd.psd')
        target_format = 'jpg'
        new_imgs = Convert2Image(destination, target_format).convert(source)

        for img in new_imgs:
            self._validate_img(img, target_format)

    @Timer.decorator
    def test_jpg_to_png(self):
        source = os.path.join(directory, 'jpg.jpg')
        target_format = 'png'
        new_imgs = Convert2Image(destination, target_format).convert(source)

        for img in new_imgs:
            self._validate_img(img, target_format)


if __name__ == '__main__':
    m = unittest.main()
