# Windows 10 Toast Notifications
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)  [![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fjithurjacob%2FWindows-10-Toast-Notifications.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fjithurjacob%2FWindows-10-Toast-Notifications?ref=badge_shield) [![HitCount](http://hits.dwyl.io/jithurjacob/Windows-10-Toast-Notifications.svg)](http://hits.dwyl.io/jithurjacob/Windows-10-Toast-Notifications) [![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

An easy-to-use Python library for displaying Windows 10 Toast Notifications which is useful for Windows GUI development.


![o7ja4 1](https://cloud.githubusercontent.com/assets/7101452/19763806/75f71ba4-9c5d-11e6-9f16-d0d4bf43e63e.png)


## Installation

```
pip install win10toast
```

## Requirements

### Installation of pywin32
```
pypiwin32
setuptools
```

## Example

```
from win10toast import ToastNotifier
toaster = ToastNotifier()
toaster.show_toast("Hello World!!!",
                   "Python is 10 seconds awsm!",
                   icon_path="custom.ico",
                   duration=10)

toaster.show_toast("Example two",
                   "This notification is in it's own thread!",
                   icon_path=None,
                   duration=5,
                   threaded=True)
# Wait for threaded notification to finish
while toaster.notification_active(): time.sleep(0.1)
```

## Compatibility with other Windows OSe

The library also works with nonWin10-OSes, so feel free to use it on Windows 7 as well...

![Win7img](http://justpic.info/images4/8f3b/2018112513_25_30computerhpTightVNCViewer.png)

## Contributors [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/jithurjacob/Windows-10-Toast-Notifications/issues)

+ [sidc9](https://github.com/sidc9)
+ [sakurai-youhei](https://github.com/sakurai-youhei)
+ [BroderickCarlin](https://github.com/BroderickCarlin)
+ [florianluediger](https://github.com/florianluediger)
+ [eric-wieser](https://github.com/eric-wieser)
+ [Guts](https://github.com/Guts)


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fjithurjacob%2FWindows-10-Toast-Notifications.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fjithurjacob%2FWindows-10-Toast-Notifications?ref=badge_large)
