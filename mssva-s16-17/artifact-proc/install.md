## Installation of Tools

### Grype (vulnerability scanner)

```bash
curl -sSfL https://get.anchore.io/grype | sudo sh -s -- -b /usr/local/bin
```
### Falco (runtime behavioral monitor)

```bash
docker pull falcosecurity/falco:latest

docker run --rm -it --name falco \
  --privileged \
  -v /var/run/docker.sock:/host/var/run/docker.sock:ro \
  -v /dev:/host/dev:ro \
  -v /proc:/host/proc:ro \
  -v /boot:/host/boot:ro \
  falcosecurity/falco:latest
```