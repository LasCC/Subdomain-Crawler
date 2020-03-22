import requests
import optparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--domain", dest="domain", help="Domain that you want to crawl")
    parser.add_argument("-w", "--worlist", dest="wordlist", help="Wordlist default is in the working directory", default="./wordlist.txt")
    options = parser.parse_args()
    if not options.url:
        parser.error("[!] Please add an domain to proceed, --help for more informations.")
    if not options.wordlist:
        parser.error("[!] Please add a wordlist to proceed, --help for more informations.")
    return options

def req(url):
    try:
        return requests.get("https://" + url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "google.com"
with open("./wordlist.txt", "r") as wordlist:
    for l in wordlist:
        w = l.strip()
        url = w + "." + target_url
        res = req(url)
        if res:
            print("[+] Subdomain found ! > " + str(url))