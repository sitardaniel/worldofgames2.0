FROM python:3.9
#ADD e2e.py /
#COPY Scores.txt /Scores.txt
#RUN pip install --no-cache-dir -r requirements.tx# Use the official Python base image
#CMD ["python", "app.py"]


# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
# COPY requirements.txt .

# Upgrade pip to the latest version
RUN python -m pip install --upgrade pip

# Install project dependencies
RUN pip install flask requests

# Copy the Flask project files to the container
COPY . .

# Set the environment variables if needed
# ENV VARIABLE_NAME value

# Expose the port the Flask app will run on
EXPOSE 5000

# Set the command to run the Flask app
CMD ["python", "MainScores.py"]


