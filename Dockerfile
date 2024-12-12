FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install Flask==2.2.2 Werkzeug==2.2.3
EXPOSE 5000
CMD ["python", "myapp.py"]
