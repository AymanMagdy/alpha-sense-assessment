# AlphaSense Ingestion Script

This Python script is designed to **ingest documents from a local directory** into the [AlphaSense Ingestion API](https://research.alpha-sense.com/services/i/ingestion-api/v1/upload-document). It reads each file, tags it with required metadata, and uploads it using a secure authenticated POST request.

---

## What It Does

- Reads all files from a specified folder.
- Tags each file with structured metadata.
- Uploads the file and metadata to the AlphaSense API via a multipart HTTP POST request.
- Logs the success or failure of each upload in real-time.
- The script also uses `click` library to run as a command line script.
---

## How to Run It

1. **Install dependencies**
   ```bash
   # running with Python 3.12.4
   pip install -f requirements.txt
   ```

2. **Run the script**
```bash
python alpha_sense_ingestion.py --access_token="ACCESS_TOKEN" --client_id="ClientId" --folder_path="FOLDER_PATH_TO_UPLOAD"
```

3. **Configurations to path as command line parameters**

| Parameter     | Description                                   |
| ------------- | --------------------------------------------- |
| `API_KEY`     | Your AlphaSense Bearer token (required)       |
| `CLIENT_ID`   | Your client identifier (if required by API)   |
| `FOLDER_PATH` | Path to the folder containing files to ingest |

4. **Metadata**

| Parameter     | 
| ------------- | 
| `title`     | 
| `language`   |
| `industry_tags` | 
| `document_type` | 
| `published_date` | 

---
## How to improve
Improvements to Implement:
- Parallel Ingestion: Use ThreadPoolExecutor or asyncio to ingest files faster while respecting API rate limits.

- Rate Limiting & Retry Logic: Avoid hitting API limits or losing files due to temporary failures.

- Persistent Error Logging
- Write failed uploads to a retry queue or error log with reason codes.

- Environment Configuration
Use .env or environment variables for storing sensitive configs like API keys.

- File Format Validation: Skip or report unsupported file types cleanly.

