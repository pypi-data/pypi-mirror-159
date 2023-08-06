# link2mp4

Download videos as MP4 files

## Get geckodriver

### Linux (Debian)

```sh
sudo apt install wget ffmpeg firefox-esr -y
wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz
sudo tar xvzf geckodriver-v0.30.0-linux64.tar.gz -C /usr/bin/
chmod +x /usr/bin/geckodriver
rm geckodriver-v0.30.0-linux64.tar.gz
```

### Windows

[Download](https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-win64.zip) and add to PATH

## Installation

### From PyPI

```sh
pip3 install link2mp4
```

### From GitHub

```sh
pip3 install git+https://github.com/Hamagnivim/link2mp4
```

## Usage

Type `link2mp4` in the console
