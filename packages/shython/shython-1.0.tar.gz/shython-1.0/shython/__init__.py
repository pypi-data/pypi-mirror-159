from PIL import Image
from io import BytesIO
from base64 import b64encode
try:
	from urllib import request
except ImportError:
	from urllib import urlopen

__version__: str = '1.0'
__author__: str = 'Shayan Heidari'
__copyright__: str = 'copyright 2022'

class Files(object):
	class getImageSize(object):
		def __init__(self, Image_Bytes: bytes) -> tuple:
			"""
				You can get the size of a photo with this method. To get the size of the photo, you must give the bytes of the photo to the argument of this method. This method returns the image size as a tuple
	
				For example:
					(1, 1)
	
				The first number in the tuple is the width of the photo and the second number is the length of the photo
			"""
			image = Image.open(BytesIO(Image_Bytes))
			self.size = image.size

	class getImageThumbnail(object):
		def __init__(self, Image_Bytes: bytes) -> str:
			"""
				With the help of this method, you can get a thumbnail of a photo in base64 encryption
			"""
			image = Image.open(BytesIO(Image_Bytes))
			(width , height) = image.size
			if height > width:
				new_height: int = 40
				new_width: int = round(new_height * width / height)
			else:
				new_width: int = 40
				new_height: int = round(new_width * height / width)
			image = image.resize((new_width, new_height), Image.ANTIALIAS)
			changed_image = BytesIO()
			image.save(changed_image, format='PNG')
			changed_image = changed_image.getvalue()
			self.thumbnail = b64encode(changed_image)

	class getFileFormat(object):
		def __init__(self, FileName : str):
			self.suffix : str = FileName.split('.')[-1]

class Network(object):
	class Get(object):
		def __init__(self, url: str):
			result = request.urlopen(url)
			self.text = result.read().decode('utf-8')

	class Post(object):
		def __init__(self, url: str, data = None, headers = None):
			if data != None:
				if data == bytes:
					result = request.urlopen(request.Request(url, data = data , headers = headers))

				else:
					data = data.encode()
					result = request.urlopen(request.Request(url, data = data , headers = headers))
			self.text = result.read()