# Abstract Recommender System

This project implements an abstract recommender system designed to interpret natural language search queries and return relevant recommendations. For example, if you ask _“A lightweight laptop with powerful graphics for Android Studio development under 500,”_ it will understand the key requirements and deliver tailored laptop suggestions that actually fit the bill.

Built with modularity in mind, the system uses NLP embeddings and a FastAPI backend, allowing easy integration with any dataset by simply updating the configuration.

## Project Structure

```
.
├── .gitignore                 # Specifies intentionally untracked files that Git should ignore
├── assets/
│   └── laptops.csv            # Dataset containing laptop information
├── config.yaml                # Configuration file for the application
├── data/
│   └── loader.py              # Module for data loading and preprocessing
├── main.py                    # Entry point for the FastAPI application
├── myconfig.yaml              # User-specific configuration file (example)
├── README.md                  # This file
├── recommender/
│   ├── __init__.py            # Initializes the recommender module
│   └── base.py                # Core functionality for the recommender system
├── requirements.txt           # Lists project dependencies
└── utils/
    └── helpers.py             # Utility functions
```

## Setup Instructions

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    ```

    *   On Windows:

        ```bash
        venv\Scripts\activate
        ```

    *   On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

The application uses a `config.yaml` file for settings. You can create a `myconfig.yaml` to override default settings if needed. The data path for the dataset is configured in `config.yaml`:

```yaml
# filepath: config.yaml
data_path: ./assets/{dataset_name}
key_fields:
  - Manufacturer
  - Model Name
  - Category
  - Screen Size_str
  - Screen
  - CPU
  - RAM
  - Storage
  - GPU
  - Operating System
  - Operating System Version
  - Weight_str
  - Price (Euros)_str

numeric_fields:
  - Price (Euros)
  - Screen Size
  - Weight

output_field: description
id_field: Model Name
```

Make sure your dataset (e.g., `laptops.csv`) is placed inside the `assets` directory.

## Usage

Run the FastAPI application with:

```bash
uvicorn main:app --reload
```

Then visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser. The root endpoint is defined in `main.py`:

```python
@app.get("/")
def read_root():
    return {"message": "Welcome to the Abstract Recommender System API"}
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
