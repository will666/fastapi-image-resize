from PIL import Image
from requests import request
from io import BytesIO
from src.utils.init import logger


def get_aspect_ratio(
    *, size: tuple[int, int], img_size: tuple[int, int]
) -> tuple[int, int]:
    """Compute the aspect ratio of an image.

    Args:
        size (tuple): The target size to resize the image to.
        img_size (tuple): The size of the original image source.

    Returns:
        tuple: The computed image size, keeping apect ratio."""

    if type(size) != tuple or type(img_size) != tuple:
        logger.error(f"Invalid argument object, wrong type: {size}")
        raise TypeError("Wrong object type. A tuple is required.")

    if type(size[0]) != int or type(size[1]) != int:
        logger.error(f"Invalid size arg, wrong type: {size}")
        raise TypeError("Wrong type. A tuple of integers is required.")

    if type(img_size[0]) != int or type(img_size[1]) != int:
        logger.error(f"Invalid img_size arg, wrong type: {img_size}")
        raise TypeError("Wrong type. A tuple of integers is required.")

    if size[0] == 0:
        width = img_size[0] * size[1] / img_size[1]
        height = size[1]
        aspect_ratio = (int(width), int(height))
    elif size[1] == 0:
        width = size[0]
        height = img_size[1] * size[0] / img_size[0]
        aspect_ratio = (int(width), int(height))
    else:
        aspect_ratio = size

    logger.debug(f"Aspect ratio: {aspect_ratio}")

    return aspect_ratio


def resize_image(*, url: str, size: tuple[int, int]) -> Image.Image:
    """Resize an image from a URL to a given size.

    Args:
        url (str): The URL of the image.
        size (tuple): The size to resize the image to.

    Returns:
        PIL.Image: The resized image."""

    if type(url) != str:
        logger.error(f"Invalid URL, wrong type: {url}")
        raise TypeError("Wrong type. A string is required.")

    if type(size) != tuple:
        logger.error(f"Invalid size, wrong type: {size}")
        raise TypeError("Wrong type. A tuple is required.")

    if type(size[0]) != int or type(size[1]) != int:
        logger.error(f"Invalid size, wrong type: {size}")
        raise TypeError("Wrong type. A tuple of integers is required.")

    response = fetch_image(url=url)

    image = Image.open(BytesIO(response))
    aspect_ratio = get_aspect_ratio(
        size=size, img_size=(int(image.size[0]), int(image.size[1]))
    )

    logger.debug(f"Aspect ratio: {aspect_ratio}")

    image = image.resize(aspect_ratio, Image.NEAREST)

    return image


def fetch_image(*, url: str) -> bytes:
    """Fetch an image from a URL."""

    response = request("GET", url)
    if response.status_code != 200:
        logger.error(f"Invalid response code: {response.status_code}")
        raise ValueError("Invalid response code!")
    logger.debug(f"Response status code: {response.status_code}")

    return response.content
