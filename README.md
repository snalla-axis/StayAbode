# Setup Env

1. Upgrade pip

    ```bash
    python -m pip install --upgrade pip
    ```

2. Install python3 latest version | stable
    ``` 
   Reference for step by step installation
    https://vitux.com/install-python3-on-ubuntu-and-set-
   up-a-virtual-programming-environment/
   
   ``` 
   
3. Setup virtualenv

    ```bash
    pip install virtualenv virtualenvwrapper
    source virtualenvwrapper.sh --python=<python path>
    mkvirtualenv <env_name>
    ```
 4. Download golden-eye repository

    ```bash
    cd $HOME
    git@github.com:snalla-axis/StayAbode.git
    ```

5. Install project dependencies

    ```bash
    cd $HOME/StayAbode/
    pip install -r requirements.txt
   ```
 6. Start server 
    ``` bash
    cd $HOME/StayAbode/todoapp
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```
 6. Create super user can use admin ui
    ``` bash
    cd $HOME/StayAbode/todoapp
    python manage.py createsuperuser
    ```


# Features
1. Sample model given

2. CRUD operations

3. Admin Interface and action to download to csv

4. API's for All records or one record
    ``` bash
    single record: http://localhost:8000/todolist/listallorone/?id=10
    records: http://localhost:8000/todolist/listallorone
   ```