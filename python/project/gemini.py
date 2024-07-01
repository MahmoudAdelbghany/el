import google.generativeai as genai

genai.configure(api_key='')

class gemini:
    def __init__(self, model_name='gemini-1.5-flash'):
        self.model = genai.GenerativeModel(model_name)

    def get_command(self, user_text, commands):
        prompt = f"I'm using you as an intermediate stage in home assistant. I use Arabic speech to text that produce crabby text. You will be sent a list of available commands of the home assistant and the user text. If it matches one of the functions, reply only with the function name else reply with the word 'invalid'. You can't write anything else as this will break workflow.\nuser text: {user_text}\navailable commands: {str(commands)}"
        response = self.model.generate_content(prompt)
        return response._result.candidates[0].content.parts[0].text

gemi = gemini()

