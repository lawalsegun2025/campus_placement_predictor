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
        
        # Predictiong the class of either 0 or 1
        predicted_class = lr_2.predict(input_features)

        # predict the probability
        predicted_prob = lr_2.predict_proba(input_features)

        print(predicted_class, predicted_prob[0][0])

        if predicted_class[0] == 1:
            proba = predicted_prob[0][1]
        else:
            proba = predicted_prob[0][0]

        print(predicted_class, proba*100)

        place_map = {1: "Will Be Placed", 0: "Beter Luck Next Time"}

        predicted_classs_end = place_map[predicted_class[0]]

        if predicted_class[0] == 1:
            return render_template('show.html', predicted_classs_end=predicted_classs_end, predicted_prob=round(proba*100, 2), placed=True)

        else:
            return render_template('show.html', predicted_classs_end=predicted_classs_end)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)