from setuptools import setup

setup(name='ProgImageClient',
      version='0.1',
      description='A simple client for ProgImage server',
      install_requires=["requests==2.19.1",
                        "Pillow==5.2.0"],
      url='http://github.com/discort/ProgImageClient',
      author='Alex Rychyk',
      author_email='odiscort@gmail.com',
      license='MIT',
      packages=['prog_image_client'],
      zip_safe=False)
