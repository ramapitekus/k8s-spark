FROM apache/spark:3.4.1
USER root
RUN pip install jupyter
RUN curl -Lo coursier https://git.io/coursier-cli
RUN chmod +x coursier
RUN ./coursier launch --fork almond:0.13.12 --scala 2.12.17 -- --install
RUN rm -f coursier