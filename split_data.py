import os
import random

DATA_PATH = 'data/'

# Train

if not os.path.exists(os.path.join(DATA_PATH, 'train')):
    os.makedirs(os.path.join(DATA_PATH, 'train'))

if not os.path.exists(os.path.join(DATA_PATH, 'train/dog')):
    os.makedirs(os.path.join(DATA_PATH, 'train/dog'))

if not os.path.exists(os.path.join(DATA_PATH, 'train/cat')):
    os.makedirs(os.path.join(DATA_PATH, 'train/cat'))

# Test

if not os.path.exists(os.path.join(DATA_PATH, 'test')):
    os.makedirs(os.path.join(DATA_PATH, 'test'))

if not os.path.exists(os.path.join(DATA_PATH, 'test/dog')):
    os.makedirs(os.path.join(DATA_PATH, 'test/dog'))

if not os.path.exists(os.path.join(DATA_PATH, 'test/cat')):
    os.makedirs(os.path.join(DATA_PATH, 'test/cat'))

# Validation

if not os.path.exists(os.path.join(DATA_PATH, 'validation')):
    os.makedirs(os.path.join(DATA_PATH, 'validation'))

if not os.path.exists(os.path.join(DATA_PATH, 'validation/dog')):
    os.makedirs(os.path.join(DATA_PATH, 'validation/dog'))

if not os.path.exists(os.path.join(DATA_PATH, 'validation/cat')):
    os.makedirs(os.path.join(DATA_PATH, 'validation/cat'))

print('Folders created...')

list_of_dogs = os.listdir(os.path.join(DATA_PATH, 'dog'))
list_of_cats = os.listdir(os.path.join(DATA_PATH, 'cat'))

# Train - 80%
# Test - 10%
# Validation - 10%

# Train

dog_train_size = int(len(list_of_dogs) * 0.8)
train_dog = random.sample(list_of_dogs, k=dog_train_size)

for dog in train_dog:
    os.rename(os.path.join(DATA_PATH, 'dog', dog), os.path.join(DATA_PATH, 'train/dog', dog))

cat_train_size = int(len(list_of_cats) * 0.8)
train_cat = random.sample(list_of_cats, k=cat_train_size)

for cat in train_cat:
    os.rename(os.path.join(DATA_PATH, 'cat', cat), os.path.join(DATA_PATH, 'train/cat', cat))

print('Train data created...')

# Test

list_of_dogs = os.listdir(os.path.join(DATA_PATH, 'dog'))
list_of_cats = os.listdir(os.path.join(DATA_PATH, 'cat'))

dog_test_size = int(len(list_of_dogs) * 0.5)
test_dog = random.sample(list_of_dogs, k=dog_test_size)

for dog in test_dog:
    os.rename(os.path.join(DATA_PATH, 'dog', dog), os.path.join(DATA_PATH, 'test/dog', dog))

cat_test_size = int(len(list_of_cats) * 0.5)
test_cat = random.sample(list_of_cats, k=cat_test_size)

for cat in test_cat:
    os.rename(os.path.join(DATA_PATH, 'cat', cat), os.path.join(DATA_PATH, 'test/cat', cat))

# Validation

list_of_dogs = os.listdir(os.path.join(DATA_PATH, 'dog'))
list_of_cats = os.listdir(os.path.join(DATA_PATH, 'cat'))

for dog in list_of_dogs:
    os.rename(os.path.join(DATA_PATH, 'dog', dog), os.path.join(DATA_PATH, 'validation/dog', dog))

for cat in list_of_cats:
    os.rename(os.path.join(DATA_PATH, 'cat', cat), os.path.join(DATA_PATH, 'validation/cat', cat))

os.rmdir(os.path.join(DATA_PATH, 'cat'))
os.rmdir(os.path.join(DATA_PATH, 'dog'))
