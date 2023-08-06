# kisskh-dl

Simple downloaded for https://kisskh.me/

---

## Installation

```console
pip install kisskh-downloader
```

Right now we are using ffmpeg to convert the downloaded stream file to some other format (.mp4, .mkv, .avi etc.). Follow the instruction [here](https://github.com/kkroening/ffmpeg-python#installing-ffmpeg) to install ffmpeg. Note if ffmpeg is not found then no conversion will take place. Also stream files will not be deleted.

---

> **NOTE:** Although of now the video files downloaded are in [.ts](https://en.wikipedia.org/wiki/MPEG_transport_stream) format, you can still use players like [VLC](https://www.videolan.org/) to play the video.

## Usage

```console
kisskh dl --help
Usage: kisskh dl [OPTIONS] DRAMA_URL_OR_NAME

Options:
  -f, --first INTEGER             Starting episode number.
  -l, --last INTEGER              Ending episode number.
  -q, --quality [360p|480p|540p|720p|1080p]
                                  Quality of the video to be downloaded.
  -o, --output-dir TEXT           Output directory where downloaded files will
                                  be store.
  -fd, --force-download           Select nearest video quality if expected one
                                  not available.
  -cs, --convert-stream-to TEXT   Convert the stream (.ts) to other format
                                  (.mkv, .mp4, .avi etc.).
  -ks, --keep-stream-file         Keep the .ts format after the conversion is
                                  done.
  --help                          Show this message and exit.
```

### Direct download entire series in highest quality available

```console
kisskh dl "https://kisskh.me/Drama/Money-Heist--Korea---Joint-Economic-Area?id=5044"
```

### Search and download entire series in highest quality available

```console
kisskh dl "Stranger Things"
1. Stranger Things - Season 4
2. Stranger Things - Season 1
3. Stranger Things - Season 2
4. Stranger Things - Season 3
Please select one from above: 1
```

### Download specific episodes with specific quality

Downloads episode 4 to 8 of `Alchemy of Souls` in 720p:
```console
kisskh dl "https://kisskh.me/Drama/Alchemy-of-Souls?id=5043" -f 4 -l 8 -q 720p -fd
```

Downloads episode 3 of `A Business Proposal` in 720p:
```console
kisskh dl "https://kisskh.me/Drama/A-Business-Proposal?id=4608" -f 3 -l 3 -q 720p -fd
```

---

# TODO
- [x] Add ability to export video in other format using ffmpeg
- [ ] Add unit test
- [x] Handle Ctrl + C signal in terminal
- [ ] Throw appropriate exception or handles it somehow
    - [ ] In valid URL pass
    - [ ] Video file not present
- [ ] Add option to download subtitles
- [ ] Enable CI/CD for linting (flake8), formatting (black and isort) and security (bandit)
- [ ] Add ability to export all download link
- [ ] Add ability to open stream in some player