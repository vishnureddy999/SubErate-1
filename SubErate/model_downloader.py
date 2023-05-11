import openai
import os

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY"

# List the available models
models = openai.Model.list()
for model in models["data"]:
    print(model["id"])

# Download the text-davinci-002 and text-babbage-001 models
models_to_download = ["text-davinci-002", "text-babbage-001"]
for model_name in models_to_download:
    model = openai.Model.create(model=model_name)
    model.download(os.path.expanduser("./models/")) # Download the model to the default directory
