**FORK** 

Forked to make codes installable by pip.

~~Forked to make an EventGhost plugin for Win10 Toast Notifications.~~

# Windows-10-Toast-Notifications

An easy-to-use Python library for displaying Windows 10 Toast Notifications which is useful for windows GUI development.


![o7ja4 1](https://cloud.githubusercontent.com/assets/7101452/19763806/75f71ba4-9c5d-11e6-9f16-d0d4bf43e63e.png)

--

## Installation

Just use pip like this.

```
# pywin32 is required
pip install git+https://github.com/sakurai-youhei/Windows-10-Toast-Notifications.git
```

### Installation of pywin32

Easiest way to install pywin32 is using executable installer published at https://sourceforge.net/projects/pywin32/files/pywin32/.

## Example

```
from win10toast import WindowsBalloonTip
w = WindowsBalloonTip()
w.balloon_tip("Example one",
              "Python is 10 seconds awsm!",
              icon_path="python.ico",
              duration=10)
```
