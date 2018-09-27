import os
from pathlib import Path
from psdconvert import ConvertPSD
from pdf.convert import pdf2img
from ImgConverter.jpg2png import jpg2png


class Convert2Image:
    def __init__(self, dst_directory, convert_to='png'):
        self._dst_dir = dst_directory
        self._dst_ext = '.' + convert_to.strip('.')

    def convert(self, source):
        """Convert a .jpg, .psd, .pdf or .png to another format"""
        # Source file name without extension
        src_name = Path(os.path.basename(source)).stem

        # Source file type
        src_ext = Path(os.path.basename(source)).suffix

        # Target file path
        target = os.path.join(self._dst_dir, src_name + self._dst_ext)
        print(target)

        # PSD ---> PNG
        if src_ext == '.psd':
            return [ConvertPSD(source).save(target)]

        # PDF ---> PNG
        elif src_ext == '.pdf':
            return pdf2img(source, output=target, ext=self._dst_ext)

        # JPG ---> PNG
        elif src_ext == '.jpg':
            return [jpg2png(source, target)]
