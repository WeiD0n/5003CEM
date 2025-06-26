import random
from collections import defaultdict
from datetime import datetime, timedelta

state_codes = [
    '01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16',
    '21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36',
    '37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52',
    '53','54','55','56','57','58','59'
]

country_codes = [
    '60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75',
    '76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91',
    '92','93','94','95','96','97','98','99'
]

all_codes = state_codes + country_codes

def generate_valid_date():
    start_date = datetime(1950, 1, 1)
    end_date = datetime(2023, 12, 31)
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.strftime('%y%m%d')

def generate_ic_number(existing_suffixes):
    birthdate = generate_valid_date()
    state_or_country_code = random.choice(all_codes)

    while True:
        suffix = f"{random.randint(0, 9999):04d}"
        if suffix not in existing_suffixes:
            existing_suffixes.add(suffix)
            break

    return f"{birthdate}{state_or_country_code}{suffix}"

def hash_function(ic_number, table_size):
    if not ic_number or len(ic_number) != 12:
        raise ValueError(f"IC number must be a 12-character string, got {len(ic_number)}.")
    
    format = [int(ic_number[i:i+4]) for i in range(0, 12, 4)]
    folded = sum(format)
    return folded % table_size

def insert_into_hash_table(hash_table, ic_number, table_size):
    index = hash_function(ic_number, table_size)
    if ic_number not in hash_table[index]:
        hash_table[index].append(ic_number)

def simulate_insertions(table_size):
    hash_table = defaultdict(list)
    existing_suffixes = set()
    ic_numbers = [generate_ic_number(existing_suffixes) for _ in range(1000)]
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
        print(f"  Total Collisions: {total_collisions :.2f}")
        print(f"  Average Collisions over 10 rounds: {total_collisions / 10:.2f}\n")

if __name__ == "__main__":
    run_simulations()
