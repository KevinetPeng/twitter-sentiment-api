build:
	docker build -t kevinp40/twitter-sentiment-api .

run: build
	docker run -d -p 5000:5000 kevinp40/twitter-sentiment-api

docker-push:
	docker push kevinp40/twitter-sentiment-api:latest