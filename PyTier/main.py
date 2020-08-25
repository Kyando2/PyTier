import requests
import re
import time


expr = re.compile("(?<=\ |\>)(\d\-[A-C])(?=\<|\ )")
expr2 = re.compile(r'(?<=href\=\")(.*?)(?=\"\ class\=\"result\-link\")')
URL = "https://vsbattles.fandom.com/wiki"


def get_tier(char: str, verbose=False, amount=3):
    '''
    `Pub meth`
    '''
    tier_list = []
    url = URL + "/Special:Search?query=" + char
    if verbose:
        print("> Obtaining " + url + " <")
    r = requests.get(url)
    new_url = expr2.findall(
        r.text
        )
    if len(new_url) < amount: amount = len(new_url)
    for x in range(amount):
        time.sleep(.3)
        if verbose:
            print("> Obtaining " + new_url[x] + " <")
        r2 = requests.get(new_url[x])
        tiers = expr.findall(
            r2.text
            )
        if verbose:
            print(tiers)
        tier_list.extend(tiers)
    tier = find_lowest(tier_list)
    return tier
    
def find_lowest(tiers):
    lowest = "11-C"
    for v in tiers:
        lowest = compare(v, lowest)
    return lowest

def compare(x: str, y: str) -> str:
    ax = to_int(x)
    ay = to_int(y)
    if ax>ay: return y
    elif ax<ay: return x
    else: return y

def to_int(tier: str) -> int:
    return int(str(tier)
               .replace("C", "3")
               .replace("B", "2")
               .replace("A", "1")
               .replace("-", ""))
