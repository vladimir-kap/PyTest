import os

site = input()

if 'https://' in site:
    os.system('start ' + site)
    print()