import time
for i in range(10):
    time.sleep(2)
from tqdm import tqdm
for i in tqdm(range(10)):
    time.sleep(2)
    