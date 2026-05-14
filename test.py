import google.generativeai as genai

genai.configure(api_key="AIzaSyDo3EfNgzMSzT1K879Ya3voFZnRtmuJyEc")

models = genai.list_models()

for m in models:
    print(m.name)