# excel-to-imbricated-json
Transform an excel file into an imbricated json file matching references with parent references

## INSTALLATION

### Python
Download and install python3.9 from https://www.python.org/downloads/.

### Pipenv
After python installation, run in your terminal:
```sh
pip install pipenv
```

Then in root folder of the project:

#### Create a virtual environment using python3
```sh
pipenv --three 
```

#### Connect to your new virtual environment
```sh
pipenv shell
```

#### Install requirements into a Pipfile and Pipfile.lock
```sh
pipenv install -r requirements.txt
pipenv lock
```

#### Install requirements from Pipfile to your virtual environment
```sh
pipenv install
```

#### Exit the virtual environment
```
exit
```
## Run
```sh
python3 excel_to_imbricated_json.py -i <input: excel file path> -o <output: json file path>
```
