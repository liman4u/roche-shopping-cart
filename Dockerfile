FROM python:3.9
WORKDIR /roche_shopping_cart

COPY ./requirements.txt /roche_shopping_cart/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /roche_shopping_cart/requirements.txt

COPY ./app /roche_shopping_cart/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
