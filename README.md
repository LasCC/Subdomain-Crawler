# Subdomain crawler 

Brute force domain with a wordlist and return all the code 200 response.

# Tech part

This script uses a number of open source projects to work properly:

- requests
- argparse
- python

### Usage

```
usage: main.py [-h] [-d DOMAIN] [-w WORDLIST]

optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Domain that you want to crawl
  -w WORDLIST, --worlist WORDLIST
                        Wordlist default is in the working directory
```

```
python main.py -d google.com -w [default wordlist is in the repo]
```

### Pictures

[![N|Solid](https://i.imgur.com/beKSyik.png)](https://i.imgur.com/beKSyik.png)

@LasCC
