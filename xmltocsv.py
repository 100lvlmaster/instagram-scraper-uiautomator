from typing import Generator
import xmltodict

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


key = '@resource-id'
value = 'com.instagram.android:id/profile_header_bio_text'


def node_by_kv(var, key, value):
    if isinstance(var, dict):
        for k, v in var.items():
            if k == key and v == value:
                print(var)
                yield var
                raise StopIteration
            if isinstance(v, (dict, list)):
                yield from node_by_kv(v, key, value)
    elif isinstance(var, list):
        for d in var:
            yield from node_by_kv(d, key, value)


def contact_dict(contact_xml: str):
    xml = xmltodict.parse(contact_xml)
    data = {
        "contact-method": from_xml(xml, "com.instagram.android:id/contact_option_header"),
        "contact": from_xml(xml, "com.instagram.android:id/contact_option_sub_text")
    }
    return data


def email_dict(email_xml: str):
    xml = xmltodict.parse(email_xml)
    data = {
        "email": from_xml(xml, "com.google.android.gm:id/spinner_account_address")
    }
    return data


def profile_dict(profile_xml: str):
    xml = xmltodict.parse(profile_xml)
    data = {
        "bio": from_xml(xml, 'com.instagram.android:id/profile_header_bio_text'),
        "category": from_xml(xml,  "com.instagram.android:id/profile_header_business_category"),
        "name": from_xml(xml,  "com.instagram.android:id/profile_header_full_name"),
        "username": from_xml(xml, "com.instagram.android:id/action_bar_title"),
    }
    return data


def from_xml(data,  resource_val, resource_id="@resource-id"):
    data = node_by_kv(data, resource_id, resource_val)
    val = data.__next__()
    text = dict(val)['@text']
    return text
