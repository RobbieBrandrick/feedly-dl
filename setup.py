from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='feedly-dl',
    version='0.1', 
    description="Download unread videos by category on feedly",
    author="Robbie Brandrick",
    url="",
    packages = find_packages(),
    install_requires = [
        'feedly-client',
        'youtube_dl'
    ],
    entry_points = {
        'console_scripts': ['feedly-dl=feedlydl.command_line:main'],
    },    
)
