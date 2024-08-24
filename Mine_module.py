#Mine module.1

from hashlib import sha256
import time
from tracemalloc import start

MAX_NONCE = 100000000000
#max no of iteration of the nonce

#defining the hash function
def SHA256(text):
    return sha256(text.encode("utf-8")).hexdigest()
#mining the block

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = "0" * prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Yay! you mined Bitcoin: {nonce}")
            return new_hash
    raise BaseException(f"Couldn't find correct has after trying {MAX_NONCE} times")
if __name__ == "__main__":
    transaction = """
        Player1->Player2-200,
        Player3->Player4-450
    """
    difficulty = 20
    #This probably a higher number 10-20 or something

    #checking the time
    start = time.time()
    print("Started Mining...")
    new_hash = mine(
        5,
        transaction,
        "b5d4045c3f466fa91fe2cc6abe79232a1a57cdf104f7a26716e0a1e2789df78",
        difficulty
    )
