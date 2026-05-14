from main import main
import psutil
import os
import gc

def mem_usage():
    sizes = [10, 100, 1000, 10000]
    base_str = "Red ram is"
    process = psutil.Process(os.getpid())
    for i in sizes:
        gc.collect()
        test_str = base_str * i
        mem_before = process.memory_info().rss / 1024 / 1024
        main(test_str)
        mem_after =  process.memory_info().rss / 1024 / 1024
        print(f"загрузка:{str(i) + "0"} символов | использование памяти:{round(mem_after - mem_before, 2)} MB")
        gc.collect()

if __name__ == "__main__":   
    mem_usage()