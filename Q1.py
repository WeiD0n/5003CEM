import random
from collections import defaultdict

def hash_function(ic_number, table_size):
    if not ic_number or len(ic_number) != 12:
        raise ValueError("IC number must be a 12-character string.")
    
    format =[int(ic_number[i:i+4]) for i in range(0, 12, 4)]
    folded = sum(format)
    hash_code = folded % table_size
    return hash_code

def generate_ic_number():
    return ''.join(random.choices('0123456789', k=12))

def insert_into_hash_table(hash_table, ic_number, hash_table_size):
    index = hash_function(ic_number, hash_table_size)
    if ic_number not in hash_table[index]:
        hash_table[index].append(ic_number)

def simulate_insertions(table_size):
    hash_table = defaultdict(list)
    ic_numbers = [generate_ic_number() for _ in range(1000)]
    for ic in ic_numbers:
        insert_into_hash_table(hash_table, ic, table_size)
    return hash_table

def num_collisions(hash_table):
    return sum(len(bucket) - 1 for bucket in hash_table.values() if len(bucket) > 1)

def run_simulations():
    table_sizes = [1009, 2003]
    for size in table_sizes:
        print("=" * 40)
        print(f"Hash Table Size: {size}")
        print("=" * 40)
        total_collisions = 0
        for round_number in range(1, 11):
            hash_table = simulate_insertions(size)
            collisions = num_collisions(hash_table)
            total_collisions += collisions
            print(f"  Round {round_number:<2}: Collisions = {collisions}")
        print("-" * 40)
        print(f"  Average Collisions over 10 rounds: {total_collisions / 10:.2f}\n")

if __name__ == "__main__":
    run_simulations()