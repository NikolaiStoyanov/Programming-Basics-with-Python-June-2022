current_record = float(input())
metres = float(input())
time_per_meter = float(input())

slow = metres // 50
slow_time = slow * 30

his_time = metres * time_per_meter

total_time = slow_time + his_time

if total_time < current_record:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
else:
    needed_time = total_time - current_record
    print(f"No! He was {needed_time:.2f} seconds slower.")