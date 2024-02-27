# Django Movies Web App

This is a Django web application for managing movies, genres, and actors.

## Overview

This project provides the following features:

- Displaying a list of movies with filtering options
- Adding, updating, and deleting movies
- Viewing detailed information about each movie
- Managing genres and actors with similar CRUD operations

## Demo

A live demo of this project is available at [Demo Django Movies](https://cinema-service-test-task.onrender.com/).

## Installation Instructions

1. Create and activate a Python virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate  # for Linux/Mac
    .\env\Scripts\activate   # for Windows
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the migrations:

    ```bash
    python manage.py migrate
    ```

4. Create a `.env` file based on the `.env.sample` file provided and enter the DJANGO_SECRET_KEY and OMDB_API_KEY tokens.

## Usage

1. Start the Django server:

    ```bash
    python manage.py runserver
    ```
2. Open the Django admin panel in your browser at `http://localhost:8000/`

## Author

Petrykiv Dmytro / petrykiv.dmytro19@gmail.com

<p align="center">
<img style="width: 100%;" src="https://i.postimg.cc/nzykWKNd/result.gif">
</p>