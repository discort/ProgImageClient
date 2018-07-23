from io import BytesIO

from PIL import Image
import requests


STORAGE_API_URL = "http://localhost:8080"
ROTATE_API_URL = "http://localhost:8081"
RESIZE_API_URL = "http://localhost:8082"


class ProgImageExeception(Exception):
    pass


class AbstractClient:
    """
    Abstract client class to work with ProgImage app
    """
    def upload_image(self, image):
        """Uploads an image to server"""
        raise NotImplementedError

    def get_image(self, image_id):
        """Get an image by image_id"""
        raise NotImplementedError

    def rotate(self, image_id, angle):
        """Rotates an image by angle"""
        raise NotImplementedError

    def resize(self, image_id, width, height):
        """Resizes an image by provided width an height"""
        raise NotImplementedError


class ProgImageClient(AbstractClient):
    def _send_request(self, url, method='POST', headers=None, **kwargs):
        if not headers:
            headers = {'Content-Type': 'application/json'}

        resp = requests.request(method=method, url=url, headers=headers, **kwargs)
        return self._process_response(resp)

    def _process_response(self, response):
        if response.status_code != 200:
            raise ProgImageExeception("Invalid response: {}".format(response.status_code))

        result = response.json()
        if not result['success']:
            raise ProgImageExeception(result['message'])

        return result['data']

    def _check_image(self, data):
        try:
            Image.open(BytesIO(data))
        except OSError:
            raise ProgImageExeception("Invalid image")

    def upload_image(self, image):
        self._check_image(image)
        headers = {'Content-Type': 'image/jpeg'}
        result = self._send_request(url="{0}/images".format(STORAGE_API_URL),
                                    headers=headers,
                                    data=image)
        return result

    def get_image(self, image_id):
        result = self._send_request(url="{0}/images/{1}".format(STORAGE_API_URL, image_id),
                                    method='GET')
        return result

    def rotate(self, image_id, angle):
        data = {
            "image_id": image_id,
            "angle": "{:d}".format(angle)
        }
        result = self._send_request(url="{0}/rotate".format(ROTATE_API_URL),
                                    json=data)
        return result

    def resize(self, image_id, width, height):
        data = {
            "image_id": image_id,
            "width": "{:d}".format(width),
            "height": "{:d}".format(height),
        }
        result = self._send_request(url="{0}/resize".format(RESIZE_API_URL),
                                    json=data)
        return result
