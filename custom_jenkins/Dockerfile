# Use official Jenkins LTS image (multi-arch, supports arm64)
FROM jenkins/jenkins:lts

# Switch to root for installations
USER root

# Install prerequisites (ca-certificates, curl, gnupg for repo setup)
RUN apt-get update && \
    apt-get install -y ca-certificates curl gnupg && \
    rm -rf /var/lib/apt/lists/*

# Add Docker's official GPG key (modern method, avoids deprecated apt-key)
RUN install -m 0755 -d /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc && \
    chmod a+r /etc/apt/keyrings/docker.asc

# Add Docker repo (use bookworm for Debian 12, auto-detect arch for arm64/amd64)
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian $( . /etc/os-release && echo "$VERSION_CODENAME") stable" | \
    tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update and install Docker packages (docker-ce, cli, containerd, buildx, compose v2)
RUN apt-get update && \
    apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin && \
    rm -rf /var/lib/apt/lists/*

# Add Jenkins user to the Docker group (create if it doesn't exist)
RUN groupadd -f docker && \
    usermod -aG docker jenkins

# Create the Docker directory and volume for DinD
RUN mkdir -p /var/lib/docker
VOLUME /var/lib/docker

# Switch back to the Jenkins user
USER jenkins