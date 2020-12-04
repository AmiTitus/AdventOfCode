import re
from typing import List, Dict, Callable

pattern = re.compile(r'(\w{3}):([#\d\w]+)')

passports: List[Dict[str, str]] = list()

with open('./input', 'r') as f:
    tmp_passport: Dict = dict()
    for line in f.readlines():
        line = line.rstrip()        
        if line:
            tmp_passport.update(dict(pattern.findall(line)))
        else:
            passports.append(tmp_passport)
            tmp_passport = dict()

passports.append(tmp_passport)


star1_valid_keys_list: List[str] = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr','hgt'] #NOTE Optional + ['cid']

print(sum(1 for p in passports if all([k in list(p.keys()) for k in star1_valid_keys_list])))

check_validity: Dict[str, Callable] = {
    'byr': lambda value: 2002 >= int(value) >= 1920,
    'iyr': lambda value: 2020 >= int(value) >= 2010,
    'eyr': lambda value: 2030 >= int(value) >= 2020,
    'hgt': lambda value: (value.endswith('cm') and (193 >= int(value[:-2]) >= 150) or (value.endswith('in') and 76 >= int(value[:-2]) >= 59)),
    'hcl': lambda value: value[0] == '#' and re.match(r'^(\d|[a-f]){6}$', value[1:]),
    'ecl': lambda value: str(value) in ['amb', 'blu', 'gry', 'brn', 'grn','hzl', 'oth'],
    'pid': lambda value: value.isdigit() and len(value) == 9,
    'cid': lambda value: True
}

print(sum(1 for p in passports if all([k in list(p.keys()) and check_validity[k](p[k]) for k in star1_valid_keys_list])))
