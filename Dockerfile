#Entire ML Code was written Python, hence need a Python Compiler
FROM python

# Current Working Directory
WORKDIR /mlapp

# Copy the App.py from Source into WORKDIR
COPY src/predict_rental.py predict_rental.py
COPY src/data/rental_1000.csv data/rental_1000.csv
COPY requirements.txt requirements.txt

# Install all the ML Libraries
# RUN pip install numpy pandas sckit-learn

# Using Requirements.txt
RUN pip install -r requirements.txt

# EXPOSE 5000

# Run the predict_rental.py
#RUN ["python","predict_rental.py"]
CMD ["python","predict_rental.py"]