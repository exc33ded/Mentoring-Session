## Creating a Virtual Environment 


```bash
python -m venv base
```

Activating the Virtual Environment
```bash
.\venv\Scripts\Activate.ps1
```



## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the modules.

```bash
pip install -r .\requirements.txt
```

## Usage 

### For FastAPI without html template:
```python
uvicorn main:app --reload
```

Go To 
```python
http://127.0.0.1:8000/
```
Or
```python
http://127.0.0.1:8000/docs
```

### For FastAPI with html template:
```python
uvicorn app:app --reload
```

Go To 
```python
http://127.0.0.1:8000/
```


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Note

<b>Everything is to done on the terminal itself, and make sure you have python installed.</b>
## License

[MIT](https://choosealicense.com/licenses/mit/)