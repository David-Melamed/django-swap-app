tag=latest
organization=davidmelamed
image=django_swap_web

build:
	docker build --force-rm $(options) -t django_swap_web:latest .

build-prod:
	$(MAKE) build options="--target production"

push:
	docker tag $(image):latest $(organization)/$(image):$(tag)
	docker push $(organization)/$(image):$(tag)

compose-start:
	docker compose up --remove-orphans $(options)

compose-stop:
	docker-compose run --rm $(options) website python manage.py $(cmd)

start-server:
	python manage.py runserver 0.0.0.0:80