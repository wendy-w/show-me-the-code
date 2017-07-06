import string, random

def gen_keys(nums=20):
    keys = []
    for i in range(nums):
        keys.append("-".join("".join([random.choice(string.ascii_letters+string.digits) for j in range(5)]) for k in range(4)))
    print(keys)
    return keys
    
if __name__ =="__main__":
    gen_keys(200)
    