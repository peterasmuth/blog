FROM python:3
ADD . /
RUN pip install flask
EXPOSE 8080:5000
CMD [ "python", "blog.py" ]
