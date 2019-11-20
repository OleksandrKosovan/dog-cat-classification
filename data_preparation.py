import os

from tqdm import tqdm

NEW_DATA_PATH = 'data/'

if not os.path.exists(NEW_DATA_PATH):
    os.makedirs(NEW_DATA_PATH)

if not os.path.exists(os.path.join(NEW_DATA_PATH, 'dog')):
    os.makedirs(os.path.join(NEW_DATA_PATH, 'dog'))

if not os.path.exists(os.path.join(NEW_DATA_PATH, 'cat')):
    os.makedirs(os.path.join(NEW_DATA_PATH, 'cat'))

DATA_PATH = 'data/train/'

for file in tqdm(os.listdir(DATA_PATH)):
    new_file = file.replace('.jpg', '')
    new_file = new_file.replace('.', '/')
    new_file = new_file + '.jpg'
    os.rename(os.path.join(DATA_PATH, file), os.path.join(NEW_DATA_PATH, new_file))

os.rmdir(DATA_PATH)
