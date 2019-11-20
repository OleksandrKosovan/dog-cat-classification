# Work in progress....

# Dog-Cat classification


# 1. Get started

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


