import hashlib
secret_mod = 18446744073709551615

# Doesn't actually add any cryptographic complexity
def generate_token(fsuid):
    hashed_fsuid = int(hashlib.sha256(fsuid.encode()).hexdigest(), 16) % secret_mod
    return str(hashed_fsuid)

def check_token(token, fsuid):
    hashed_fsuid = int(hashlib.sha256(fsuid.encode()).hexdigest(), 16) % secret_mod
    token = int(token)
    return hashed_fsuid == token
