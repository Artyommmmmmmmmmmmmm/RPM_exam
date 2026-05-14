from main import main
import time

def work_speed():    
    text100 = "Red ram is" * 10
    text1000 = "Red ram is" * 100
    text10000 = "Red ram is" * 1000
    text100000 = "Red ram is" * 10000

    cur_time1 = time.time()
    main(text100)
    new_time1 = time.time()
    print(f"Загрузка:100 символов | время выполнения:{str(round(((new_time1 - cur_time1) * 1000), 2))} mc")

    cur_time2 = time.time()
    main(text1000)
    new_time2 = time.time()
    print(f"Загрузка:1000 символов | время выполнения:{str(round(((new_time2 - cur_time2) * 1000), 2))} mc")

    cur_time3 = time.time()
    main(text10000)
    new_time3 = time.time()
    print(f"Загрузка:10000 символов | время выполнения:{str(round(((new_time3 - cur_time3) * 1000), 2))} mc")

    cur_time4 = time.time()
    main(text100000)
    new_time4 = time.time()
    print(f"Загрузка:100000 символов | время выполнения:{str(round(((new_time4 - cur_time4) * 1000), 2))} mc")
    # print(time())
if __name__ == "__main__":
    work_speed()