from hashlib import sha224, sha256, sha384, sha512
from re import findall

# Create a list of Hash Methods
hash_methods = [
    sha224,
    sha256,
    sha384,
    sha512
]

# A function to generate a random Number based on a seed
def randomize(seed):
    hashed_value = sha512(str(seed).encode()).hexdigest()
    regex = r".{1,10}"
    hashed_value = findall(regex, hashed_value)
    hashed_value = sum([int(i,16) for i in hashed_value]) 
    return hashed_value % 2147483647

# A function to generate a Hash function based on a seed
def generatePrecidualHashFunction(seed):
    seed: int = int(seed)
    seed = randomize(seed)
    def prodedualHashFunction(string):
        combined_string = string + str(seed)
        method = hash_methods[seed % (len(hash_methods)- 1)]
        hashed = method(combined_string.encode()).hexdigest()
        return hashed
    return prodedualHashFunction

seed = 1234
string = "Hello World!"
hash_method = generatePrecidualHashFunction(seed)
hash = hash_method(string)
print(hash)