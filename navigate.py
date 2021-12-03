from uiautomator import device as d

# This script will handle the functions that provide routing


def navigate_to_profile(name: str):
    click_explore()
    click_explore()
    d(text='Search').click()
    d(className="android.widget.EditText").set_text(name)
    profile = d(text=name)
    if not profile.exists:
        return False
    profile.click()
    d.wait.update()
    return True


def click_explore():
    d(description="Search and Explore").click()


def open_ig_from_home():
    d.press.home()
    d(descriptionMatches="Instagram").click()


def open_followings():
    d(textContains="Following").click()


def scroll_to_top():
    device_info = d.info
    height = device_info['displayHeight']
    width = device_info['displayWidth']
    # From sx,sy to ex,ey
    d.swipe(width*0.5, height*0.9, width*0.5, height*0.15)
