# wakatime-cli pip

This wraps the Go [wakatime-cli][wakatime-cli] in a Python package, replacing the [legacy Python wakatime-cli][wakatime-cli-legacy].

## Installing

    pip install wakatime

Installing runs `install_cli.py` and downloads the latest Go wakatime-cli [release][releases] to `~/.wakatime/wakatime-cli`.

## Using

    wakatime --help

For more info, see [wakatime-cli usage docs][usage].


[wakatime-cli]: https://github.com/wakatime/wakatime-cli
[wakatime-cli-legacy]: https://github.com/wakatime/legacy-python-cli
[usage]: https://github.com/wakatime/wakatime-cli#usage
[releases]: https://github.com/wakatime/wakatime-cli/releases
