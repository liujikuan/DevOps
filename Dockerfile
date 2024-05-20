FROM python:3.12.3-alpine3.19

# Copy the Python script
COPY script.py /script.py

# Set the entry point
ENTRYPOINT ["python3", "/script.py"]
