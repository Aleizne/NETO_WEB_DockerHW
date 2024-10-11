FROM python:3.8

WORKDIR /dj_app

COPY ./dj_app /dj_app

# RUN pip install -r /dj_app/requirements.txt
RUN pip install --upgrade pip; \
    pip install -r /dj_app/requirements.txt



ENV SECRET_KEY=django-insecure-9m2%u2yq=+#)6c#^j7^1p+@mpiob-r)9ki+zrv%*ad779fz89l
ENV DEBUG=1

RUN python manage.py migrate


CMD ["gunicorn", "--bind", "0.0.0.0:8000", "smart_home.wsgi"]