# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
# ENV NAME World

# Run gunicorn when the container launches
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["gunicorn", "linkshortner.wsgi:application", "-t", "30", "--workers", "4", "--bind", "0.0.0.0:8000"]
