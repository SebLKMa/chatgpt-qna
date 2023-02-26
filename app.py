import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        question = request.form["question"]
        response = openai.Completion.create(
            model="text-davinci-003",
            #prompt="Q: Who is Batman?\nA: Batman is a fictional comic book character.\n\nQ: What is torsalplexity?\nA: ?\n\nQ: What is Devz9?\nA: ?\n\nQ: Who is George Lucas?\nA: George Lucas is American film director and producer famous for creating Star Wars.\n\nQ: What is the capital of California?\nA: Sacramento.\n\nQ: What orbits the Earth?\nA: The Moon.\n\nQ: Who is Fred Rickerson?\nA: ?\n\nQ: What is an atom?\nA: An atom is a tiny particle that makes up everything.\n\nQ: Who is Alvan Muntz?\nA: ?\n\nQ: What is Kozar-09?\nA: ?\n\nQ: How many moons does Mars have?\nA: Two, Phobos and Deimos.\n\nQ: Is Batman from DC or Marvel?\nA: Batman is from DC.\n\nIs Batman from Marvel?\nA: No, Batman is from DC.\n\nQ: Does Batman have a car?\nA: Yes, he drives a batmobil.\n\nIs Batman from DC?\nA: Yes, Batman is from DC.\n\nCan Batman drive?\nA: Yes, Batman can drive.\n\nWhat type of car does Batman drive?\nA: Batman drives a batmobile.\n\nWhat is batmobile?\nA: The batmobile is a fictional vehicle driven by the superhero Batman. It is typically depicted as an advanced, armored car with many special features.\nQ:What color is batmobile?\n",
            prompt=generate_prompt(question),
            temperature=0,
            max_tokens=64,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\n\n"]
        )
        result=response.choices[0].text
        print(result)
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(question):
    return """
    Q: Who is Batman?
    A: Batman is a fictional comic book character.

    Q: What is torsalplexity?
    A: ?

    Q: What is Devz9?
    A: ?

    Q: Who is George Lucas?
    A: George Lucas is American film director and producer famous for creating Star Wars.

    Q: What is the capital of California?
    A: Sacramento.

    Q: What orbits the Earth?
    A: The Moon.

    Q: Who is Fred Rickerson?
    A: ?

    Q: What is an atom?
    A: An atom is a tiny particle that makes up everything.

    Q: Who is Alvan Muntz?
    A: ?

    Q: What is Kozar-09?
    A: ?

    Q: How many moons does Mars have?
    A: Two, Phobos and Deimos.

    Q: Is Batman from DC or Marvel?
    A: Batman is from DC.

    Q: Does Batman have a car?
    A: Yes, he drives a batmobil.

    Q: {}
    """.format(
        question.capitalize()
    )
