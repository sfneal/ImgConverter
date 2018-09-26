import os
from pathlib import Path
from psdconvert import ConvertPSD
from pdf.convert import pdf2img
from ImgConverter.jpg2png import jpg2png


class Convert2Image:
    def __init__(self, target_directory, target_ext='.png'):
        self.dst_path = target_directory
        self.dst_ext = target_ext

    def convert(self, source):
        """Convert a .jpg, .psd, .pdf or .png to another format"""
        # Source file name without extension
        src_name = Path(os.path.basename(source)).stem

        # Source file type
        src_ext = Path(os.path.basename(source)).suffix

        # Target file path
        target = os.path.join(self.dst_path, src_name + self.dst_ext)

        # PSD ---> PNG
        if src_ext == '.psd':
            return [ConvertPSD(source).save(target)]

        # PDF ---> PNG
        elif src_ext == '.pdf':
            return pdf2img(source, tempdir=self.dst_path, ext=self.dst_ext)

        # JPG ---> PNG
        elif src_ext == '.jpg':
            return [jpg2png(source, target)]
