# ATM Flask Application

This is a Flask-based Automated Teller Machine (ATM) application. It provides a web interface for managing bank accounts and performing ATM operations.

## Project Structure

- `app.py`: Main Flask application file.
- `atm.py`: Core ATM logic.
- `bank.py`: Bank-related operations.
- `models.py`: Database models.
- `templates/`: HTML templates for the web interface.
- `test.py`: Test cases for the application.
- `requirements.txt`: Python dependencies.
- `.env`: Environment variables.
- `secrete_key.py`: Secret keys for the application.

## Setup Instructions

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**:
   ```bash
   python app.py
   ```

3. **Access the application**:
   Open your browser and navigate to `http://localhost:5000`.

## Testing

Run the test suite to ensure all components are functioning correctly:
```bash
python test.py
```

## Contributing

Feel free to fork the repository and submit pull requests for any improvements or bug fixes.
