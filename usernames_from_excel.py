

def main():

    file = open('fashion-influencers.csv', 'r')
    data = file.readlines()
    file.close()
    ig_usernames = []
    for username in data:
        if not username:
            continue
        lastSlash = username.rfind("/")+1
        firstQueryStart = username.find("?")
        ig_usernames.append(username[lastSlash: firstQueryStart])
    file = open('influencers.txt', "+a")
    for names in ig_usernames:
        file.write(names+'\n')
    file.close


main()
