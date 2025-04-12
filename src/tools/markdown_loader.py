from crewai.tools import tool


@tool("Markdown Loader Tool")
def markdown_loader(file_path: str) -> str:
    """Loads the contents of a markdown file given its file path."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: File not found at path {file_path}"
    except Exception as e:
        return f"Error reading file: {str(e)}"
