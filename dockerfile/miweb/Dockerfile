
FROM bitnami/git AS clonador
RUN git clone https://github.com/IvanciniGT/webEjemploAnsible /miweb


FROM nginx:stable
RUN rm -rf /usr/share/nginx/html
COPY --from=clonador /miweb/ /usr/share/nginx/html/

# SOLUCION QUE TE CAGAS !!!!!!