import sys

# This script will extract usernames from
# a given list of instagram profile urls


def main():
    file = open(sys.argv[1], 'r')
    data = file.readlines()
    file.close()
    ig_usernames = []
    for username in data:
        if not username:
            continue
        lastSlash = username.rfind("/")+1
        firstQueryStart = username.find("?")
        ig_usernames.append(username[lastSlash: firstQueryStart])
    file = open(sys.argv[1]+".txt", "+a")
    for names in ig_usernames:
        file.write(names+'\n')
    file.close


main()
