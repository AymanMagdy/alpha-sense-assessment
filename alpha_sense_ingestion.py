import os
import requests
import mimetypes
import click
import logging

# API: 
# modify-> PUT v1/modify-document/{docId} 
# upload-> POST v1/upload-document
# bulk modify-> PATCH v1/bulk/modify/metadata [docIds: Array of strings]
# delete document-> DELETE v1/delete-document/{docId}
# bulk delete-> v1/bulk/delete

ingest_url = "https://research.alpha-sense.com/services/i/ingestion-api/v1/upload-document"

# access_token = "access token"
# ClientId = "ClientId"

# # supported types: pdf, html, htm, txt, doc, docx, xls, xlsx, ppt, pptx, msg, eml, csv, xlsb, xlsm, one, tsv, ods
# folder_path = "uploads"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("ingestion.log"),
        logging.StreamHandler()
    ]
)

def get_metadata(file_name):
    return {
        "title": os.path.splitext(file_name)[0],
        "source": "LocalFileSystem",
        "language": "en",
        "industry_tags": ["US", "map"],
        "document_type": "test",
        "published_date": "2024-06-01T00:00:00Z"
    }

# uploading file with file_path
def upload_file(access_token, client_id, file_path):
    file_name = os.path.basename(file_path)
    metadata = get_metadata(file_name)

    content_type = mimetypes.guess_type(file_path)[0] or 'application/octet-stream' # treat as a raw binary if cant determine the type.

    with open(file_path, 'rb') as file_data:
        file = {
            'file': (file_name, file_data, content_type)
        }
        data = {
            'metadata': (None, str(metadata), 'application/json')
        }

        headers = {
            'Authorization': f'Bearer {access_token}',
            'ClientId':  client_id
        }

      
        logging.info(f"Making a POST request: {file_name}")
        response = requests.post(ingest_url, headers=headers, files=file, data=data)
        if response.status_code == 200 or response.status_code == 201:
            logging.info(f"Uploaded file succefully: {file_name}")
        else:
            logging.error(f"Failed to upload {file_name}")
            logging.error(response.text)
        

@click.command()
@click.option('--access_token', prompt='Enter Access Token', help='Access token.')
@click.option('--client_id', prompt='Enter ClientId',help='Client ID.')
@click.option('--folder_path', prompt='Enter folder path',help='Folder path for files to upload.')

# dir ingest all files in a directory.
def ingest_directory(access_token, client_id, folder_path):
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            logging.info(f"Uploading file: {file_name}")
            upload_file(access_token, client_id, file_path)
        else:
            logging.error(f"Failure uploading: {file_name}")

if __name__ == "__main__":
    ingest_directory()
