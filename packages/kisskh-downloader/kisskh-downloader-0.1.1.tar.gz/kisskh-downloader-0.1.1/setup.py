# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['kisskh_downloader', 'kisskh_downloader.models']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'ffmpeg-python>=0.2.0,<0.3.0',
 'm3u8>=2.0.0,<3.0.0',
 'pydantic>=1.9.1,<2.0.0',
 'requests>=2.28.1,<3.0.0',
 'tqdm>=4.64.0,<5.0.0',
 'validators>=0.20.0,<0.21.0']

entry_points = \
{'console_scripts': ['kisskh = kisskh_downloader.cli:kisskh']}

setup_kwargs = {
    'name': 'kisskh-downloader',
    'version': '0.1.1',
    'description': 'Simple downloaded for https://kisskh.me/',
    'long_description': '# kisskh-dl\n\nSimple downloaded for https://kisskh.me/\n\n---\n\n## Installation\n\n```console\npip install kisskh-downloader\n```\n\nRight now we are using ffmpeg to convert the downloaded stream file to some other format (.mp4, .mkv, .avi etc.). Follow the instruction [here](https://github.com/kkroening/ffmpeg-python#installing-ffmpeg) to install ffmpeg. Note if ffmpeg is not found then no conversion will take place. Also stream files will not be deleted.\n\n---\n\n> **NOTE:** Although of now the video files downloaded are in [.ts](https://en.wikipedia.org/wiki/MPEG_transport_stream) format, you can still use players like [VLC](https://www.videolan.org/) to play the video.\n\n## Usage\n\n```console\nkisskh dl --help\nUsage: kisskh dl [OPTIONS] DRAMA_URL_OR_NAME\n\nOptions:\n  -f, --first INTEGER             Starting episode number.\n  -l, --last INTEGER              Ending episode number.\n  -q, --quality [360p|480p|540p|720p|1080p]\n                                  Quality of the video to be downloaded.\n  -o, --output-dir TEXT           Output directory where downloaded files will\n                                  be store.\n  -fd, --force-download           Select nearest video quality if expected one\n                                  not available.\n  -cs, --convert-stream-to TEXT   Convert the stream (.ts) to other format\n                                  (.mkv, .mp4, .avi etc.).\n  -ks, --keep-stream-file         Keep the .ts format after the conversion is\n                                  done.\n  --help                          Show this message and exit.\n```\n\n### Direct download entire series in highest quality available\n\n```console\nkisskh dl "https://kisskh.me/Drama/Money-Heist--Korea---Joint-Economic-Area?id=5044"\n```\n\n### Search and download entire series in highest quality available\n\n```console\nkisskh dl "Stranger Things"\n1. Stranger Things - Season 4\n2. Stranger Things - Season 1\n3. Stranger Things - Season 2\n4. Stranger Things - Season 3\nPlease select one from above: 1\n```\n\n### Download specific episodes with specific quality\n\nDownloads episode 4 to 8 of `Alchemy of Souls` in 720p:\n```console\nkisskh dl "https://kisskh.me/Drama/Alchemy-of-Souls?id=5043" -f 4 -l 8 -q 720p -fd\n```\n\nDownloads episode 3 of `A Business Proposal` in 720p:\n```console\nkisskh dl "https://kisskh.me/Drama/A-Business-Proposal?id=4608" -f 3 -l 3 -q 720p -fd\n```\n\n---\n\n# TODO\n- [x] Add ability to export video in other format using ffmpeg\n- [ ] Add unit test\n- [x] Handle Ctrl + C signal in terminal\n- [ ] Throw appropriate exception or handles it somehow\n    - [ ] In valid URL pass\n    - [ ] Video file not present\n- [ ] Add option to download subtitles\n- [ ] Enable CI/CD for linting (flake8), formatting (black and isort) and security (bandit)\n- [ ] Add ability to export all download link\n- [ ] Add ability to open stream in some player',
    'author': 'Debakar Roy',
    'author_email': 'allinonedibakar@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
