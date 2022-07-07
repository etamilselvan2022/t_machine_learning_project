from flask import Flask
import os,sys
from housing.exception import HousingException
from housing.logger import logging

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    try:
        logging.info('Custom logging module')
        return "FSDS CI/CD Pipeline"
    except Exception as e:
        logging.error(f'error_message:{e}')
        raise HousingException(e,sys) from e

   



if __name__=="__main__":
    app.run(debug=True)    