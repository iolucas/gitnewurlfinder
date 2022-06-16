import requests

import itertools

import tqdm

import random

import time

available_urls_f = open("available_users.txt", "a")
not_available_urls_f = open("not_available_users.txt", "a")

def write_found_url(url):
    open("README.md", "a").write("\n* " + url)


def flush_files():
    global available_urls_f
    global not_available_urls_f

    available_urls_f.close()
    available_urls_f = open("available_users.txt", "a")
    not_available_urls_f.close()
    not_available_urls_f = open("not_available_users.txt", "a")



def check_git_url_free(url, wait_time=5):

    req_status_code = requests.get(f"https://github.com/{url}").status_code

    if req_status_code == 404:
        available_urls_f.write("\n" + url)
    elif req_status_code == 200:
        not_available_urls_f.write("\n" + url)
    elif req_status_code == 429:
        print(url, f"Too many requests error. Awaiting {wait_time} seconds...")
        time.sleep(wait_time)
        check_git_url_free(url)
    else:
        print("Erro:", url, req_status_code)

if __name__ == '__main__':

    consonants = "bcdfghjklmnpqrstvwxyz"
    vowels = "aeiou"
    numbers = "0123456789"
    hyphen = "-"

    available_urls = [l[:-1] if l[-1] == "\n" else l for l in open("available_users.txt", "r").readlines()]
    not_available_urls = [l[:-1] if l[-1] == "\n" else l for l in open("not_available_users.txt", "r").readlines()]
    
    already_check_urls = set(available_urls + not_available_urls)

    print("Amount of already checked users: ", len(already_check_urls))

    #characters = "l"
    #characters1 = "abcdefghijklmnopqrstuvwxyz0123456789-"
    #characters2 = "abcdefghijklmnopqrstuvwxyz0123456789"
    #characters3 = "abcdefghijklmnopqrstuvwxyz"

    #n_characters = 2
    #char_groups = [characters] + [characters3] * n_characters

    #char_groups = [consonants] + [vowels] + [consonants] + [vowels]
    #char_groups = [consonants] + [vowels] + [vowels] + [consonants]
    #char_groups = ["l"] + [vowels] + [vowels+consonants] + [vowels+consonants]
    #char_groups = [vowels+consonants+numbers] + [vowels+consonants+numbers] + [vowels+consonants+numbers]
    #char_groups = [vowels+consonants] + [vowels+consonants+numbers] + [vowels+consonants+numbers]
    #char_groups = ["l"] + ["u"] + ["c"] + [vowels+consonants+numbers] + [vowels+consonants+numbers]
    char_groups = ["l"] + ["u"] + ["c"] + [vowels+consonants+numbers]# + [vowels+consonants+numbers]
    char_groups = ["l"] + ["u"] + ["c"] + [vowels+consonants+numbers] + [vowels+consonants]

    print(char_groups)

    candidates = set(list(map("".join, itertools.product(*char_groups))))

    print("Total combinatoric users: ", len(candidates))

    candidates = list(candidates - already_check_urls)

    print("Amount of users to be checked: ", len(candidates))

    random.shuffle(candidates)

    print("Sample: ", candidates[:10])

    done_files = 0
    for candidate in tqdm.tqdm(candidates, unit="user"):
        check_git_url_free(candidate)
        done_files += 1

        if done_files % 100 == 0:
            flush_files()