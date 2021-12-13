import utils as u

diagram, instructions  = u.import_instructions("./data/input")

for instruction in instructions:
    diagram = u.apply_instruction(instruction, diagram)

u.print_diagram(diagram)
