FROM python:3.11.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
ARG URL=0.0.0.0:8000
CMD ["sh", "-c", "python manage.py install_labels && python manage.py runserver $URL"]

#docker build -t ms_usersocial .
#docker run -p 8000:8000 -e URL=0.0.0.0:8000 ms_usersocial