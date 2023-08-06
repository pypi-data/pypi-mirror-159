import setuptools


setuptools.setup(
    name="aiom3u8",
    version="1.1.0",
    author="yfd",
    author_email="yunxiaofeng2019@gmail.com",
    description="Using async way to download a video file by parsing m3u8 file",
    url="https://github.com/yfd-01/aiom3u8",
    license='MIT',
    packages=setuptools.find_packages(),
    package_data={
        'aiom3u8': ['ffmpeg.exe'],
    },
    install_requires=["aiohttp", "tqdm", "printy", "crypto"],
    python_requires='>=3.5'
)
