import re
import urllib.parse
from src.utils.init import logger


def clean_image_url(*, image_url: str) -> str:
    """Clean the image URL.

    Args:
        image_url (str): The URL of the source image.
    Returns:
        str: The cleaned image URL."""

    img_url = urllib.parse.unquote(image_url)

    if not re.match("//.*//", img_url):
        logger.error(f"Invalid image URL: {image_url}")
        raise ValueError("Invalid image URL!")

    cleaned_url = re.sub("//.*//", "https://", img_url)
    logger.debug(f"Cleaned URL: {cleaned_url}")

    return cleaned_url


def size_parse(*, size: str) -> tuple[int, int]:
    """Parse a size string into a tuple of ints.

    Args:
        size (str): The size string to parse.

    Returns:
        tuple: The parsed size string."""

    if re.match(r"^\d+x\d+$", size):
        parsed_size = tuple(map(int, size.split("x")))
    elif re.match(r"^x\d+$", size):
        parsed_size = (0, int(size.split("x")[1]))
    elif re.match(r"^\d+x$", size):
        parsed_size = (int(size.split("x")[0]), 0)
    else:
        raise ValueError("Invalid size!")

    logger.debug(f"Parsed size: {parsed_size}")

    return parsed_size


def extract_image_format(*, image_url: str) -> str:
    """Extract the image format from the URL.

    Args:
        image_url (str): The URL of the source image.

    Returns:
        str: The image format."""

    format = image_url.split("/")[-1].split(".")[-1].lower()
    logger.debug(f"Image format: {format}")

    for item in ["jpg", "jpeg", "png", "webp", "gif"]:
        if item in format:
            if item == "jpg":
                return "jpeg"
            return item

    logger.error(f"Invalid format: {format}.")
    raise ValueError("Invalid image format!")
