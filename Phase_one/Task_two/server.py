from flask import Flask
import routes

ml=Flask('ml')
ml.register_blueprint(routes.model_predict)
ml.run(host='0.0.0.0',port=5005)