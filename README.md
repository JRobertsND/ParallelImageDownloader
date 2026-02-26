# ParallelImageDownloader

**Project title:** ParallelImageDownloader
**Description of the problem:** We were tasked by our manager to build a robust image downloading system. It must generate 100 random images using the provided URL and demonstrate time execution differences between serial and parallel downloading. 
**Setup instructions:** To run the program, simply access the downloader.py file. Under the "if __name__ == '__main__':" script, choose if you want to demonstrate serial or parallel processing, or both. 
**How to run the program:** Run the program using the "python3 downloader.py" command. 
Serial vs parallel explanation: The serial execution calls teh download function one-at-a-time. Therefore, each of the 100 images is downloaded sequentially. The parallel execution process uses a maximum of 5 workers to simultaneously download images. It calls he download function in parallel, making the speed much faster. 
**Performance results:** The parallel processing function was consistently much quicker than the serial processing function. The parallel processing function took ~5 seconds to execute. Teh serial processing function took ~12 seconds. 
**Design decisions:** I used the provided code but split it into two functions, download and log. This simplified my function calls. To develop my parallel execution function, I recycled class code. I also used a sempahore to limit the number of workers to 5. 
