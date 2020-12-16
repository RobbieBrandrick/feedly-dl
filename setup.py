from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='feedly-dl',
    version='0.1', 
    description="Download unread videos by category on feedly",
    packages = find_packages(),
    entry_points = {
        'console_scripts': ['feedly-dl=feedlydl.command_line:main'],
    },
    dependency_links=[
        'https://github.com/ytdl-org/youtube-dl',
        'https://github.com/feedly/python-api-client'
    ]
)
