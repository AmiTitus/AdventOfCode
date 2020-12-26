with open('input') as f:
    entries = f.read()
prog = entries.splitlines()

def execute(fix: int = None):
    acc, index = 0, 0
    passed_instruction = set()
    infinite_loop: bool = False
    while index < len(prog) and index not in passed_instruction and not infinite_loop:
        cmd, value = prog[index].split()
        passed_instruction.add(index)
        if fix == index:
            cmd = {
                'nop': 'jmp',
                'jmp': 'nop'
            }.get(cmd, cmd)
        if cmd == 'acc':
            acc += int(value)
            index += 1
        elif cmd == 'nop':
            index += 1
        elif cmd == 'jmp':
            index += int(value)

        if index in passed_instruction:
            infinite_loop = True

    return (acc, infinite_loop)

print(execute())
for i in range(len(prog)):
    acc, loop = execute(i)
    if not loop:
        print(acc)
