@echo off
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
pip install wheel
pip install Flask==2.3.3 pandas==1.5.3 scikit-learn==1.0.2 numpy==1.21.6 plotly==5.17.0 flask-cors==4.0.0
