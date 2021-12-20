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

alg, img = u._read_from_stream(fh)
alg, img = u.import_data("./data/input")


img = u.enhance(img, alg, outside=u.DARK_PIXEL_VALUE)
img = u.enhance(img, alg, outside=u.LIGHT_PIXEL_VALUE)

n_light_pixels = sum([v for v in img.values()])

print(f"N. Light Pixels {n_light_pixels}")

