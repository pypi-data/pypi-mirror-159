# -*- coding: utf-8 -*-

domain_dict = {}
def load():
    with open("domain.txt") as f:
        while True:
            line = f.readline()
            if line:
                domain, num, date = line.split(",")
                domain_dict[domain] = {"num": num, "date": date}
            else:
                break

def is_licensed(domain):
    return domain in domain_dict

# if __name__ == '__main__':
#     load()
#     print (is_licensed("gldmachinery.com"))