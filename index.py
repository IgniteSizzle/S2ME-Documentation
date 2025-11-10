from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/welcome')
def index():
    return render_template('pages/index.html')
    
@app.route('/install')
def install():
    return render_template('pages/help_to_install.html')
    
@app.route('/tutorial')
@app.route('/tutorial_midlet')
def tutorial_midlet():
    return render_template('pages/baseMidlet.html')
    
@app.route('/tutorial_alert')
def tutorial_alert():
    return render_template('pages/baseAlert.html')
    
@app.route('/tutorial_canvas')
def tutorial_canvas():
    return render_template('pages/baseCanvas.html')
    
@app.route('/first_scene')
def first_scene():
    return render_template('components/firstScene.html')

@app.route('/sceneManager')
def sceneManager():
    return render_template('components/sceneManager.html')

@app.route('/audioPlayer')
def audioPlayer():
    return render_template('components/audioPlayer.html')

@app.route('/buttonView')
def buttonView():
    return render_template('components/buttonView.html')

@app.route('/cursorView')
def cursorView():
    return render_template('components/cursorView.html')

@app.route('/gameSaveManager')
def gameSaveManager():
    return render_template('components/gameSaveManager.html')

@app.route('/imageView')
def imageView():
    return render_template('components/imageView.html')

@app.route('/textBlitter')
def textBlitter():
    return render_template('components/textBlitter.html')
    
@app.route('/lmelib')
def lmelib():
    return render_template('components/lmelib.html')

@app.route('/player')
def player():
    return render_template('components/player.html')

@app.route('/tilesetMap')
def tilesetMap():
    return render_template('components/tilesetMap.html')

@app.route('/undertaleBox')
def undertaleBox():
    return render_template('components/undertaleBox.html')
    
if __name__ == '__main__':
    app.run(debug=True)
