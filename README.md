# Django-Medication-Tracker-API
A back-end API built with django rest framework that allows users to track and manage their medications.
Users can enter certain data related to their medications such as name, dosage, times taken per day,
and other useful information.

# Install and Setup

1. Clone the repository

```shell
git clone https://github.com/ManuelDelarosa1204/Django-Medication-Tracker-API.git
```

2. Create a virtual environment

```shell
python3 -m venv venv
```

3. Activate the virtual environment

    Windows

    ```shell
    venv/Scripts/activate
    ```

    Unix

    ```shell
    source venv/bin/activate
    ```

4. Install the required packages

```shell
pip install -r requirements.txt
```

5. Apply database migrations

```shell
python3 manage.py migrate
```

6. Create a superuser (admin) (Fill out information as prompted)

```shell
python3 manage.py createsuperuser
```

7. Run the development server

```shell
python3 manage.py runserver
```

8. Access the admin panel in your browser by navigating to `localhost:8000/admin` and logging in with superuser credentials.

9. Obtain a User Token: In the admin panel, navigate to Tokens. Copy the token associated with a user to make authorized API calls.

# API Endpoints

**GET** *`users/`* : List all users of the application

**POST** *`users/`* : Create a user

**GET** *`users/{user slug}/`* : Retrieve user data

**POST** *`medications/create/`* : Create medications (requires token)

**GET** *`medications/{user slug}/` : List all medications for a specific user (requires token)

**DELETE** *`medications/{user slug}/{medication id}/delete/` : Delete a medication for a user

