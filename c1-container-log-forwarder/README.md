# Cloud One Container Security Runtime Events Forwarder

Fill the file `/env/log_forwarder.env` with the relevant information.

To run in continuously, simply run it as a container:
```sh
docker build -t c1cs_log_forwarder .
docker run --rm -d --name c1cs_log_forwarder c1cs_log_forwarder
```

Docker Compose
```sh
docker compose up -d
```