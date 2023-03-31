# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import openai

openai.api_key = "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"
model_engine = "text-davinci-003"


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(input('Enter Your Name: '))
print("Do you want to ask ChatGpt any question?if Yes press 1,otherwise press Enter:")
i = (input())
while i == '1':
    prompt = input("Enter your query:")
    completion = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=2000, n=1, stop=None,
                                          temperature=0.7)
    message = completion.choices[0].text
    print(message)
    print("Do you want to ask ChatGpt any other question?if Yes press 1,otherwise press Enter:")
    i = input()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
