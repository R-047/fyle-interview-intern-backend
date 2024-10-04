FROM python:3.9-slim

RUN mkdir /classroom-backend
WORKDIR /classroom-backend
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=core/server.py
RUN flask db upgrade -d core/migrations/
RUN pytest --cov --cov-report html:/classroom-backend/coverage

CMD ["bash", "run.sh"]
EXPOSE 7755
