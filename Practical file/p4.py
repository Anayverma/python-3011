import sys

def word_count(text):
    words = text.split()
    return len(words)

def main():
    # Check if there are command line arguments
    if len(sys.argv) != 2:
        print("Usage: python script.py 'your text here'")
        sys.exit(1)
    input_text = sys.argv[1]
    # Calculate word count
    count = word_count(input_text)
    # Print the result
    print(f"Word count: {count}")

if __name__ == "__main__":
    main()
