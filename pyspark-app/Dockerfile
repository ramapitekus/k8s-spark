FROM apache/spark:3.4.1

WORKDIR /workspace
COPY . /workspace

CMD ["/opt/spark/bin/spark-class", "org.apache.spark.deploy.worker.Worker"]