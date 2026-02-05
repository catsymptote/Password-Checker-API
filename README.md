# Password Checker API
Use to check if your passwords are bad/leaked/exists in available password lists.

1. Install or venv the `requirements.txt`. E.g., by running `pip install -r requirements.txt`
2. Place the password lists in `./passwords/` (1 line == 1 password, no csv and amounts of anything)
3. Launch `main.py`. E.g., by running `python main.py`

- The program will first load the password files. This may take a few seconds, if the password files are huge. (100's of MB will take seconds.)
- Once this is done, the API will be available. Run `GET` at `/` to get a short guide. Run `GET` at `/{password}` to check password. This will return `{pwned: <bool>}` (i.e., `true` og `false`).
