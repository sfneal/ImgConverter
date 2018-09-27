import os
from shutil import rmtree
from pathlib import Path
from tempfile import NamedTemporaryFile, mkdtemp
from psdconvert import ConvertPSD
from pdf.convert import pdf2img
from ImgConverter.jpg2png import jpg2png


class Convert2Image:
    def __init__(self, dst_directory=None, convert_to='png'):
        self._dst_dir = dst_directory
        self._dst_ext = '.' + convert_to.strip('.')
        self._tempdir = None

    def cleanup(self):
        rmtree(self._tempdir)

    @staticmethod
    def _get_name_ext(source):
        """
        Get file name and file extension from a source file

        :param source: A file path
        :return: file_name, file_ext
        """
        s = Path(os.path.basename(source))
        return s.stem, s.suffix

    def _get_target(self, src_name):
        """
        Retrieve the target file_path

        Returns either a tempfile in a tempdir or a concatenated
        file path in the same directory as the source file
        """
        if self._dst_dir and os.path.isdir(self._dst_dir):
            # Concatenate destination
            return os.path.join(self._dst_dir, src_name + self._dst_ext)

        else:
            # Create a temporary destination
            if self._tempdir is None:
                self._tempdir = mkdtemp()
            return NamedTemporaryFile(dir=self._tempdir, suffix=self._dst_ext).name

    def convert(self, source):
        """Convert a .jpg, .psd, .pdf or .png to another format"""
        # Source file name without extension and file extension tup
        src_name, src_ext = self._get_name_ext(source)

        # Target file path
        target = self._get_target(src_name)

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
