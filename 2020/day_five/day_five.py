from typing import List, Dict, Callable

ROWS:int = 128
COLUMNS:int = 8

with open('input', 'r') as f:
    entries = [e.strip() for e in f.readlines()]

def lower_half(kargs:Dict, key:str):
    kargs.update({key:[kargs[key][0], (kargs[key][1] + kargs[key][0]) // 2]}),
def upper_half(kargs:Dict, key:str):
    kargs.update({key:[(kargs[key][1] + kargs[key][0]) // 2 + 1, kargs[key][1]]})

callable_matrix: Dict = {
        'F': lambda kargs: lower_half(kargs, 'ubound'),
        'B': lambda kargs: upper_half(kargs, 'ubound'),
        'L': lambda kargs: lower_half(kargs, 'lbound'),
        'R': lambda kargs: upper_half(kargs, 'lbound')
}

def seat_id(ticket) -> int:
    ticket_parameters: Dict = {
        'ubound': [0, ROWS - 1],
        'lbound': [0, COLUMNS - 1]
    }
    [callable_matrix[c](ticket_parameters) for c in ticket]
    return ticket_parameters['ubound'][0] * 8 + ticket_parameters['lbound'][0]

seat_ids: List = sorted([seat_id(ticket) for ticket in entries])

# First star
print(max(seat_ids))

# Second star
seat_ids = set(seat_ids)
ans = list(set(range(min(seat_ids), max(seat_ids)+1)) - seat_ids)[0]
print(ans)
