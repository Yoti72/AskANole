# AskANole
“Where Noles Help Noles. Trade, Task, and Triumph Together.”

# Flask Web App with Python, HTML, CSS, and Flash

## Project Overview

This is a simple Flask-based web application that allows users to sign up, log in, post messages, and interact with other users. The application uses HTML templates for the front end, CSS for styling, and Flask, a Python web framework, for the back end. The main features include user authentication, posting messages, viewing posts, sending and receiving messages, and searching for posts.

## Prerequisites

- Python 3.12
- Flask
- SQLite3

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   ```   

2. Change to the project directory:

   ```bash
   cd your-repo
   ```
4. Start a virtual environment:

   ```bash
   python -m venv <name_of_virtual_environment>.
   ```
   
5. Activate the vevn:

   ```bash
   .\.venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install Flask
   ```

## Setup

1. Run the `Setup.py` script to initialize the database:

   ```bash
   python -u "DRIVE:\path\Setup.py"
   ```

3. Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to access the application.

## Usage

1. **Sign Up:** Click on the "Sign Up" link to create a new account.

2. **Log In:** Enter your credentials on the login page.

3. **Post Messages:** Once logged in, you can post messages by clicking on the "Add Post" link.

4. **View Messages:** Visit the "Main" page to view posts from all users.

5. **Send Messages:** Use the "Messages" page to send and receive messages with other users.

6. **Search Posts:** You can search for posts using the "Search" feature.

## File Structure

- `main.py`: The main Python file containing the Flask application.
- `Setup.py`: Script to set up the database.
- `check.py`: Module for checking authentication tokens.
- `static/`: Directory containing CSS files for styling.
- `templates/`: Directory containing HTML templates for the web pages.

## Contributing

If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Special thanks to the Flask and Python communities for their excellent documentation and support.

Feel free to customize this README file according to your project's specific details and requirements.
