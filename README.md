# My Flask Blog

1. Create and activate a venv virtual environment (using python 3.12)
```
cd ~
mkdir blogflask
cd blogflask
python3.12 -m venv venv
source venv/bin/activate
```

2. Clone the repo
```
git clone git@github.com:todd-demone/blogflask.git
```

3. Install the dependencies
```
pip install -r requirements.txt
```

4. Copy sample.env to .env and make necessary changes (need an app password if using google for email)
```
cp sample.env .env
```

5. Run the app
```
python app.py
```

## Notes:
To install a library:
```
pip install markdown
```
To add all installed libraries to a requirements.txt file:
```
pip freeze > requirements.txt
```