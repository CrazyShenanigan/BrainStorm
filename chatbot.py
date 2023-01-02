import openai
import colorama
import readline
openai.api_key = "Insert your api key here"
model_engine = "text-davinci-003"
while True:
    print("")
    prompt = input(colorama.Fore.YELLOW + "Ask Me Anything: " + colorama.Style.RESET_ALL)
    if prompt.lower() == "exit":
        break
    completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=3000,
            n=1,
            stop=None,
            temperature=0.5,
        )
    response = completion.choices[0].text
    print(colorama.Fore.GREEN + response + colorama.Style.RESET_ALL, end='\n\n')
