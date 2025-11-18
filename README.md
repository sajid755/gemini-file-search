# Gemini File Search Guide

Simple Python scripts demonstrating Google Gemini File Search API operations.

## Prerequisites

- Python 3.8 or higher
- Google Cloud API key with Gemini API access
- google-genai Python package version 1.49 or higher

## Installation

1. Clone or download this repository

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_api_key_here
```

You can copy `.env.example` and fill in your API key.

## Project Structure

```
gemini-file-search-guide/
├── config.py                    # Shared configuration and client setup
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment template
├── README.md                    # This file
│
├── Store Operations
│   ├── store_create.py          # Create a new file search store
│   ├── store_list.py            # List all stores
│   ├── store_get.py             # Get store details
│   ├── store_update.py          # Update store metadata
│   ├── store_delete.py          # Delete a store with force option
│   └── store_tree.py            # Display stores and documents in tree
│
├── Document Operations
│   ├── document_upload.py       # Upload a file to a store
│   ├── document_list.py         # List documents in a store
│   ├── document_get.py          # Get document details
│   ├── document_update.py       # Update document metadata
│   └── document_delete.py       # Delete a document with force option
│
└── Query Operations
    ├── query_basic.py           # Basic file search query
    ├── query_with_filters.py    # Query with metadata filters
    └── query_with_grounding.py  # Extract detailed source citations
```

## Usage

Each script is standalone and can be run independently.

### Store Operations

Create a new store:
```bash
python store_create.py
```

List all stores:
```bash
python store_list.py
```

View store and document tree:
```bash
python store_tree.py
```

Delete a store (including all documents):
```bash
python store_delete.py
```

### Document Operations

Upload a document:
```bash
python document_upload.py
```

List documents in a store:
```bash
python document_list.py
```

Delete a document:
```bash
python document_delete.py
```

### Querying

Basic query:
```bash
python query_basic.py
```

Query with metadata filters:
```bash
python query_with_filters.py
```

Query with source extraction:
```bash
python query_with_grounding.py
```

## Modifying Scripts

Each script contains example values that need to be replaced:

- `store_name = "fileSearchStores/your-store-id"` - Replace with actual store ID
- `file_path = "path/to/your/document.pdf"` - Replace with actual file path
- `document_name = "fileSearchStores/store-id/documents/doc-id"` - Replace with actual document ID

Store IDs and document IDs are returned when you create them using the respective scripts.

## Important Notes

### Force Deletion

Both store and document deletion support a `force` parameter:

- `force=True` (default): Deletes documents even if they have been indexed
- `force=False`: Only deletes empty stores or non-indexed documents

Example:
```python
delete_store(store_name, force=True)  # Deletes store and all documents
delete_document(document_name, force=True)  # Deletes indexed document
```

### Document States

Documents can be in different states:
- `STATE_ACTIVE` - Document is ready and searchable
- `STATE_PROCESSING` - Document is being indexed
- `STATE_FAILED` - Document processing failed

### Metadata Filters

Documents can have custom metadata that can be used for filtering during queries:

```python
# Upload with metadata
custom_metadata = {"category": "technical", "version": "1.0"}

# Query with filter
filters = [
    {
        'key': 'category',
        'conditions': [{
            'string_value': 'technical',
            'operation': 'EQUAL'
        }]
    }
]
```

### Grounding Metadata

Query responses include grounding metadata that shows which documents were used:

```python
# Access grounding chunks
if hasattr(chunk, 'retrieved_context'):
    context = chunk.retrieved_context
    title = getattr(context, 'title', 'Unknown')
```

## API References

- [Google Gemini API Documentation](https://ai.google.dev/gemini-api/docs)
- [File Search API](https://ai.google.dev/gemini-api/docs/file-search)
- [Python SDK](https://github.com/googleapis/python-genai)

## License

This guide is provided as-is for educational purposes.
