import hashlib
secret_mod = 18446744073709551615

# Doesn't actually add any cryptographic complexity
def generate_token(fsuid):
    return int(hashlib.sha256(fsuid.encode()).hexdigest(), 16) % secret_mod

def check_token(token, fsuid):
    hashed_fsuid = int(hashlib.sha256(fsuid.encode()).hexdigest(), 16) % secret_mod
    return hashed_fsuid == token
