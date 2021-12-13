import utils as u

diagram, instructions  = u.import_instructions("./data/input")

first_instruction = instructions[0]

result = u.apply_instruction(first_instruction, diagram)

n_dots = result.sum()

print(f"Number of dots after the first instruction: {n_dots}")
