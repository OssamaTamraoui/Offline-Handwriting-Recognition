# HTR-app

### 1. install torch

We must install torch separately as putting in the requirements.txt works for cuda version

``` 
$ pip install torch==1.7.0+cpu torchvision==0.8.1+cpu torchaudio===0.7.0 -f https://download.pytorch.org/whl/torch_stable.html
```

### 2. install the requirements.txt

``` 
pip install -r reequiremnts.txt
```

### 3. run the streamlit app

```
streamlit run app.py
```