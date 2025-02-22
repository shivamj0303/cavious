# Cavious Assignment

## Introduction
This project implements a backend for voice-based intent recognition API using FastAPI. It processes text input (simulating voice), performs basic intent recognition, stores interactions in a database, and runs inside a Docker container. Additionally, logging is implemented to track API requests and responses.

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- Python
- Docker (for containerization)
- MongoDB/PostgreSQL (optional)

### Clone the Repository
```bash
git clone https://github.com/shivamj0303/cavious.git
```

### Running using docker container
This command uses the docker-compose.yml file available in the repository so ensure you are in the correct directory.
```bash
docker-compose up -d
```
# Testing

## 1️⃣ Check If Containers Are Running
Run the following command to check if your containers are running:

```bash
docker ps
```

You should see two containers:
- `fastapi_app` (your FastAPI app)
- `postgres_db` (PostgreSQL database)

If they are running, proceed to testing.

## 2️⃣ Test API Using Swagger UI
Open your browser and go to:

👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

This will open FastAPI’s interactive documentation.

Try making a `POST` request to `/chat` with sample text like:

```json
{
  "text": "hello"
}
```

## 3️⃣ Test API Using cURL
Open a terminal and run:

```bash
curl -X 'POST' 'http://127.0.0.1:8000/chat' \
     -H 'Content-Type: application/json' \
     -d '{"text": "hello"}'
```

Expected response:

```json
{
  "response": "Hello! How can I assist you?"
}
```

## 4️⃣ Test API Using Postman
1. Open Postman.
2. Create a new `POST` request to `http://127.0.0.1:8000/chat`.
3. In the **Body** section, select `raw`, choose `JSON`, and enter:
   
   ```json
   {
     "text": "hello"
   }
   ```
   
4. Click **Send** and check the response.

## 5️⃣ Check Logs Inside the Container
To view logs for debugging:

```bash
docker logs fastapi_app
```

This will show request details, errors (if any), and interactions.

## 6️⃣ Test Database Connection
To access the PostgreSQL database:

```bash
docker exec -it postgres_db psql -U shivam -d voice_assistant
```

Run the following SQL query to check stored chat interactions:

```sql
SELECT * FROM interactions;
```

## 7️⃣ Stop & Restart Containers
If needed, restart the containers:

```bash
docker-compose down
docker-compose up -d
```
## Thank You!


