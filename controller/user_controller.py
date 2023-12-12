from app import app
from model.user_model import user_model
from flask import request
obj=user_model()

#request handler
@app.route('/user/getall')
def user_getall_controller():
    return obj.user_getall_model()

@app.route('/user/addone', methods=["POST"])
def user_addone_controller():
    return obj.user_addone_model(request.form)

# @app.route('/user/update', methods=["PUT"])
# def user_update_controller():
#     return obj.user_update_model(request.form)

@app.route('/user/getpurse',methods=["GET"])
def user_getpurse_controller():
    return obj.user_getpurse_model(request.form)

@app.route('/user/selectedteam',methods=["GET"])
def user_selectedteam_controller():
    return obj.user_selectedteam_model(request.form)

@app.route('/user/delete', methods=["DELETE"])
def user_delete_controller():
    return obj.user_delete_model(request.form)

