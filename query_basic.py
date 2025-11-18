"""
Basic query using File Search
"""
from config import client, DEFAULT_MODEL

def query_with_file_search(question, store_names):
    """
    Query Gemini with File Search enabled

    Args:
        question: The question to ask
        store_names: List of store names to search in

    Returns:
        Response object
    """
    # Build file search tool configuration
    file_search_tool = {
        'file_search': {
            'file_search_stores': store_names
        }
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
    print(f"\nAnswer: {response.text}")
    print()

    # Display grounding metadata if available
    if hasattr(response, 'candidates') and response.candidates:
        candidate = response.candidates[0]

        if hasattr(candidate, 'grounding_metadata'):
            grounding = candidate.grounding_metadata

            if hasattr(grounding, 'grounding_chunks') and grounding.grounding_chunks:
                print(f"Sources ({len(grounding.grounding_chunks)} chunks):")

                for i, chunk in enumerate(grounding.grounding_chunks, 1):
                    if hasattr(chunk, 'retrieved_context'):
                        context = chunk.retrieved_context
                        title = getattr(context, 'title', 'Unknown')
                        print(f"  {i}. {title}")

    return response


if __name__ == "__main__":
    # Replace with your actual store names
    store_names = ["fileSearchStores/your-store-id"]

    question = "What are the main topics discussed in the documents?"

    response = query_with_file_search(question, store_names)
