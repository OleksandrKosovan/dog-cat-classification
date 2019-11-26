# Dog-Cat classification

![img](https://miro.medium.com/max/3840/1*oB3S5yHHhvougJkPXuc8og.gif)

[The Dogs vs. Cats dataset](https://www.kaggle.com/c/dogs-vs-cats-redux-kernels-edition/data) is a standard computer vision dataset that involves classifying photos as either containing a dog or cat.

Although the problem sounds simple, it was only effectively addressed in the last few years using deep learning convolutional neural networks.


# Content

- [Results]()
- [Get started]()


# Results

| Approach  | Accuracy |
| ------------- | ------------- |
| Baseline model  |  84,54% |


# Get started

Create folder for data.

```bash
mkdir data
```

Download data from [Kaggle](https://www.kaggle.com/c/dogs-vs-cats-redux-kernels-edition/data) 
to this folder. After that select train folder and push it into "data".

It will be like that:
```bash
└── data
    └── train
```

Create and activate environment.

```bash
virtualenv -p python3 venv
source venv/bin/activate
```

Data preparation:

```bash
python3 data_preparation.py
```

After that data folder need to be like it:

```bash
├── data
│   ├── cat
│   └── dog
```

Splitting data:


```bash
python3 split_data.py
```


