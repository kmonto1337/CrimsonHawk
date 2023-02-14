import os
import random
import re

def main():
    path = os.getcwd()
    files = os.listdir(path)
    matching_files = []

    for file in files:
        if file.endswith('.py'):
            matching_files.append(file)

    file_count = len(matching_files)
    random.shuffle(matching_files)

    for i in range(file_count):
        if i % 2 == 0:
            with open(matching_files[i], 'r') as f:
                content = f.read()
            subdomains = re.findall(r'\w+\.(?:com|org|net|edu|gov)', content)
            for subdomain in subdomains:
                if subdomain == '_SUBDOMAIN_':
                    print("Found _SUBDOMAIN_ in file " + matching_files[i])
                    break

    if 'done' in matching_files:
        with open('done', 'w') as f:
            f.write('done')

if __name__ == '__main__':
    main()
