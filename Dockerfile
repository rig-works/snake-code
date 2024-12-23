FROM python:3.9
ADD main.py .
RUN pip freeze > requirements.txt
CMD ["python", "./main.py"]