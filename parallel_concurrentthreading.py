import threading

table = threading.Lock()
table_time = 11
table_used = threading.Condition(lock=table)


def table_use(person_id):
    global table_time
    while table_time > 0:
        with table:  #It's lock the thread and open the lock for other thread
            while (person_id != (table_time % 2)) and (table_time > 0):
                print(
                    f"Person {person_id},checked if other is using table and stand there"
                )
                table_used.wait()
            if (table_time > 0):
                table_time -= 1
                print(
                        f"Person {person_id} used table, {table_time} left for other person"
                )
                
                table_used.notify()


if __name__ == "__main__":
    for person in range(2):
        threading.Thread(target=table_use, args=(person,)).start()
