from PIL import Image
from pathlib import Path


def jpg2png(source, destination):
    assert Path(source).suffix == '.jpg'
    assert Path(destination).suffix == '.png'

    with Image.open(source) as im:
        im.save(destination)
    return destination
