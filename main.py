from flask import Flask

app=Flask(__name__)
#rendering the HTML page which has the button
@app.route('/json')
def json():
    return render_template('json.html')

#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    print ("Hello")
    return "nothing"
# import main_redirect
# print("rendering script")
# main_redirect.to_launch()


# @app.route('/')
# def chetans_function():
#     return 'Some Open CV work'
# app=Flask(_name_)

# app.config['DEBUG']= True
# app.secret_key="something i need"

# @app.route("/server",methods=['GET'])
# def index():
# 	if request.method=='GET':
# 		fun()
# 		response = {'this is response'}
# 		return 
# jsonify(response)

# if _name_ == '_main_':
# 	app.run(host='0.0.0.0',port=5000)



# def fun():
# 	print("i am a function")