from uiautomator import device as d
from navigate import click_explore, navigate_to_profile, open_followings, open_ig_from_home
from xmltocsv import email_dict, contact_dict, profile_dict
brand: str = "urshaynesss"


# Profile
# com.instagram.android:id/profile_header_bio_text
# com.instagram.android:id/profile_header_business_category
# com.instagram.android:id/profile_header_full_name
# com.instagram.android:id/action_bar_title
# com.instagram.android:id/contact_option_sub_text
# com.instagram.android:id/contact_option_header

# Contact
# com.instagram.android:id/contact_option_header
# com.instagram.android:id/contact_option_sub_text


# Email
# com.google.android.gm:id/spinner_account_address


# Navigate to email page
# and return email dict
def dump_email_if_exists():
    hasEmail = d(
        text="Email", resourceId="com.instagram.android:id/button_text").exists
    if(hasEmail):
        d(
            text="Email", resourceId="com.instagram.android:id/button_text").click()
        d.wait.idle()
        email_xml = d.dump()
        d.press.back()
        d.press.back()
        data = email_dict(email_xml)
        return data


def dump_contact_if_exists():
    has_contact = d(text='Contact').exists
    if(has_contact):
        d(text="Contact").click()
        d.wait.update()
        contact_xml = d.dump()
        data = contact_dict(contact_xml)
        d.press.back()
        return data


def dump_profile():
    profile_xml = d.dump()
    data = profile_dict(profile_xml)
    return data


def init_dump():
    profile = dump_profile()
    email = dump_email_if_exists()
    contact = dump_contact_if_exists()
    data = profile
    if(contact is not None):
        data = profile | contact
    if(email is not None):
        data = data | email
    return data


def scroll_to_top():
    device_info = d.info
    height = device_info['displayHeight']
    width = device_info['displayWidth']
    # From sx,sy to ex,ey
    d.swipe(width*0.5, height*0.9, width*0.5, height*0.15)


def browse_profiles():
    follow_list = d(resourceId='com.instagram.android:id/follow_list_username')
    count = len(follow_list)
    for index in range(count):
        follow_list[index].click()
        init_dump()
        d.press.back()
        if(index == (count-1)):
            scroll_to_top()


def main():
    usernames = ''
    with open('usernames.txt', 'r') as text:
        usernames = "".join(text.readlines()).split('\n')
        text.close()
    d.press.home()
    open_ig_from_home()
    for val in usernames:
        navigate_to_profile(val)
        data = init_dump()
        print(data)
    d.wait.update()
    # open_followings()
    # browse_profiles()
    click_explore()


main()
