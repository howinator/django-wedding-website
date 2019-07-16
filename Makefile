run_docker: SHELL:=/bin/bash
run_docker:
	docker run --rm -it -p 8885:80 -v "$$(pwd)/client/build":/usr/share/nginx/html howinator/benefielinthelove

build: build_statics build_statics_docker build_docker push

build_statics:
	docker-compose run web python manage.py collectstatic --noinput

build_statics_docker:
	docker build -f Dockerfile.statics -t howinator/benefielinthelove-statics:$(version) ./static_root

build_docker:
	docker build -t howinator/benefielinthelove:$(version) .

push:
	docker push howinator/benefielinthelove:$(version) 
	docker push howinator/benefielinthelove-statics:$(version)
