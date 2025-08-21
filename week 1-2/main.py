from utils import clean_text, get_stats
import sys
sys.stdout.reconfigure(encoding='utf-8')

def main():
    # Read input text
    with open("sample.txt", "r", encoding="utf-8") as file:
        text = file.read()

    # Clean and analyze
    cleaned = clean_text(text)
    stats = get_stats(cleaned, text)

    # Display results
    print("Text Analysis Report:")
    for key, value in stats.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()