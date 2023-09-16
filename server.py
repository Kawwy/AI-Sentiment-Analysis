''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package :
from flask import Flask, render_template, request

# Import the sentiment_analyzer function from the package created:
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

#Initiate the flask app :
app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """Function returning response to the user - used to increase PyLint score"""
    text_to_analyze = request.args.get('textToAnalyze')
    resp = sentiment_analyzer(text_to_analyze)
    label = resp['Label']
    score = resp['Score']
    if not label:
        return "Please provide any value"
    if label is None:
        return "Invalid input!"
    return f"The given text has been identfied as {label.split('_')[1]} with the score of {score}"

@app.route("/")
def render_index_page():
    """Function returning html page to the user - used to increase PyLint score"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
