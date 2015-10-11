_, _, state, accepting_state, tape, rules = open("input.txt").read().splitlines()
tape, head = dict(enumerate(tape)), 0

rules_dict = {(s1, v1): (s2, v2, dir) for s1, v1, _, s2, v2, dir in map(str.split, rules)}

while state != accepting_state:
    state, tape[head], dir = rules_dict[(state, tape.get(head, "_"))]
    head += (1 if dir == ">" else -1)

locations = {head: "^", 0: "|"}
indicators = "".join(locations.get(i, " ") for i in sorted(tape))
tape = "".join(tape[i] for i in sorted(tape)).rstrip("_")

while tape[0] == "_" and indicators[0] == " ":
    tape, indicators = tape[1:], indicators[1:]

print(tape)
print(indicators)