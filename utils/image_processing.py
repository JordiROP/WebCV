import base64
from pathlib import Path


def image_to_bytes(img_path: str):
    img_bytes = Path(img_path).read_bytes()
    return base64.b64encode(img_bytes).decode()
