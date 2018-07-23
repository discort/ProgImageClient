# ProgImageClient

Python (3.5 or greater) client for [ProgImage](https://github.com/discort/ProgImage)

## Getting started

1. Make sure that you set up [ProgImage](https://github.com/discort/ProgImage) locally, see description.

2. Install `ProgImageClient` using:

    `pip install git+https://github.com/discort/ProgImageClient`


## Usage

### Upload an image:

    >>> from prog_image_client import ProgImageClient
	>>> client = ProgImageClient()
	>>> with open('image.jpg', 'rb') as f:
	...   image = f.read()
	...
	>>> client.upload_image(image)
	{'id': '503a4ad2-4935-4c34-8709-424af72e14bb'}

### Get the image:

    >>> client.get_image(image_id)
    {
		'upload_time': '2018-07-23T11:24:52.460755',
		'size': 55058,
		'id': 'b4abdd78-2eb9-4c14-bddc-6c1f2bf889d1',
		'data': '<...base64 encoded image...>',
		'content_type': 'image/jpeg'
	}

### Rotation:

    >>> client.rotate(image_id, 90)
	>>> {'image': '/9j/4AAQSkZJRgABAQAA...base64_encoded'}

### Resizing:

	>>> client.resize(image_id, width=100, height=200)
	>>> {'image': '<base64_encoded image>'}