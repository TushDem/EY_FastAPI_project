from multiprocessing import Pool

def add_list(numbers):
    return sum(numbers)

def perform_addition(payload):
    with Pool(processes=4) as pool:
        results = pool.map(add_list,payload)
    return results