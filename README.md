# Network Attack Detection System

A machine learning-based network attack detection system with FastAPI backend and React frontend.

## Features

- Real-time network attack detection using ML models
- LIME-based explainability for predictions
- Gemini AI-powered mitigation recommendations
- Interactive React dashboard
- REST API backend

## Project Structure

```
network-attack-system/
├── network-attack-backend/     # FastAPI backend
│   ├── main.py                # Main API server
│   ├── train_model.py         # Model training script
│   ├── requirements.txt        # Python dependencies
│   └── ...model files...
├── network-attack-frontend/    # React frontend
│   ├── src/
│   ├── public/
│   ├── package.json           # Node dependencies
│   └── ...
└── run.ps1                     # One-click startup script
```

## Quick Start

### Prerequisites

- Python 3.8+
- Node.js 14+
- Git

### Run Everything with One Command

```powershell
cd network-attack-system
.\run.ps1
```

This will:

1. Set up Python virtual environment
2. Install backend dependencies
3. Install frontend dependencies
4. Start backend on `http://localhost:8000`
5. Start frontend on `http://localhost:3000`

### Manual Setup

**Backend:**

```powershell
cd network-attack-backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

**Frontend:**

```powershell
cd network-attack-frontend
npm install
npm start
```

## Configuration

Create `.env` file in `network-attack-backend/`:

```
GEMINI_API_KEY=your_api_key_here
```

## API Endpoints

- `POST /predict` - Predict network attack from CSV upload
- `POST /predict-manual` - Predict from manual input
- `POST /batch-predict` - Batch predictions
- `POST /mitigation` - Get mitigation recommendations

## Stop Services

Press `Ctrl+C` in each terminal window.

## Requirements

- FastAPI
- scikit-learn
- pandas
- numpy
- React
- See full requirements in respective `requirements.txt` and `package.json` files

## License

MIT License
