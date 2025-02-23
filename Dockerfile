FROM python:3.13

WORKDIR /competenciapp

# Install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
# .dockerignore should exclude unnecessary folders
COPY . .

# Entrypoint
COPY resources/entrypoint.sh .
RUN chmod +x ./entrypoint.sh

# Open ports
EXPOSE 8000

# Run server
ENTRYPOINT ["./entrypoint.sh"]