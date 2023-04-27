from flask import Flask, Response, request, render_template, send_file, redirect
import json, os, requests, base64, re, io, pandas as pd, math, numpy as np
from imageio import imread
from dotenv import load_dotenv

load_dotenv()
DEV_PORT = int(os.getenv("port"))

def compress_image(image_ndarray):
    pixel_list = []
    for i in range(image_ndarray.shape[0]):
        for j in range(image_ndarray.shape[1]):
            pixel = math.floor(np.mean(image_ndarray[i,j]))
            pixel_list.append(pixel)
    return pixel_list

def get_image_df_X(b64_string):
    image = imread(io.BytesIO(base64.b64decode(b64_string)))
    row = compress_image(image)
    column_list = []
    for i in range(len(row)):
        column_list.append("frag_" + str(i))
    df_X = pd.DataFrame([row], columns=column_list)
    return df_X


app = Flask("Classify Server")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result")
def display_result():
    answer = request.args.get("answer")
    context = {}
    context['answer'] = answer
    return render_template("result.html", context=context)

@app.route("/classify", methods=["POST"])
def classify():
    #link to function that calculates answer and set
    # that equal to result
    request_body = request.json
    print(request_body)
    image_64 = request_body['Image']
    image_64 = re.findall("base64,(.+)", image_64)[0]
    #print(image_64)
    #convert image to df_X
    image_df_X = get_image_df_X(image_64)
    print(image_df_X)
    #run image through model
    #result = predict(image_row)

    result = "0" #TODO To be replaced with the actual result
    if result:
        msg_json = json.dumps({"answer" : result})
        return Response(msg_json, mimetype='application/json', status=200)
    else:
        msg_json = json.dumps({"message" : "Error"})
        return Response(msg_json, mimetype='application/json', status=500)

if __name__=="__main__":
    app.run(debug=True, port=DEV_PORT) 
    # When no port is specified, starts at default port 5000