# Simple Key-Value Store

This is a simple in-memory key-value store implemented in Python with a Flask API.

## Features
- Store and retrieve key-value pairs in memory
- Flask API endpoints:
  - `POST /set` - store a value
  - `GET /get/<key>` - retrieve a value

## Run with Docker
1. Build Docker image:
```bash
docker build -t simple-kv-store .
