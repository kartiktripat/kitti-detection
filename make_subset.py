import random
import zipfile
from pathlib import Path

DATA = Path("data")
ZIP_PATH = DATA / "data_object_image_2.zip"
STEP = 4
SEED = 42
TRAIN_FRACTION = 0.8

ids = [f"{i:06d}" for i in range(0, 7481, STEP)]

with zipfile.ZipFile(ZIP_PATH) as z:
    for image_id in ids:
        z.extract(f"training/image_2/{image_id}.png", DATA)

random.seed(SEED)
random.shuffle(ids)
cut = int(len(ids) * TRAIN_FRACTION)
train_ids = sorted(ids[:cut])
val_ids = sorted(ids[cut:])

splits = DATA / "splits"
splits.mkdir(exist_ok=True)
(splits / "train.txt").write_text("\n".join(train_ids) + "\n")
(splits / "val.txt").write_text("\n".join(val_ids) + "\n")

print(f"{len(train_ids)} train, {len(val_ids)} val")
