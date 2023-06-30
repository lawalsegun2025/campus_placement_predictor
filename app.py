from flask import Flask, request, render_template
import pickle 


# unpickling the model
file = open("cp_predictor.pkl", "rb")
lr_2 = pickle.load(file)
file.close()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():

    if request.method == "POST":

        my_dict = request.form
        gender = int(my_dict['gender'])
        spec = int(my_dict['spec'])
        tech = int(my_dict['tech'])
        work = int(my_dict['work'])
        ssc = float(my_dict['ssc'])
        hsc = float(my_dict['hsc'])
        dsc = float(my_dict['dsc'])
        mba = float(my_dict['mba'])
        input_features = [[gender, spec, tech, work, ssc, hsc, dsc, mba]]
        