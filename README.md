# dev-search

[![Build Status](https://travis-ci.org/your-username/your-repo.svg?branch=master)](https://travis-ci.org/your-username/your-repo)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Python web app to search developers

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. Create a virtual environment and install dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Apply migrations:

    ```bash
    python manage.py migrate
    ```
   4. Run server
       ```bash
      python manage.py runserver
       ```

## Usage
- Access the app at  http://127.0.0.1:8000/.
- Sign up and log in http://127.0.0.1:8000/admin/ to access the admin panel for CRUD operations on restaurants.
- Creating an account is required to make changes (CRUD) .

##  Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these guidelines:

- Fork the repository
- Create your branch: git checkout -b feature/your-feature
- Make your changes and commit them: git commit -m 'Add some feature'
- Push to the branch: git push origin feature/your-feature
- Create a pull request

## Walkthrough video

