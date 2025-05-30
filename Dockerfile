FROM --platform=linux/amd64 python:3.12-slim
# Setup the application
WORKDIR /app
COPY ./app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app .
# Start the application
EXPOSE 8000
CMD ["python", "app.py"]
