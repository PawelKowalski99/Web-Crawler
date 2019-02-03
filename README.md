# SiteScrap Web Crawler
This project scraps url's domain and makes map of this site.
## Installing
Firstly you need to make virtual environment
```
python3 -m venv /path/to/new/virtual/environment
```
Then clone git repository to this virtual environment path
```
$ git clone https://github.com/asplia/Web-Crawler.git
```
Let's go inside venv
```
/path/to/new/virtual/environment/venv/scripts/activate.bat
```
You should now install all required files
If you are not in 
```
 /path/to/new/virtual/environment
```
Go there.
Then
```
pip install -r /path/to/requirements.txt
```
Good job! You can now run web crawler by running the command in command line
Remember that you need to be in this directory nad you have to run virtual environment also!
```
web_crawler.py
```

## Tests
To run tests you need to run
```
pytest
```
