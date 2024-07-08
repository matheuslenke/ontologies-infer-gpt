import vertexai
from vertexai.generative_models import GenerativeModel
import vertexai.preview.generative_models as generative_models
from src.prompts.zero_shot import instructions, stereotypes_explanation, ufo_explanation
from src.prompts.few_shot import ufo_instructions, stereotypes, generate_instructions, examples

generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}


class GeminiClient:
    def __init__(self):
        system_instruction = ufo_instructions + stereotypes + examples + generate_instructions
        vertexai.init(project="gemini-code-project", location="us-central1")
        self.model = GenerativeModel(
           model_name="gemini-1.5-pro",
           generation_config=generation_config,
           system_instruction=[system_instruction],
           safety_settings=safety_settings
        )

    def get_completion(self, prompt):
        return self.model.generate_content(
            prompt,
            stream=True
        )
