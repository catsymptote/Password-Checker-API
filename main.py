import time

from fastapi import FastAPI
import uvicorn

import pw_loader


app = FastAPI()


# Load password list
start_time = time.time()
PASSWORDS = pw_loader.load_passwords()
delta_time = time.time() - start_time
print(f'Passwords loaded for {delta_time:.0f} s.')


@app.get('/')
def check_password():
    return {'Guide': '''Send `GET to /{password}` and you will recieve `{'pwned': true}` (or false).'''}


@app.get('/{password}')
def check_password(password: str):
    return {'pwned': password in PASSWORDS}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
