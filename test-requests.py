import requests
import time

def send_requests(url, num_requests):
    # print start time of the test
    print(f"Sending {num_requests} requests to {url}")
    print("Start Time", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    
    for _ in range(num_requests):
        try:
            response = requests.get(url)
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                print(f"Request {_ + 1} sent successfully")
            else:
                print(f"Request {_ + 1} failed with status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request {_ + 1} failed: {e}")
    print("End Time", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        
            
# Container            
# send_requests("https://cr380-demo-qsqlsyejkq-nn.a.run.app",1000)
# 13:03:26 - 13:08:57

# VM
# send_requests("http://35.203.124.6:3000/",1000)
# 13:10:04 - 13:10:23