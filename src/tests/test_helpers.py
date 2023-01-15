import pytest
from src.helpers import clean_image_url, size_parse, extract_image_format


def test_clean_image_url() -> None:
    """Test the clean_image_url function."""
    assert (
        clean_image_url(image_url="//https://i.imgur.com/1.jpg")
        == "https://i.imgur.com/1.jpg"
    )
    with pytest.raises(ValueError):
        clean_image_url(image_url="https://i.imgur.com/1.jpg")


def test_size_parse() -> None:
    """Test the size_parse function."""
    assert size_parse(size="100x100") == (100, 100)
    assert size_parse(size="100x") == (100, 0)
    assert size_parse(size="x100") == (0, 100)
    with pytest.raises(ValueError):
        size_parse(size="100")
    with pytest.raises(ValueError):
        size_parse(size="100x100x100")
    with pytest.raises(ValueError):
        size_parse(size="100x100x")
    with pytest.raises(ValueError):
        size_parse(size="x100x100")
    with pytest.raises(ValueError):
        size_parse(size="x100x")


def test_extract_image_format():
    """Test the extract_image_format function."""
    assert (
        extract_image_format(image_url="https://i.imgur.com/1.jpg") == "jpeg"
    )
    assert extract_image_format(image_url="https://i.imgur.com/1.png") == "png"
    assert extract_image_format(image_url="https://i.imgur.com/1.gif") == "gif"
    assert (
        extract_image_format(image_url="https://i.imgur.com/1.webp") == "webp"
    )
    assert (
        extract_image_format(image_url="https://i.imgur.com/1.jpeg") == "jpeg"
    )
    with pytest.raises(ValueError):
        extract_image_format(
            image_url="https://i.imgur.com/asdas/asdasd/asdasda/1.tiff"
        )
    with pytest.raises(ValueError):
        extract_image_format(
            image_url="https://i.imgur.com/asdas/asdasd/asdasda/1.bmp"
        )
    with pytest.raises(ValueError):
        extract_image_format(image_url="https://i.imgur.com/asdas/a/1.svg")
