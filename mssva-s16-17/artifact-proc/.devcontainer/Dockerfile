FROM python:3.11-slim

RUN useradd -m appuser

WORKDIR /workspace

COPY requirements.txt tmp/requirements.txt
RUN pip install --no-cache-dir -r tmp/requirements.txt

# Copy app folder
COPY ./app /workspace/app
COPY ./artifacts /workspace/artifacts


USER appuser

EXPOSE 8080
CMD ["python", "app/main.py"]