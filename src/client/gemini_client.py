import string

import google.generativeai as genai

from src.prompts.zero_shot import csv_instructions, stereotypes_explanation, ufo_explanation


class GeminiClient:
    def __init__(self, api_key: string):
        genai.configure(api_key=api_key)
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 0,
            "max_output_tokens": 8192,
        }
        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
        ]
        system_instruction = ufo_explanation + stereotypes_explanation + csv_instructions
        self.model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                           generation_config=generation_config,
                                           system_instruction=system_instruction,
                                           safety_settings=safety_settings)

    def get_completion(self, prompt):
        chat = self.model.start_chat(history=[])
        chat.send_message(content=prompt)
