## Requirements
* Python 3

## Installation
* In order to run your own build, first ensure you have python3 globally installed in your computer. If not, you can get python [here](https://www.python.org).
* After doing this, confirm that you have installed virtualenv globally as well. If not, run this:
    ```bash
        $ python -m pip install virtualenv
    ```
* Then, Git clone this repo to your PC
    ```bash
        $ git clone https://github.com/lopezz/activity_feed_django.git
    ```

* #### Dependencies
    1. Cd into your the cloned repo as such:
        ```bash
            $ cd activity_feed_django
        ```
    2. Create and activate your virtual enviroment:
        ```bash
            $ python -m venv venv
            $ source venv/bin/activate
        ```
        If you are on Windows, you can achieve this using.
        ```bash            
            $ venv\Scripts\activate
        ```
    3. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt
        ```
    4. Make those migrations work
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
        ```
    5. load the initial data
        ```bash
            $ python manage.py loaddata feed/fixtures/feed_fixture.json
        ```
        If you need to add more Users/FeedItems, you sould create a super user and go 
        to the admin after you run the server (http://localhost:8000/admin).

* #### Run It
    Start the server using this command:
    ```bash
        $ python manage.py runserver
    ```
    You can now access the application in your browser using
    ```
        http://localhost:8000
    ```