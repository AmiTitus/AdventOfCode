from typing import List

with open('input', 'r') as f:
    entries = [e.strip() for e in f.readlines()]

def get_row(code:str) -> int:
    return int(code[0:7].replace('B', '1').replace('F', '0'), 2)

def get_col(code:str) -> int:
    return int(code[7::].replace('L', '0').replace('R', '1'), 2)

def get_seat_id(code: str) -> int:
    return get_row(code) * 8 + get_col(code)

seat_ids: List = sorted([get_seat_id(code) for code in entries])
print(f"First star: {max(seat_ids)}")
last_id: int = 0
for seat_id in seat_ids:
    if seat_id - last_id == 2:
        print(f"Second star {seat_id - 1}")
        break
    else:
        last_id = seat_id
