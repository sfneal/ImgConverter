import os
from pathlib import Path
from tempfile import NamedTemporaryFile
from psdconvert import ConvertPSD
from pdf.convert import pdf2img
from ImgConverter.jpg2png import jpg2png


class Convert2Image:
    def __init__(self, convert_to='png', dst_directory=None):
        self._dst_dir = dst_directory
        self._dst_ext = '.' + convert_to.strip('.')

    @staticmethod
    def name_ext(source):
        """
        Get file name and file extension from a source file

        :param source: A file path
        :return: file_name, file_ext
        """
        s = Path(os.path.basename(source))
        return s.stem, s.suffix

    def get_target(self, src_name):
        if os.path.isdir(self._dst_dir):
            # Concatenate destination
            return os.path.join(self._dst_dir, src_name + self._dst_ext)

        else:
            # Create a temporary destination
            return NamedTemporaryFile(suffix=self._dst_ext).name

    def convert(self, source):
        """Convert a .jpg, .psd, .pdf or .png to another format"""
        # Source file name without extension and file extension tupe
        src_name, src_ext = self.name_ext(source)

        # Target file path
        target = self.get_target(src_name)

        # No conversion needed
        if src_ext == self._dst_ext:
            return source

        # PSD ---> PNG
        elif src_ext == '.psd':
            return [ConvertPSD(source).save(target)]

        # PDF ---> PNG
        elif src_ext == '.pdf':
            return pdf2img(source, output=target, ext=self._dst_ext)

        # JPG ---> PNG
        elif src_ext == '.jpg':
            return [jpg2png(source, target)]

        # Cannot convert this file type
        else:
            print('ImgConverter error: unsupported file type (' + src_ext + ')')
            print('File path         :', source, '\n')
