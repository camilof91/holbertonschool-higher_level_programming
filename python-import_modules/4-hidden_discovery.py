#!/usr/bin/python3
if __name__ == "__main__":
    import dis
    with open("hidden_4.pyc", "rb") as file:
        code = file.read()
        instructions = dis.get_instructions(code)
        names = {instr.argval for instr in instructions if instr.opname == "LOAD_CONST"}
        for name in sorted(names):
            if not name.startswith("__"):
                print(name)
