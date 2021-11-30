
from uiautomator import device as d


def navigate_to_profile(name: str):
    click_explore()
    click_explore()
    d(text='Search').click()
    d(className="android.widget.EditText").set_text(name)
    d(text=name).click()


def click_explore():
    d(description="Search and Explore").click()


def open_ig_from_home():
    d.press.home()
    d(descriptionMatches="Instagram").click()


def open_followings():
    d(textContains="Following").click()
