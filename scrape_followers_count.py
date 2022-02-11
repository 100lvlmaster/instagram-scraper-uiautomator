from uiautomator import device as d
from navigate import navigate_to_profile, open_ig_from_home, scroll_to_top
from xmltocsv import email_dict, contact_dict, profile_dict
from os.path import exists
import csv
import sys

# Navigate to email page
# and return email dict


export_file = sys.argv[1] + ".csv"
import_file = sys.argv[1]


def dump_email_if_exists():
    d.wait.idle()
    d.wait.update()
    hasEmail = d(text="Email", resourceId="com.instagram.android:id/button_text").exists
    if hasEmail:
        d(text="Email", resourceId="com.instagram.android:id/button_text").click()
        d.wait.idle()
        d.wait.idle()
        email_xml = d.dump()
        d.press.back()
        d.press.back()
        data = email_dict(email_xml)
        return data
    # return empty dict
    return {"email": ""}


def dump_contact_if_exists():
    has_contact = d(text="Contact").exists
    if has_contact:
        d(text="Contact").click()
        d.wait.update()
        d.wait.idle()
        contact_xml = d.dump()
        data = contact_dict(contact_xml)
        d.press.back()
        return data
    return {"contact": "", "email": ""}


def dump_profile():
    d.wait.idle()
    d.wait.idle()
    profile_xml = d.dump()
    data = profile_dict(profile_xml)
    return data


def init_dump():
    email = dump_email_if_exists()
    contact = dump_contact_if_exists()
    if not contact["contact"] and not email["email"] and not contact["email"]:
        return {}
    contact.update(email)
    profile = dump_profile()
    data = profile | contact
    return data


def browse_profiles():
    follow_list = d(resourceId="com.instagram.android:id/follow_list_username")
    count = len(follow_list)
    for index in range(count):
        follow_list[index].click()
        init_dump()
        d.press.back()
        if index == (count - 1):
            scroll_to_top()


def init_users_csv():
    file_exists = exists(export_file)
    if not file_exists:
        file = open(export_file, "+a")
        csv_writer = csv.writer(file)
        header = ["username", "followers_count"]
        csv_writer.writerow(header)
        file.close()
    # Create file with header


def dump_csv(user_dict: dict):
    file = open(export_file, "a+")
    csv_writer = csv.writer(file)
    csv_writer.writerow(user_dict.values())
    file.close()


offset = 0
limit = 500


def main():
    init_users_csv()
    file = open(sys.argv[1], "r")
    usernames = "".join(file.readlines()).split("\n")
    file.close()
    d.press.home()
    open_ig_from_home()
    for idx, val in enumerate(usernames):
        print(idx)
        if not val:
            continue
        if idx < offset:
            continue
        if idx > (offset + limit):
            print("Scrape completed")
            break
        try:
            profile_exists = navigate_to_profile(val)
        except:
            continue
        if not profile_exists:
            d.press.back()
            d.press.back()
            continue
        followers_count = d(
            resourceIdMatches="com.instagram.android:id/row_profile_header_textview_followers_count"
        )
        count = followers_count.info["text"]
        data = {"username": val, "followers_count": count}
        if bool(data):
            dump_csv(data)
        d.wait.update()
    # open_followings()
    # browse_profiles()
    # click_explore()


main()
