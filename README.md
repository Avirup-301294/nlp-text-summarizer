# NLP Text Summarizer

An end-to-end machine learning project for text summarization using PEGASUS transformer model. This project implements a complete MLOps pipeline for training and deploying a text summarization model.

## 🚀 Features

- **Data Ingestion**: Automated download and extraction of SAMSum dataset
- **Data Transformation**: Tokenization and preprocessing using PEGASUS tokenizer
- **Model Training**: Fine-tuning PEGASUS model on SAMSum dataset
- **Model Evaluation**: ROUGE metrics evaluation
- **REST API**: FastAPI-based prediction service
- **Docker Support**: Containerized deployment

## 📋 Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Training](#training)
- [API Usage](#api-usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Docker](#docker)
- [Contributing](#contributing)

## 🛠 Installation

### Prerequisites

- Python 3.8+
- conda (recommended for environment management)

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd nlp-text-summarizer
   ```

2. **Create conda environment**
   ```bash
   conda create -n text-summarizer python=3.8
   conda activate text-summarizer
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 📖 Usage

### Training the Model

Run the complete training pipeline:

```bash
python main.py
```

This will execute all stages:
1. Data Ingestion
2. Data Transformation
3. Model Training
4. Model Evaluation

### Starting the API Server

```bash
python app.py
```

The API will be available at `http://127.0.0.1:8080`

## 🔌 API Usage

### Get API Documentation

Visit `http://127.0.0.1:8080/docs` for interactive Swagger UI documentation.

### Prediction Endpoint

**Endpoint**: `POST /predict`

**Request Body**:
```json
{
  "text": "Your text to summarize here..."
}
```

**Response**:
```json
{
  "summary": "Generated summary text..."
}
```

### Example cURL Request

```bash
curl -X 'POST' \
  'http://127.0.0.1:8080/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"text":"Once upon a time, in a beautiful garden, there lived a proud Rose who boasted about her beauty, often insulting a Cactus growing nearby. \"You are so ugly with all those thorns!\" the Rose would say. The Cactus remained silent, never taking offense. One hot summer day, the garden dried up, and there was no water for the plants. The Rose began to wilt under the scorching sun. Soon, she saw birds pecking at the Cactus to drink water stored inside. Feeling ashamed, the Rose asked the Cactus if she could have some water, too. The kind Cactus readily agreed and shared his water, saving the Rose'\''s life."}'
```

### Training Endpoint

**Endpoint**: `GET /train`

Triggers model retraining:

```bash
curl -X 'GET' \
  'http://127.0.0.1:8080/train' \
  -H 'accept: application/json'
```

## 📁 Project Structure

```
nlp-text-summarizer/
├── app.py                          # FastAPI application
├── main.py                         # Training pipeline orchestrator
├── Dockerfile                      # Docker configuration
├── requirements.txt                # Python dependencies
├── setup.py                        # Package setup
├── params.yaml                     # Training parameters
├── config/
│   └── config.yaml                 # Configuration file
├── src/
│   └── textSummarizer/
│       ├── __init__.py
│       ├── components/             # ML pipeline components
│       │   ├── data_ingestion.py
│       │   ├── data_transformation.py
│       │   ├── model_trainer.py
│       │   └── model_evaluation.py
│       ├── config/                 # Configuration management
│       ├── constants/              # Constants
│       ├── entity/                 # Data classes
│       ├── logging/                # Logging configuration
│       ├── pipeline/               # Pipeline orchestrators
│       │   ├── prediction_pipeline.py
│       │   └── *_pipeline.py
│       └── utils/                  # Utility functions
├── artifacts/                      # Generated artifacts
│   ├── data_ingestion/
│   ├── data_transformation/
│   ├── model_trainer/
│   └── model_evaluation/
├── logs/                           # Application logs
└── research/                       # Jupyter notebooks for experimentation
```

## ⚙️ Configuration

### config/config.yaml

```yaml
artifacts_root: artifacts

data_ingestion:
  root_dir: artifacts/data_ingestion
  source_URL: https://github.com/krishnaik06/datasets/raw/refs/heads/main/summarizer-data.zip
  local_data_file: artifacts/data_ingestion/data.zip
  unzip_dir: artifacts/data_ingestion

data_transformation:
  root_dir: artifacts/data_transformation
  data_path: artifacts/data_ingestion/samsum_dataset
  tokenizer_name: google/pegasus-cnn_dailymail

model_trainer:
  root_dir: artifacts/model_trainer
  data_path: artifacts/data_transformation/samsum_dataset
  model_ckpt: google/pegasus-cnn_dailymail

model_evaluation:
  root_dir: artifacts/model_evaluation
  data_path: artifacts/data_transformation/samsum_dataset
  model_path: artifacts/model_trainer/pegasus-samsum-model
  tokenizer_path: artifacts/model_trainer/tokenizer
  metric_file_name: artifacts/model_evaluation/metrics.csv
```

### params.yaml

Training hyperparameters and configuration.

## 🐳 Docker

### Build Docker Image

```bash
docker build -t nlp-text-summarizer .
```

### Run Docker Container

```bash
docker run -p 8080:8080 nlp-text-summarizer
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- SAMSum dataset for training data
- Google PEGASUS model for base architecture
- Hugging Face Transformers library
- FastAPI framework for API development