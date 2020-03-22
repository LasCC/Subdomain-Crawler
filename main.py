import requests
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--domain", dest="domain", help="Domain that you want to crawl")
    parser.add_argument("-w", "--worlist", dest="wordlist", help="Wordlist default is in the working directory", default="./wordlist.txt")
    options = parser.parse_args()
    if not options.domain:
        parser.error("[!] Please add an domain to proceed, --help for more informations.")
    if not options.wordlist:
        parser.error("[!] Please add a wordlist to proceed, --help for more informations.")
    return options

def req(url):
    try:
        return requests.get("https://" + url)
    except requests.exceptions.ConnectionError:
        pass

options = get_arguments()
target_url = str(options.domain)
with open(options.wordlist, "r") as wordlists:
    for l in wordlists:
        w = l.strip()
        url = w + "." + target_url
        res = req(url)
        if res:
            print("[+] Subdomain found ! > " + url)
