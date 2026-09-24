def load_environment_variables():
    import os
    from dotenv import load_dotenv

    load_dotenv()

def calculate_percentage(part, whole):
    if whole == 0:
        return 0
    return (part / whole) * 100

def validate_file_extension(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def generate_unique_id():
    import uuid
    return str(uuid.uuid4())

def clean_text(text):
    return ' '.join(text.split())

def extract_metadata_from_filename(filename):
    import os
    return {
        'filename': os.path.basename(filename),
        'extension': os.path.splitext(filename)[1],
        'size': os.path.getsize(filename) if os.path.exists(filename) else None
    }