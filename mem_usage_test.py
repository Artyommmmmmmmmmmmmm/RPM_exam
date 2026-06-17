import main
import tracemalloc
import gc

def mem_usage_test():
    sizes = [10, 100, 1000, 10000]
    base_str = "Red ram is"

    print("Тестирование потребления памяти:\n")

    for i in sizes:
        gc.collect()

        test_str = base_str * i

        tracemalloc.start()

        main.main(test_str)

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(
            f"размер текста: {len(test_str)} символов | "
            f"пиковое потребление: {peak / 1024:.2f} KB"
        )

        gc.collect()


if __name__ == "__main__":
    mem_usage_test()