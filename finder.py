import requests

import itertools

import tqdm

import random

import time

def write_found_url(url):
    open("README.md", "a").write("\n* " + url)


def check_git_url_free(url, wait_time=5):

    req_status_code = requests.get(f"https://github.com/{url}").status_code

    if req_status_code == 404:
        print(url)
        return True
    elif req_status_code == 200:
        pass
    elif req_status_code == 429:
        print(url, f"Too many requests error. Awaiting {wait_time} seconds...")
        time.sleep(wait_time)
        check_git_url_free(url)
    else:
        print("Erro:", url, req_status_code)

url_styles = [

]

if __name__ == '__main__':

    limit = 10000

    consonants = "bcdfghjklmnpqrstvwxyz"
    vowels = "aeiou"
    numbers = "0123456789"
    hyphen = "-"

    #characters = "l"
    #characters1 = "abcdefghijklmnopqrstuvwxyz0123456789-"
    #characters2 = "abcdefghijklmnopqrstuvwxyz0123456789"
    #characters3 = "abcdefghijklmnopqrstuvwxyz"

    #n_characters = 2
    #char_groups = [characters] + [characters3] * n_characters

    char_groups = [consonants] + [vowels] + [consonants] + [vowels]

    candidates = list(set(list(map("".join, itertools.product(*char_groups)))))

    random.shuffle(candidates)

    print("Number of candidates:", len(candidates))

    for candidate in tqdm.tqdm(candidates[:limit]):
        if check_git_url_free(candidate):
            write_found_url(candidate)