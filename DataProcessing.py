import emoji
import re

def preprocess_text(input_text):
    # Remove HTML tags and extra spaces
    cleaned_text = re.sub(r'<.*?>', '', input_text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)

    # Remove URLs
    cleaned_text = re.sub(r'http\S+', '', cleaned_text)

    # Remove digits
    cleaned_text = re.sub(r'\d', '', cleaned_text)

    # Convert emojis to text and remove duplicates
    def replace_emoji(match):
        emoji_text = emoji.demojize(match.group())
        return emoji_text

    # Replace emojis with their text representation
    cleaned_text = emoji.demojize(cleaned_text)

    # Remove duplicate emojis
    emojis = re.findall(r'(:[^:]+:)', cleaned_text)
    cleaned_emojis = list(set(emojis))  # Convert to set and back to list to remove duplicates
    emoji_pattern = '|'.join(re.escape(e) for e in cleaned_emojis)
    emoji_regex = re.compile(emoji_pattern)
    cleaned_text = emoji_regex.sub(replace_emoji, cleaned_text)

    # Add space between different emoji texts
    cleaned_text = re.sub(r'(:\w+:)(:\w+:)', r'\1 \2', cleaned_text)

    # Remove punctuation (except underscore) and unnecessary spaces between words
    punctuations_to_remove = ''.join([c for c in string.punctuation if c != '_'])
    cleaned_text = re.sub(f"[{re.escape(punctuations_to_remove)}]", '', cleaned_text)
    cleaned_text = ' '.join(cleaned_text.split())

    # Convert to lowercase and strip
    cleaned_text = cleaned_text.lower().strip()

    return cleaned_text

