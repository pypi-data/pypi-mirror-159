import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.3'
PACKAGE_NAME = 'ourkids-common-frontend' 
AUTHOR = 'Jefry Zárate Ruíz' 
AUTHOR_EMAIL = 'jefryzarateruiz@gmail.com'
URL = 'https://github.com/Jefry-bot/ourkids_f'
DOWNLOAD_URL= URL + '/tarball/0.0.1'

LICENSE = 'MIT' 
DESCRIPTION = 'Librería para tener configuraciones y archivos comunes para la implementación y uso de servidores en flask.'
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8') 
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'python-dotenv',
      'flask'
      ]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    download_url=DOWNLOAD_URL,
    install_requires=INSTALL_REQUIRES,
    keywords=['testing', 'logging', 'example'],
    classifiers=[],
    license=LICENSE,
    packages= ['ourkids_f'],
    include_package_data=True
)