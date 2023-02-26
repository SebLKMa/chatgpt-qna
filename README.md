# chatgpt-qna

Factual question and answer response using ChatGPT based on OpenAI API [quickstart tutorial](https://beta.openai.com/docs/quickstart). It uses the [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework. Check out the tutorial or follow the instructions below to get set up.

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/)

2. Clone this repository

3. Navigate into the project directory

   ```bash
   $ cd openai-quickstart-python
   ```

4. Create a new virtual environment (do this unless you are developing and running inside docker)  

   ```bash
   $ python3 -m venv venv
   $ . venv/bin/activate
   ```

   You may deactivate python env by:  
   ```bash
   deactivate
   ```

5. Install the requirements

   ```bash
   $ pip3 install -r requirements.txt
   ```

6. Make a copy of the example environment variables file

   ```bash
   $ cp .env.example .env
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file

8. Run the app

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)! For the full context behind this example app, check out the [tutorial](https://beta.openai.com/docs/quickstart).

9. References

https://platform.openai.com/docs/quickstart/build-your-application  
https://platform.openai.com/docs/guides/completion/introduction  
https://rollbar.com/blog/how-to-integrate-chatgpt-into-your-python-script/#  


## Q and A for Factual Answers

```txt
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

Is Batman from Marvel?
A: No, Batman is from DC.

Q: Does Batman have a car?
A: Yes, he drives a batmobil.

Is Batman from DC?
A: Yes, Batman is from DC.

Can Batman drive?
A: Yes, Batman can drive.

What type of car does Batman drive?
A: Batman drives a batmobile.

What is batmobile?
A: The batmobile is a fictional vehicle driven by the superhero Batman. It is typically depicted as an advanced, armored car with many special features.
```


