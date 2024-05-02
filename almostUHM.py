from hashlib import sha224, sha256, sha384, sha512
from re import findall
from typing import Callable

# Create a list of Hash Methods
hash_methods: list = [
    sha224,
    sha256,
    sha384,
    sha512
]

# A function to generate a random Number based on a seed
def randomize(seed: int) -> int:
    hashed_value = sha512(str(seed).encode()).hexdigest()
    regex = r".{1,10}"
    hashed_value = findall(regex, hashed_value)
    hashed_value = sum([int(i,16) for i in hashed_value]) 
    return hashed_value % 2147483647

# A function to generate a Hash function based on a seed
def generateProceduralHashFunction(seed: int) -> Callable[[str], str]:
    """
    Usage:
    import almostUHM
    hash_method = almostUHM.generateProceduralHashFunction(1234567890)
    hash = hash_method('Hello World')
    print(hash)
    """
    seed: int = int(seed)
    seed = randomize(seed)
    def proceduralHashFunction(string: str) -> str:
        combined_string = string + str(seed)
        method = hash_methods[seed % (len(hash_methods)- 1)]
        hashed = method(combined_string.encode()).hexdigest()
        return hashed
    return proceduralHashFunction
