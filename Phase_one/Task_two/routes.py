from flask import Blueprint,request,jsonify
import pickle

model_predict=Blueprint('model_predict',__name__)
@model_predict.route('/predict',methods=['POST'])
def predict():
	 nb_model = open("picklenewfile.pkl","rb")
	 clf = pickle.load(nb_model)

	 if request.method == 'POST':
		comment = request.form['comment']
		data = [comment]
		vect = cv.transform(data).toarray()
		my_prediction = clf.predict(vect)
	return render_template(prediction = my_prediction)

if __name__ == '__main__':
	model_predict.run(debug=True)