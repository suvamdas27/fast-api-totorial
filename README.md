#### 1. Create and Activate a Virtual Environment

- Step 1: Create a new directory and open it in VSCode:
```bash 
    mkdir fastAPI
```
- Step 1: Create the virtual environment 
```bash
    python -m venv .my-venv
```
- Step 2: Activate the virtual environment
    - In VSCode
        ```bash
            source .my-venv/Scripts/activate
        ```
    - In Windows Terminal/CMD
        ```bash
            .my-venv/Scripts/activate.bat
        ```
- Step 3: Select python interpretor from the newly created virtual environment in VS Code

```Ctrl+Shift+P -> Python: Select Interpretor -> Select newly created python interpretor```

- Step 4: Check which python interpretor
```bash
    which python
```
- Step 5: Update pip
```bash
    python.exe -m pip install --upgrade pip
```
- Step 6: Install Make (to handle Makefile) with admin cmd
```bash
    choco install make
```
- Step 7: Install mkcert (to create https) with admin cmd
```bash
    choco install mkcert
```

- Step 8: Deactivate virtual environment
    - In VSCode
    ```bash
        deactivate
    ```
    - In Windows Terminal/CMD
    ```bash
        deactivate
    ```
    or
    ```bash
        .my-venv/Scripts/deactivate.bat
    ```

#### 2. Install Requirements with below code after activating the virtual environment

```bash
    pip install -r requirements.txt
```
or 

```bash
    make install
```

#### 3. Create https certificate

- Open cmd with admin and go to the project directory then run
```bash
    mkcert -install && mkcert localhost 127.0.0.1 ::1
```

#### 4. Run FastApi (app) Server in virtual environment

- Wthout HTTPS

```bash
    uvicorn main:app --reload
```

- With HTTPS

```bash
    uvicorn main:app --ssl-keyfile localhost+2-key.pem --ssl-certfile localhost+2.pem --reload
```

#### 5. Set Custom Environment Variable in Virtual Environment

- Open "active" script in ".my-venv" virtual environment from below path

```path
    .my-venv/Scripts/activate
```

- Add below line at the end to export uvicorn app starting command

```bash
    export DEBUG_APP="uvicorn main:app --ssl-keyfile localhost+2-key.pem --ssl-certfile localhost+2.pem --reload"
```
or

```bash
    export DEBUG_APP="uvicorn main:app --reload"
```

- Add below line at the end of deactivate function

```bash
    unset DEBUG_APP
```

- Open "active.bat" script in ".my-venv" virtual environment from below path

```path
    .my-venv/Scripts/activate.bat
```

- Add below line at the end to export uvicorn app starting command

```bash
    set DEBUG_APP=uvicorn main:app --ssl-keyfile localhost+2-key.pem --ssl-certfile localhost+2.pem --reload
```
or

```bash
    set DEBUG_APP=uvicorn main:app --reload
```

- Open "deactive.bat" script in ".my-venv" virtual environment from below path

```path
    .my-venv/Scripts/deactivate.bat
```

- Add below line at the end

```bash
    set "DEBUG_APP="
```

- Save the file, close it & restart the virtual environment

- Run below command to check the environment

    - In VSCOde
    ```bash
        echo $DEBUG_APP
    ```
    - In Windows Terminal/CMD
    ```bash
        echo %DEBUG_APP%
    ```

- Now simply use the environment variable to start the FastAPI app server

    - In VSCOde
    ```bash
        $DEBUG_APP
    ```
    - In Windows Terminal/CMD
    ```bash
        %DEBUG_APP%
    ```


#### 6. Open APP in Browser

- Step 1: Open FastApi Swagger UI (With HTTPS)
```link
https://127.0.0.1:8000/docs
```

- Step 2: Open FastApi built-in documentaion of your app (With HTTPS)
```link
https://127.0.0.1:8000/redoc
```

`Note: Use https if server started with certificate and key else use http only`

#### 7. HTTP Request Methods and Status Codes Documentation

- Request Methods

```link
https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods
```

- Status Codes

```link
https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status
```