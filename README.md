# Microblock

![build badge](https://github.com/malwaredllc/microblock/actions/workflows/python-app.yml/badge.svg)

A minimal blockchain implementation with an interactive user interface which allows the user to visually explore the blockchain. Supports distributed consensus amongst a network of nodes mining on this blockchain.

<img src="docs/preview.png" width="100%">

### Requirements
- [Docker](https://docs.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Steps to Run
1. From the root directory, run `docker-compose up`
2. Once this builds the images and initializes the containers, you can navigate to `http://0.0.0.0:3000` in your browser to interact with the application. **NOTE**: 
3. Also, the backend API to interact with the blockchain directly is on port 5000.
