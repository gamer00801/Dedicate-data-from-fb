import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="大數據公司",
    version="1.1.2",
    author="gamer00801",
    author_email="yrz521@yahoo.com.tw",
    description="Python library to download post and message from https://www.facebook.com/groups/1260448967306807",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gamer00801/Costco-",
    keywords=['fb', 'post', 'message', '大數據公司',],
    packages=['大數據公司'],
)