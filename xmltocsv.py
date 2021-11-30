import os
from os.path import isfile, join
from os import listdir, path
from typing import Generator
import xmltodict
import json
dumps_dir = path.join('dumps')
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


def profile_xml_file(val: str):
    return os.path.join(dumps_dir, val, 'profile.xml')

# Check if profile.xml exists if yes then parse and save to csv


key = '@resource-id'
value = 'com.instagram.android:id/profile_header_bio_text'


def node_by_kv(var, key, value) -> Generator:
    if isinstance(var, dict):
        for k, v in var.items():
            if k == key and v == value:
                yield var
            if isinstance(v, (dict, list)):
                yield from node_by_kv(v, key, value)
    elif isinstance(var, list):
        for d in var:
            yield from node_by_kv(d, key, value)


def profile_to_csv(profile_xml: str):
    xml = xmltodict.parse(profile_xml)
    data = {
        "bio": from_xml(xml, 'com.instagram.android:id/profile_header_bio_text'),
        "category": from_xml(xml,  "com.instagram.android:id/profile_header_business_category"),
        "name": from_xml(xml,  "com.instagram.android:id/profile_header_full_name"),
        "username": from_xml(xml, "com.instagram.android:id/action_bar_title"),
    }
    print(data)
    return data


def from_xml(data,  resource_val, resource_id="@resource-id"):
    return dict(node_by_kv(data, resource_id, resource_val).__next__())['text']


def main():
    dirs = [f for f in listdir(
        dumps_dir) if not isfile(join(dumps_dir, f))]
    for val in dirs:
        profile_to_csv(val)
        break
        # hasContact = isfile(os.path.join(dumps_dir, val, 'contact.xml'))
        # hasEmail = isfile(os.path.join(dumps_dir, val, 'email.xml'))


main()
