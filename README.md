# Windows 10 Toast Notifications

Fork of https://github.com/jithurjacob/Windows-10-Toast-Notifications.

An easy-to-use Python library for displaying Windows 10 Toast Notifications with support for notifications that persist
in the notification center.

Update original package's interface to support persistent notifications by passing ``duration=None``.

## Installation

```
pip install win10toast-persist
```

## Requirements

### Installation of pywin32
```
pypiwin32
setuptools
```

## Example

```
from win10toast_persist import ToastNotifier
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

## Contributors [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/jithurjacob/Windows-10-Toast-Notifications/issues)

+ [sidc9](https://github.com/sidc9)
+ [sakurai-youhei](https://github.com/sakurai-youhei)
+ [BroderickCarlin](https://github.com/BroderickCarlin)
+ [florianluediger](https://github.com/florianluediger)
+ [eric-wieser](https://github.com/eric-wieser)
+ [Guts](https://github.com/Guts)


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fjithurjacob%2FWindows-10-Toast-Notifications.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fjithurjacob%2FWindows-10-Toast-Notifications?ref=badge_large)
