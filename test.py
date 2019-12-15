from flask import Flask,url_for,request,render_template
import cube_result_test
import cube_transform_test
import json
import kociemba
import statearray2returnmsg
import numpy as np

app = Flask(__name__)

def solve(state):
    load_states = json.loads(state)  # 字符串到数组
    print(load_states)
    load_stats1 = np.array(load_states)
    load_stats2 = np.array(load_stats1).reshape((6, 9))
    return statearray2returnmsg.state2result(load_stats2)

@app.route('/solvecube')
def solvecube():
    state = request.args.get("state")
    return solve(state)
    
@app.route('/solvetext')
def solvetext():
    white =  request.args.get("white")
    yellow = request.args.get("yellow")
    orange = request.args.get("orange")
    red =    request.args.get("red")
    blue =   request.args.get("blue")
    green =  request.args.get("green")
    state = '['+white+','+yellow+','+orange+','+red+','+blue+','+green+']'
    print(state)
    return solve(state)
    
if __name__ == '__main__':
    app.debug = True # 设置调试模式，生产模式的时候要关掉debug
    app.run()