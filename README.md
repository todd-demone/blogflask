# My Flask Blog

1. Install python3.10
```
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.10
python3.10 --version
```

2. Create and activate a venv virtual environment (using python 3.10)
```
cd ~
mkdir blogflask
cd blogflask
python3.10 -m venv venv
source venv/bin/activate
```

3. Clone the repo
```
git clone git@github.com:todd-demone/blogflask.git
```

4. Install the dependencies
```
pip install -r requirements.txt
```

5. Copy sample.env to .env and make necessary changes (need an app password if using google for email)
```
cp sample.env .env
```

6. Run the app
```
python app.py
```

## Notes:
To install a library, e.g.:
```
pip install markdown
```
To add all installed libraries to a requirements.txt file:
```
pip freeze > requirements.txt
```