from collections import defaultdict
from io import StringIO
import utils as u

fh = StringIO("""\
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
""")

alg, img = u.import_data("./data/input")

outside_values = [u.DARK_PIXEL_VALUE, u.LIGHT_PIXEL_VALUE]
for i in range(50):
    outval_idx = i % len(outside_values)
    outval = outside_values[outval_idx]
    
    img = u.enhance(img, alg, outside=outval)

n_light_pixels = sum([v for v in img.values()])

print(f"N. Light Pixels {n_light_pixels}")

