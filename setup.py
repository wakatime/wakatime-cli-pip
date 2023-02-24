from setuptools import setup
from wakatime.install_cli import main

version_info = ("14", "0", "1")
about = {
    "title": "wakatime",
    "description": "Command line interface to WakaTime used by all WakaTime text editor plugins.",
    "url": "https://github.com/wakatime/wakatime-cli-pip",
    "version_info": version_info,
    "version": ".".join(version_info),
    "author": "WakaTime",
    "author_email": "support@wakatime.com",
    "license": "BSD",
    "copyright": "Copyright 2023 WakaTime, LLC",
}

main()

setup(
    name=about["title"],
    version=about["version"],
    license=about["license"],
    description=about["description"],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author=about["author"],
    author_email=about["author_email"],
    url=about["url"],
    packages=[about["title"]],
    package_dir={about["title"]: about["title"]},
    include_package_data=True,
    zip_safe=False,
    platforms="any",
    entry_points={
        "console_scripts": ["wakatime = wakatime.__init__:main"],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Text Editors",
    ],
)
