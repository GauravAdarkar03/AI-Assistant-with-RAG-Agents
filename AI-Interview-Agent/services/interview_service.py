import json

from services.llm_service import LLMService

class InterviewService:

    @staticmethod
    def generate_question():

        with open(
            "prompts/interviewer.txt",
            "r"
        ) as f:

            system_prompt = f.read()

        messages = [

            {
                "role": "system",
                "content": system_prompt
            },

            {
                "role": "user",
                "content":
                "Generate a Kubernetes interview question in JSON."
            }

        ]

        response = LLMService.generate(messages)

        return response