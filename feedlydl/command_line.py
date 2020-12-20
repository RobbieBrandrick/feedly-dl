import argparse
import json
import os

from .FeedlyVideoDownloader import FeedlyVideoDownloader

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-config", help="Location of the json configuration file", default="config.json")
    args = parser.parse_args()
    
    with open(args.config) as f:
        config = json.load(f)

    downloader = FeedlyVideoDownloader(config)

    downloader.download_category()