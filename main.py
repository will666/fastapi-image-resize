import io
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from src.helpers import size_parse, extract_image_format, clean_image_url
from src.image_resize import resize_image

app = FastAPI()


@app.get("/")
def read_root() -> dict:
    """Ping the API."""

    return {"ping": "pong"}


@app.get("/api/v1/resize/{size}{image_url:path}")
def resize_img(size: str, image_url: str) -> StreamingResponse:
    """Resize an image from a URL to a given size.

    Args:
        size (str): The size to resize the image to.
        image_url (str): The URL of the image.

    Returns:
        StreamingResponse: The resized image."""

    parsed_size = size_parse(size=size)
    cleaned_url = clean_image_url(image_url=image_url)
    img_format = extract_image_format(image_url=cleaned_url)

    img = resize_image(url=cleaned_url, size=parsed_size)

    img_byte_arr = io.BytesIO()
    img.save(fp=img_byte_arr, format=img_format.upper())
    img_byte_arr = img_byte_arr.getvalue()

    return StreamingResponse(content=io.BytesIO(img_byte_arr), media_type=f"image/{img_format.lower()}")
