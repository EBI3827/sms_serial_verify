from flask import Flask
app=Flask(__name__)


@app.route('/')
def main_page():
    '''this is the main page of the site
    '''
    return "Hello" 
    

@app.route('/bye')
def byee():
    return 'bye'