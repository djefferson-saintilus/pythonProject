import requests
from bs4 import BeautifulSoup

"""
---ideas for chatgpt
$groseria=[cagando, mierda, verga, puta, perra, cabron, cojon]

$forums=["quora.com","reddit.com","stackoverflow.com", "youtube.com", "twitter.com", "wattpad.com"]

if $groseria in $forums then how many times $groseria repeat in $forums
else
no groseria found

use the search bar to look for the groseria words but limit it to the 50
result found, then show what he foundm but try to be more user-friendly

after that if the program found a total of 50 groseria word, in 
each $forums so this $forums is not recommended for child,
elseif it's not too bad for child, else let your
go there it's safe
"""
import requests
from bs4 import BeautifulSoup

groseria = ['cagando', 'mierda', 'verga', 'puta', 'perra', 'cabron', 'cojon']
forums = ["quora.com", "reddit.com", "stackoverflow.com", "youtube.com", "twitter.com", "wattpad.com"]

# initialize counters
groseria_count = 0
page_count = 0

# iterate over each forum
for forum in forums:
    # initialize forum counter
    forum_count = 0
    # iterate over each groseria word
    for g in groseria:
        # make a request to the forum's search page for the groseria word
        response = requests.get(f"https://{forum}/search?q={g}")
        # parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # search for each groseria in the search results
        count = soup.text.count(g)
        groseria_count += count
        forum_count += count
    # increment the page count
    page_count += 1
    # print forum results
    if forum_count >= 50:
        print(f"\n{forum} is not recommended for child.")
    elif forum_count > 0:
        print(f"\n{forum} is not too bad for child.")
    else:
        print(f"\n{forum} is safe for your child to go to.")

# check if any groseria was found
if groseria_count > 0:
    print(f"\nTotal number of groseria instances found: {groseria_count} in {page_count} pages.")
else:
    print("\nNo groseria found.")
