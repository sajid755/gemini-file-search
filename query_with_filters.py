"""
Query with metadata filters
"""
from config import client, DEFAULT_MODEL

def query_with_filters(question, store_names, metadata_filters=None):
    """
    Query with custom metadata filters

    Args:
        question: The question to ask
        store_names: List of store names to search in
        metadata_filters: List of filter conditions

    Returns:
        Response object
    """
    # Build file search configuration
    file_search_config = {
        'file_search_stores': store_names
    }

    # Add metadata filters if provided
    if metadata_filters:
        file_search_config['metadata_filters'] = metadata_filters

    file_search_tool = {
        'file_search': file_search_config
    }

    # Generate response
    response = client.models.generate_content(
        model=DEFAULT_MODEL,
        contents=question,
        config={
            'tools': [file_search_tool]
        }
    )

    print(f"Question: {question}")
    if metadata_filters:
        print(f"Filters: {metadata_filters}")
    print(f"\nAnswer: {response.text}")

    return response


if __name__ == "__main__":
    # Replace with your actual store names
    store_names = ["fileSearchStores/your-store-id"]

    # Example: Filter by custom metadata
    # Only search in documents where category equals "technical"
    filters = [
        {
            'key': 'category',
            'conditions': [
                {
                    'string_value': 'technical',
                    'operation': 'EQUAL'
                }
            ]
        }
    ]

    question = "What are the technical specifications?"

    response = query_with_filters(question, store_names, filters)
