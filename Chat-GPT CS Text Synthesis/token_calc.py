import tiktoken
enc = tiktoken.encoding_for_model("gpt-3.5-turbo")
assert enc.decode(enc.encode("hello world")) == "hello world"

with open("json_file.txt", "r") as file:
    prompt = file.read()

enc.encode(prompt)

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

print(num_tokens_from_string(prompt, "cl100k_base"))