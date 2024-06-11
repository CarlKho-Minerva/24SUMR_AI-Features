# Video Recommender

A personalized video recommendation algorithm utilizing user actions and interests, built with Python and ChromaDB for semantic search.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Overview

This project demonstrates a personalized video recommendation system that adjusts recommendations based on user interactions such as likes, shares, views, and loops. The project utilizes ChromaDB for embedding-based semantic search and OpenAI for generating embeddings.

## Features

- User interest management with dynamic weighting
- Action-based interest adjustment
- Embedding-based video search using ChromaDB
- Supports user interruptions and recommends relevant interests

## Project Structure

```markdown
video_recommender/
├── __init__.py
├── chromadb_helper.py
├── constants.py
├── main.py
├── recommender.py
├── user_actions.py
├── utils.py
└── demo.py
```

- `chromadb_helper.py`: Functions for initializing and interacting with ChromaDB.
- `constants.py`: Project-wide constants.
- `main.py`: Entry point for running the recommender system.
- `recommender.py`: Core recommendation logic.
- `user_actions.py`: Functions related to user actions and interest adjustments.
- `utils.py`: Utility functions, including debugging and printing.
- `demo.py`: Script to demonstrate the functionality of the recommender system.

## Setup

### Prerequisites

- Python 3.11
- Pandas
- ChromaDB
- OpenAI API Key

### Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/yourusername/video_recommender.git
    cd video_recommender
    ```

2. **Create a virtual environment and activate it**:

    ```sh
    python3.11 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up your OpenAI API key**:
    - Replace the placeholder `OPENAI_API_KEY` in your environment or directly in the code.

## Usage

1. **Run the main script**:

    ```sh
    python main.py
    ```

2. **Simulation**:
    - The main script runs a simulation that demonstrates the video recommendation process based on predefined user interests and actions.

## Configuration

- **Modify user interests**:
  - Edit the `user_interests` list in `main.py` to include your interests.

- **Adjust constants**:
  - Modify constants in `constants.py` to fine-tune the recommendation algorithm.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions, please contact [Carl Kho](mailto:kho@uni.minerva.edu).
