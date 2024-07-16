# Zootopia Animal Program

Welcome to the Zootopia Animal Program! This program allows you to 
fetch and display information about various animals from an API and generate an HTML file with the animal details.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)

## Installation

1. **Clone the repository:**

    ```bash
    git clone git@github.com:lennartzut/My-Zootopia.git
    ```

2. **Install the required packages:**

    Make sure you have [Python](https://www.python.org/downloads/) installed, then run:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set your API key:**

    Get your API key from [API Ninjas](https://api-ninjas.com/) and set it in the `API_KEY` variable in your code:

    ```python
    API_KEY = "YOUR_API_KEY"
    ```

## Usage

1. **Run the program:**

    ```bash
    python3 animals_web_generator.py
    ```

2. **Follow the prompts:**

    - Enter the name of an animal to fetch information.
    - If data is found, the program will generate an `animals.html` file with the details.
    - If no data is found, a message will be displayed, and you can try another animal name.

## Features

- **Fetch animal data:** Retrieves animal data from an external API.
- **Generate HTML:** Creates an HTML file with the fetched animal data.
- **User-friendly:** Provides a simple command-line interface for user interaction.

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request with your improvements.

