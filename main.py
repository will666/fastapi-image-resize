import io
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from src.helpers import size_parse, extract_image_format, clean_image_url
from src.image_resize import resize_image
import asyncio

app = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
    """Ping the API."""

    return {"ping": "OK"}


@app.get("/api/v1/resize/{size}{image_url:path}")
async def resize_img(size: str, image_url: str) -> StreamingResponse:
    """Resize an image from a URL to a given size.

    Args:
        size (str): The size to resize the image to.
        image_url (str): The URL of the image.
        possible values:
            /api/v1/resize/100x100//https://example.com/image.jpg
            /api/v1/resize/x100//https://example.com/image.jpg
            /api/v1/resize/100x//https://example.com/image.jpg

    Returns:
        Async StreamingResponse: The resized image."""

    return await asyncio.to_thread(handle_request, size=size, image_url=image_url)


def handle_request(*, size: str, image_url: str) -> StreamingResponse:
    parsed_size = size_parse(size=size)
    cleaned_url = clean_image_url(image_url=image_url)
    img_format = extract_image_format(image_url=cleaned_url)

    img = resize_image(url=cleaned_url, size=parsed_size)

    img_byte_arr = io.BytesIO()
    img.save(fp=img_byte_arr, format=img_format.upper())
    img_byte_arr = img_byte_arr.getvalue()

    return StreamingResponse(content=io.BytesIO(img_byte_arr), media_type=f"image/{img_format.lower()}")
