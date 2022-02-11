import sys

# This script will extract usernames from
# a given list of instagram profile urls


def main():
    if(sys.argv[1].endswith('txt')):
        print('invalid file, file should be a txt with names')
        exit()
    file = open(sys.argv[1], "r")
    data = file.readlines()
    file.close()
    ig_usernames = []
    for username in data:
        if not username:
            continue
        if username.startswith("@"):
            username_without_at = username.replace("@", "")
            ig_usernames.append(username_without_at)
            continue
        if not username.startswith("http"):
            ig_usernames.append(username)
            continue
        lastSlash = username.rfind("/") + 1
        firstQueryStart = username.find("?")
        ig_username = username[lastSlash:firstQueryStart]
        ig_username = ig_username.replace("@", "")
    file = open(sys.argv[1].replace(".txt", "") + "-cleaned.txt", "+a")
    for names in ig_usernames:
        file.write(names)
    file.close


main()
