FROM python:3
ADD . /
RUN pip install -r requirements.txt
EXPOSE 8080:5000
CMD [ "python", "blog.py" ]
