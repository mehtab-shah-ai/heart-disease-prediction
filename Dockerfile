# base image
FROM python:3.10-slim

# work directory
WORKDIR /app

# pehle requirements copy karo
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# ab saara code copy karo
COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "App.py", "--server.port=8501", "--server.address=0.0.0.0"]