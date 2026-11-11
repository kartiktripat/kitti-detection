from dataclasses import dataclass


@dataclass
class KittiObject:
    label: str
    truncated: float
    occluded: int
    box: tuple


def parse_label_line(line):
    parts = line.strip().split()
    return KittiObject(
        label=parts[0],
        truncated=float(parts[1]),
        occluded=int(parts[2]),
        box=(float(parts[4]), float(parts[5]), float(parts[6]), float(parts[7])),
    )


def read_label_file(path):
    objects = []
    with open(path) as f:
        for line in f:
            if line.strip():
                objects.append(parse_label_line(line))
    return objects


if __name__ == "__main__":
    sample = "Pedestrian 0.00 0 -0.20 712.40 143.00 810.73 307.92 1.89 0.48 1.20 1.84 1.47 8.41 0.01"
    print(parse_label_line(sample))