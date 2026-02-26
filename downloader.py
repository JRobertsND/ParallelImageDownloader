import urllib.request
import requests, certifi
import threading
import requests
from datetime import datetime
import time

url = "https://picsum.photos/300"

images = 5
image_pool = threading.Semaphore(images)

def log(i, status):
    filename = f"image_{i:03d}.jpg"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("logger.txt", "a") as f:
        f.write(f"{timestamp} | {url} | {filename} | {status}\n")

def download(i):
    with image_pool:
        for _ in range(4):
            try:
                filename = f"image_{i:03d}.jpg"
                # timeout=3 means: wait max 3 seconds
                response = requests.get(url, timeout=3)
                with open(filename, "wb") as f:
                    f.write(response.content)
                print(f"Downloaded: {i}/100")
                log(i, "SUCCESS")
                return

            except requests.exceptions.Timeout:
                log(i, "TIMEOUT")
            except Exception:
                log(i, "FAILED")


def serial():
    start = time.time()
    success = 0
    for i in range(1,101):
        download(i)
    end = time.time()
    print(f"Serial execution time is: {end-start} seconds\n")
    

def parallel():
    start = time.time()
    threads = []

    for i in range(1,101):
        t = threading.Thread(target=download, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    
    end = time.time()
    print(f"Parallel execution time is: {end-start} seconds\n")

if __name__ == "__main__":
    serial()
    parallel()


