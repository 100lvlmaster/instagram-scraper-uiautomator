import time
import os


def createDir():
    directory = f'{time.time_ns()}'
    path = os.path.join('dumps', directory)
    print(path)
    try:
        print("Directory '%s' created successfully" % directory)
        os.makedirs(path, exist_ok=True)
    except OSError as error:
        print("Directory '%s' can not be created" % directory)
    return path

# Send file with full path


def dumpXml(data: str, path: str):
    f = open(path, "w")
    f.write(data)
    f.close()


def dump_profile_xml(xml_dump: str, path: str):
    dumpXml(xml_dump, f'{path}/profile.xml')


def dump_contact(xml_dump: str, path: str):
    dumpXml(xml_dump, f'{path}/contact.xml')


def dump_email(xml_dump: str, path: str):
    dumpXml(xml_dump, f'{path}/email.xml')
