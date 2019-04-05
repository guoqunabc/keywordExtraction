import textrank
textrank.setup_environment()
def extract_phrases(filename):
    """Print key-phrases to stdout."""
    with open(filename) as f:
        phrases = textrank.extract_key_phrases(f.read())
        print(phrases)
extract_phrases('1.txt')

