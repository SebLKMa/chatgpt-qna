# chatgpt-qna

Factual question and answer response using ChatGPT based on OpenAI API [quickstart tutorial](https://beta.openai.com/docs/quickstart). It uses the [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework. Check out the tutorial or follow the instructions below to get set up.

## IMPORTANT: Data Privacy, Intellectual Property

You must read this section before starting any ChatGPT project

**Can you delete specific prompts?**

   **No, we are not able to delete specific prompts from your history. Please don't share any sensitive information in your conversations.**

```txt
can you delete my prompts?

As an AI language model, I do not have the ability to delete your prompts or any other data. I am designed to process and respond to text input, and I do not have any control over the data or prompts that are fed to me.

If you have entered any sensitive or personal information, it is important to be cautious about sharing that information and take appropriate measures to protect your privacy. If you are concerned about the security of your data, you should consider using a secure and trusted communication channel, such as an encrypted messaging app or a private email service.
```

Beware and mitigate risks below:   

https://help.openai.com/en/articles/6783457-chatgpt-general-faq  
```txt
Who can view my conversations?

    As part of our commitment to safe and responsible AI, we review conversations to improve our systems and to ensure the content complies with our policies and safety requirements. 

Will you use my conversations for training?

    Yes. Your conversations may be reviewed by our AI trainers to improve our systems.

Can you delete specific prompts?

    No, we are not able to delete specific prompts from your history. Please don't share any sensitive information in your conversations.

Where do you save my personal and conversation data?

    For more information on how we handle data, please see our Privacy Policy and Terms of Use.
```

```txt
3. Content

(a) Your Content. You may provide input to the Services (“Input”), and receive output generated and returned by the Services based on the Input (“Output”). Input and Output are collectively “Content.” As between the parties and to the extent permitted by applicable law, you own all Input, and subject to your compliance with these Terms, OpenAI hereby assigns to you all its right, title and interest in and to Output. OpenAI may use Content as necessary to provide and maintain the Services, comply with applicable law, and enforce our policies. You are responsible for Content, including for ensuring that it does not violate any applicable law or these Terms.

(b) Similarity of Content. Due to the nature of machine learning, Output may not be unique across users and the Services may generate the same or similar output for OpenAI or a third party. For example, you may provide input to a model such as “What color is the sky?” and receive output such as “The sky is blue.” Other users may also ask similar questions and receive the same response. Responses that are requested by and generated for other users are not considered your Content.

(c) Use of Content to Improve Services. One of the main benefits of machine learning models is that they can be improved over time. To help OpenAI provide and maintain the Services, you agree and instruct that we may use Content to develop and improve the Services. You can read more here about how Content may be used to improve model performance. We understand that in some cases you may not want your Content used to improve Services. You can opt out of having Content used for improvement by contacting support@openai.com with your organization ID. Please note that in some cases this may limit the ability of our Services to better address your specific use case.
```

https://openai.com/privacy/
https://openai.com/terms/    


https://www.channelnewsasia.com/commentary/chatgpt-ai-data-privacy-collection-personal-information-3262871  

https://www.information-age.com/chatgpt-vs-gdpr-what-ai-chatbots-mean-for-data-privacy-123501570/  

https://www.forbes.com/sites/joemckendrick/2022/12/21/who-ultimately-owns-content-generated-by-chatgpt-and-other-ai-platforms/?sh=92f3ed95423a  

https://qz.com/open-ai-underpaid-200-kenyans-to-perfect-chatgpt-1850005025  

https://proton.me/blog/privacy-and-chatgpt  


## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/)

2. Clone this repository

3. Navigate into the project directory

   ```bash
   $ cd chatgpt-qna
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


