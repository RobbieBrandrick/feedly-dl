
# feedly-dl

Download unread videos by category on feedly

This tool allows me to download all the videos from my Feedly account using youtube-dl. I wanted to build this to queue up all the videos while I am on wifi on my android device. That way, I don't have to use precious mobile data or download videos one at a time.

## Installation

You should be able to install this using pip as follows

```bash
pip install git+httpshttps://github.com/RobbieBrandrick/Python
```

## Usage

You'll run the feedly-dl command from the command line and you will need a json configuration file containing the following fields.

### config.json

```json
{
    "token": "A6JDwdxXe9bd3AdqX_6ZmgjEGyvqy-i1ofJW-Kv86DX16Egc22lODZcrJsO52SFvVNYWkT8zK9DjxBfHsDV49rxsq8Lm16Ems6_kGdrlhlSUunkoMhNvTjmJNOEadhzEW3djBtIBVnzEuV5TmmWMOZYkTEYgp7v4T_oGf3OzfxtScTvT-lTdNH5xoDcugsFcxmWU56ykB_VmVbZ0lMuk2agwAo35bh51tg75cApqS-vvvUbg:feedly",
    "directory": "./videos",
    "category": "Health",
    "youtube-dl-options": {
        "ratelimit": 512000,
        "format": "bestvideo[height<=?720][fps<=?30][vcodec!=?vp9]+bestaudio/best"
    }
```

### usage

```bash
feedly-dl
```

or

```bash
feedly-dl -config <your config file>
```
