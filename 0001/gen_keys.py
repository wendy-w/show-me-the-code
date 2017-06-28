import string, random

def gen_keys(nums=20):
    keys = []
    for i in range(nums):
        keys.append("".join([random.choice(string.letters+string.digits) for j in range(20)]))
    print keys
    return keys
        
if __name__ =="__main__":
    gen_keys(200)