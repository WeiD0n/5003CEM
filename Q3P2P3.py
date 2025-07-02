import random
import threading
import time

#Function to generate 100 random numbers between 0 and 10000
def generate_random_numbers():
    return [random.randint(0, 10000) for _ in range(100)]

#Function for thread to generate a set of numbers
def generate_sets(result_list, index):
    result_list[index] = generate_random_numbers()

def main():
    rounds = 10
    total_time_in_ns = 0
    
    print("-" * 50)
    print("Multithreaded Random Number Generation Test")
    print("-" * 50)

    #Loop for the specified number of rounds
    for round_number in range(1, rounds + 1):
        results = [None, None, None]
        threads = []

        start_ns = time.perf_counter_ns()

        #Create and start threads for generating random number sets
        for i in range(3):
            thread = threading.Thread(target=generate_sets, args=(results, i))
            threads.append(thread)
            thread.start()

        #Wait for all threads to complete
        for thread in threads:
            thread.join()

        end_ns = time.perf_counter_ns()
        T = end_ns - start_ns
        total_time_in_ns += T

        print(f"Round {round_number:>2}: Time Taken (T) = {T} ns")

    #Calculate the average time taken over all rounds
    average_time_in_ns = total_time_in_ns / rounds

    print("\n" + "-" * 50)
    print(f"Total Time over {rounds} rounds: {total_time_in_ns} ns")
    print(f"Average Time per round: {average_time_in_ns:.2f} ns")
    print("-" * 50)

if __name__ == "__main__":
    main()
