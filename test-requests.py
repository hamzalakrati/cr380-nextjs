import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def send_request(url, request_num):
    try:
        start = time.time()
        response = requests.get(url, timeout=10)  # Added a timeout for the request
        duration = time.time() - start
        if response.status_code == 200:
            # Uncomment the line below to print successful requests
            # print(f"Request {request_num} successful in {duration:.4f} seconds.")
            return duration
        else:
            print(f"Request {request_num} failed (Status Code: {response.status_code}) in {duration:.4f} seconds.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request {request_num} failed: {e}")
        return None

def send_requests(url, num_requests):#
    print(f"Sending {num_requests} requests to {url}")
    start_time = time.time()
    print("Start Time:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    durations = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(send_request, url, i) for i in range(num_requests)]
        for future in as_completed(futures):
            result = future.result()
            if result is not None:
                durations.append(result)

    end_time = time.time()
    total_time = end_time - start_time
    print("End Time:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print(f"Total Time: {total_time:.4f} seconds")
    
    if durations:
        average_time = sum(durations) / len(durations)
        print(f"Average Response Time: {average_time:.4f} seconds")
        print(f"Min Response Time: {min(durations):.4f} seconds")
        print(f"Max Response Time: {max(durations):.4f} seconds")
    else:
        print("No successful requests to calculate performance metrics.")

# Replace with your container and VM URLs
NUMBER_OF_REQUESTS = 1000
CONTAINER_URL = "http://35.203.124.6:8080/"
VM_URL = "http://34.47.33.122:3000/"

# Uncomment the line for the test you want to run
# send_requests(CONTAINER_URL, NUMBER_OF_REQUESTS)

send_requests(VM_URL, NUMBER_OF_REQUESTS)
