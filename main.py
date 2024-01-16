import openai
from openai import OpenAI

client = OpenAI(api_key = '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')

def get_completion(prompty, model="gpt-3.5-turbo"):
    # messages = [{"role": "user", "content": prompt}]
    try:
        response = client.completions.create(
            prompt= prompty,
            model="gpt-4"
        )
    except openai.APIError as e:
        print(f"OpenAI API returned an API Error: {e}")
        pass
    except openai.APIConnectionError as e:
        print(f"Failed to connect to OpenAI API: {e}")
        pass
    except openai.RateLimitError as e:
        print(f"OpenAI API request exceeded rate limit: {e}")
        pass

def describe_image(file_path):
    try:
        with open(file_path, 'rb') as image_file:
            print(file_path)
            data = image_file.read()
            prompt = f""" Describe the image at the following URL: {file_path} """
            final_response = get_completion(prompt)
            return final_response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

image_description = describe_image('cir3.png')
print(image_description)

