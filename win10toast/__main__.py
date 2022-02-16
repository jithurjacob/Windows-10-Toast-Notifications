from win10toast import ToastNotifier
import time

# #############################################################################
# ###### Stand alone program ########
# ###################################
if __name__ == "__main__":
    # Example simple use
    toaster = ToastNotifier()
    toaster.show_toast(
        "Hello World!!!",
        "Python is 10 seconds awsm!")
    toaster.destroy()
    
    # Example with case
    with toaster:
        toaster.show_toast(
            "Hello World!!!",
            "Python is 10 seconds awsm!")

    # Example with threaded
    toaster.show_toast(
        "Example two",
        "This notification is in it's own thread!",
        icon_path=None,
        threaded=True
        )
    # Wait for threaded notification to finish
    while toaster.notification_active(): time.sleep(0.1)
    toaster.destroy()
