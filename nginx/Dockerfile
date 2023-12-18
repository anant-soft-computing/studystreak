FROM nginx:latest

# COPY ./default.conf /etc/nginx/conf.d/default.conf

RUN mkdir -p /home/app/staticfiles

RUN mkdir -p /usr/share/nginx/html

COPY ./front/ /usr/share/nginx/html