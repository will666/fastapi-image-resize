# type: ignore

import pytest
from src.image_resize import get_aspect_ratio, resize_image, fetch_image


def test_get_aspect_ratio() -> None:
    """Test the get_aspect_ratio function."""
    assert get_aspect_ratio(size=(100, 100), img_size=(100, 100)) == (100, 100)
    assert get_aspect_ratio(size=(0, 100), img_size=(100, 100)) == (100, 100)
    assert get_aspect_ratio(size=(100, 0), img_size=(100, 100)) == (100, 100)
    assert get_aspect_ratio(size=(150, 0), img_size=(200, 180)) == (150, 135)
    assert get_aspect_ratio(size=(0, 0), img_size=(100, 100)) != (100, 100)
    with pytest.raises(TypeError):
        get_aspect_ratio(size=("xxx", "ddd"), img_size=(100, 100))
    with pytest.raises(TypeError):
        get_aspect_ratio(size=(100, 100), img_size=("xxx", "ddd"))
    with pytest.raises(TypeError):
        get_aspect_ratio(size=[100, 100], img_size=(100, 100))


def test_fetch_image() -> None:
    """Test the fetch_image function."""
    assert fetch_image(
        url="https://www.w3.org/People/mimasa/test/imgformat/img/w3c_home.jpg"
    )
    with pytest.raises(ValueError):
        fetch_image(url="https://i.imgur.com/1.jpg")


def test_resize_image():
    """Test the resize_image function."""
    assert resize_image(
        url="https://www.w3.org/People/mimasa/test/imgformat/img/w3c_home.gif",
        size=(100, 100),
    )
    with pytest.raises(ValueError):
        resize_image(url="https://i.imgur.com/1.tiff", size=(100, 100))
    with pytest.raises(ValueError):
        resize_image(url="https://i.imgur.com/1.bmp", size=(100, 100))
    with pytest.raises(ValueError):
        resize_image(url="https://i.imgur.com/1.svg", size=(100, 100))
    with pytest.raises(ValueError):
        resize_image(url="https://i.imgur.com/1.jpg", size=(0, 0))
    with pytest.raises(TypeError):
        resize_image(
            url="https://www.w3.org/People/mimasa/test/imgformat/img/w3c_home.jpg",
            size=("xxx", "ddd"),
        )
    with pytest.raises(TypeError):
        resize_image(
            url="https://www.w3.org/People/mimasa/test/imgformat/img/w3c_home.jpg",
            size=(100, 100, 100),
        )
    with pytest.raises(TypeError):
        resize_image(url=100, size=(100, 100))
    with pytest.raises(TypeError):
        resize_image(url="test", size="test")
