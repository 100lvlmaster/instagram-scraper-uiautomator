import time
from uiautomator import device as d
from dump_xml import dump_email, dump_profile_xml, dump_contact, dumpXml, createDir
from navigate import click_explore, navigate_to_profile, open_followings, open_ig_from_home
import os
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

def dump_email_if_exists(path: str):
    hasEmail = d(
        text="Email", resourceId="com.instagram.android:id/button_text").exists
    if(hasEmail):
        d(
            text="Email", resourceId="com.instagram.android:id/button_text").click()
        dump_email(d.dump(), path)
        d.press.back()
        d.press.back()


def dump_contact_if_exists(path: str):
    has_contact = d(text='Contact').exists
    if(has_contact):
        d(text="Contact").click()
        d.wait.update()
        contact_dump = d.dump()
        dump_contact(contact_dump, path)
        d.press.back()


def dump_data():
    path = createDir()
    profile_dump = d.dump()
    dump_profile_xml(profile_dump, path)
    # Dump gmail
    dump_email_if_exists(path)
    # Dump contact
    dump_contact_if_exists(path)


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
        dump_data()
        d.press.back()
        if(index == (count-1)):
            scroll_to_top()


def main():
    dumpXml(d.dump('dump.xml'))
    usernames = ''
    with open('usernames.txt', 'r') as text:
        usernames = "".join(text.readlines()).split('\n')
        text.close()
    d.press.home()
    open_ig_from_home()
    for val in usernames:
        path = createDir()
        navigate_to_profile(val)
        dump_contact_if_exists(path)
        dump_email_if_exists(path)
        dump_profile_xml(d.dump(), path)
    d.wait.update()
    open_followings()
    browse_profiles()
    click_explore()


main()
