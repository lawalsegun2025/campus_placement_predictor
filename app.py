from flask import Flask, request, render_template
import pickle 


# unpickling the model
file = open("cp_predictor.pkl", "rb")
lr_2 = pickle.load(file)
file.close()