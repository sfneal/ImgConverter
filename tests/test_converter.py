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
    @classmethod
    def setUpClass(cls):
        cls.Converter = Convert2Image(destination)

    def test_pdf(self):
        pdf = os.path.join(directory, 'charts.pdf')
        new_imgs = self.Converter.convert(pdf)

        for img in new_imgs:
            self.assertTrue(os.path.exists(img))

    def test_psd(self):
        psd = os.path.join(directory, 'plan.psd')
        new_psds = self.Converter.convert(psd)

        for img in new_psds:
            self.assertTrue(os.path.exists(img))


if __name__ == '__main__':
    m = unittest.main()
