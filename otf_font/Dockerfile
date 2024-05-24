# Use the official Ubuntu base image
FROM ubuntu:latest

# Install dependencies
RUN apt-get update && apt-get install -y \
    fontforge \
    python3 \
    python3-pip

# Install FontForge Python bindings
RUN apt-get install -y python3-fontforge

# Copy the script and font to the container
COPY create_vjscript_font.py /app/create_vjscript_font.py
COPY DejaVuSans.ttf /app/DejaVuSans.ttf

# Set the working directory
WORKDIR /app

# Command to run the script
CMD ["python3", "create_vjscript_font.py"]
