# FastAPI Image Resize

Simple API that resizes on the fly images from URL, standard web image formats supported.

## Parameters

Request format: http(s)://API_HOST:PORT/api/v1/resize/WIDTHxHEIGHT//IMAGE_URL
Size format:

- WIDTHxHEIGHT (eg. 100x100)
- WIDTHx (eg. 100x)
- xHEIGHT (eg. x100)

Example to fetch and resize on the fly an image to width of 100px and height of 100px.

```shell
wget http://localhost:8000/api/v1/resize/100x100//https://www.google.com/images/branding/googlelogo/1x/googlelogo_light_color_272x92dp.png
```

If the width or the height is not specified, an aspect ratio will be applied:

```shell
wget http://localhost:8000/api/v1/resize/100x//https://www.google.com/images/branding/googlelogo/1x/googlelogo_light_color_272x92dp.png
```

## Install Package Dependencies

```shell
pipenv --python 3.11
pipenv shell
pipenv install --dev
```

## Run the API

```shell
uvicorn main:app
```

The API route is http://127.0.0.1:8000/api/v1/resize/

Rename .env.example to .env for logging and debugging.

## Tests

```shell
pytest --cov
```
