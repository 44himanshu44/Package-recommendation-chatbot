from utils import *
from flask import Flask, render_template, request



app = Flask(__name__)
app.static_folder = 'static'




df = pd.read_csv("data/package_recommend.csv")
data_fill = find_entity("create empty dictionary")

df2 = df.copy()
features = ["Package", "Sub_package", "Prop_type", "Difficulty_level"]





@app.route("/") 
def home():
    return render_template("index.html")                                                                                                        


@app.route("/get")
def get_bot_response():
    global df
    global data_fill
    global df2
    global features
    
    
    string = request.args.get('msg')
    response,data_fill,features,df2 = get_user_info(string,data_fill,features,df2)
    return response



if __name__ == "__main__":
    app.run(debug=True)