# Water Demand Prediction and Management System

A comprehensive web application for predicting water demand, managing water resources, and providing intelligent recommendations for water conservation.

## 🌟 Features

### Core Features

- **Water Demand Prediction**: Predict daily water demand using machine learning
- **Real-time Monitoring**: Live sensor data integration
- **Storage Recommendations**: Personalized water storage planning
- **Data Visualization**: Interactive charts and analytics
- **User Management**: Secure authentication and authorization
- **Multi-language Support**: English and Amharic interface
- **Responsive Design**: Works on desktop and mobile devices

### Advanced Features

- Risk assessment and alerts
- Water conservation tips
- API endpoints for integration
- Admin dashboard for system management
- Data export functionality
- Automated reporting
- Historical data analysis
- Export functionality for reports
- Admin dashboard for system management

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- PostgreSQL 12+
- Redis 6+
- Node.js 16+ (for frontend assets)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/water-demand-api.git
   cd water-demand-api
   ```

2. **Create and activate a virtual environment**
   ```bash
   # On Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Initialize the database**
   ```bash
   flask db upgrade
   ```

6. **Run the development server**
   ```bash
   flask run
   ```

## 🐳 Docker Setup

1. **Build and start the containers**
   ```bash
   docker-compose up -d --build
   ```

2. **Initialize the database**
   ```bash
   docker-compose exec web flask db upgrade
   ```

3. **Create an admin user**
   ```bash
   docker-compose exec web flask users create-admin
   ```

The application will be available at http://localhost:5000

## 📚 API Documentation

API documentation is available at `/api/docs` when running the application.

## 🌍 Environment Variables

Key environment variables:

- `DATABASE_URL`: Database connection URL
- `SECRET_KEY`: Secret key for session management
- `FLASK_ENV`: Environment (development/production)
- `MAIL_SERVER`, `MAIL_PORT`, `MAIL_USE_TLS`, `MAIL_USERNAME`, `MAIL_PASSWORD`: Email configuration
- `REDIS_URL`: Redis connection URL for caching and rate limiting

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to all contributors who have helped shape this project.
- Built with ❤️ using Flask and Python.
- RESTful API for integration with other systems

## Prerequisites

- Python 3.8+
- PostgreSQL 12+ (or SQLite for development)
- Node.js 14+ (for frontend assets)
- Redis (for background tasks, optional)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/water-demand-api.git
cd water-demand-api
```

### 2. Set up a virtual environment

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory:

```env
FLASK_APP=app
FLASK_ENV=development
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///app.db  # For development
# DATABASE_URL=postgresql://user:password@localhost/water_demand  # For production

# Optional settings
UPLOAD_FOLDER=./uploads
MAX_CONTENT_LENGTH=16777216  # 16MB max upload size
MAIL_SERVER=smtp.example.com
MAIL_PORT=587
MAIL_USE_TLS=1
MAIL_USERNAME=your-email@example.com
MAIL_PASSWORD=your-email-password
```

### 5. Initialize the database

```bash
flask init-db
flask create-user admin@example.com admin --admin
```

## Running the Application

### Development Mode

```bash
flask run
```

The application will be available at http://localhost:5000

### Production Mode

For production, use a WSGI server like Gunicorn:

```bash
gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app
```

## Project Structure

```
water-demand-api/
├── app/                      # Application package
│   ├── commands/             # CLI commands
│   ├── models/               # Database models
│   ├── routes/               # Application routes
│   ├── static/               # Static files (CSS, JS, images)
│   ├── templates/            # Jinja2 templates
│   ├── utils/                # Utility functions
│   ├── __init__.py           # Application factory
│   └── config.py             # Configuration settings
├── migrations/               # Database migrations
├── tests/                    # Test suite
├── .env.example              # Example environment variables
├── .gitignore
├── config.py                 # Main configuration
├── requirements.txt          # Python dependencies
└── wsgi.py                  # WSGI entry point
```

## API Documentation

The API documentation is available at `/api/docs` when running the application.

### Authentication

Most API endpoints require authentication. Include the API token in the request header:

```
Authorization: Bearer your-api-token
```

### Available Endpoints

- `GET /api/predict` - Get water demand prediction
- `POST /api/sensor-data` - Submit sensor data
- `GET /api/history` - Get prediction history
- `GET /api/stats` - Get system statistics

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to all contributors who have helped with this project
- Built with Flask and other amazing open source libraries
