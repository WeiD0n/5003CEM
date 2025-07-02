import random
import time

#Function to generate 100 random numbers between 0 and 10000
def generate_random_numbers():
    return [random.randint(0, 10000) for _ in range(100)]

def main():
    rounds = 10
    total_time_ns = 0

    print("-" * 50)
    print("Sequential Random Number Generation (No Threads)")
    print("-" * 50)

    #Loop for the specified number of rounds
    for round_num in range(1, rounds + 1):
        results = []

        start_time = time.perf_counter_ns()

        #Generate 3 sets of random numbers sequentially
        for _ in range(3):
            results.append(generate_random_numbers())

        end_time = time.perf_counter_ns()
        T = end_time - start_time
        total_time_ns += T

        print(f"Round {round_num:>2}: Time Taken (T) = {T} ns")

    avg_time = total_time_ns / rounds
    print("\n" + "-" * 50)
    print(f"Total Time over {rounds} rounds : {total_time_ns} ns")
    print(f"Average Time per round: {avg_time:.2f} ns")
    print("-" * 50)

if __name__ == "__main__":
    main()
