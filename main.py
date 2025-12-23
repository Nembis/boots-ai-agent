import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from functions.call_function import call_function
from config import MODEL, MAX_ITERATIONS


available_functions = [
    types.Tool(function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file
    ])
]

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        raise RuntimeError("Missing GEMINI_API_KEY")

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.prompt)])]

    client = genai.Client(api_key=api_key)

    iter = 0
    while True:
        iter += 1
        if iter > MAX_ITERATIONS:
            print(f"Maximum iterations ({MAX_ITERATIONS}) reached.")
            sys.exit(1)

        try:
            final_response = generate_content(client, messages, args.verbose)
            if final_response:
                print("Final Response:")
                print(final_response)
                break
        except Exception as e:
            print(f"Error: while in loop {e}")
            break

def generate_content(client, messages, verbose):
    response = client.models.generate_content(
            model=MODEL, 
            contents=messages,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                tools=available_functions
            )
        )
    if not response.usage_metadata:
        raise RuntimeError("Gemini API response appears to be malformed")

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    if response.candidates:
        for candidate in response.candidates:
            messages.append(candidate.content)

    if not response.function_calls:
        return response.text

    response_list = []
    for function_call_part in response.function_calls:
        function_call_response: types.Content = call_function(function_call_part, verbose=verbose)
        if (
            not function_call_response.parts or
            not function_call_response.parts[0].function_response or
            not function_call_response.parts[0].function_response.response
        ):
            raise Exception("empty function call result")
        if verbose:
            print(f"-> {function_call_response.parts[0].function_response.response}")
        response_list.append(function_call_response.parts[0])

    messages.append(types.Content(parts=response_list, role="user"))


if __name__ == "__main__":
    main()
