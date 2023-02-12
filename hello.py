from flask import Flask, request, send_file, make_response, url_for, render_template
import edge_ded

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route("/process_image", methods=['GET', 'POST'])
def process_image():
    form = request.form
    threshold = form["threshold"]
    img = request.files['in_img']
    i_path = "static\\image.jpg"
    img.save(i_path)
    t2 = edge_ded.main(float(threshold))
    print(t2)
    i_name = form["FN"]
    return render_template("output.html", img_name=form["FN"], time=t2)

@app.route("/image")
def image():
    with open("image.jpg", "rb") as f:
        image_data = f.read()

    response = make_response(image_data)
    response.content_type = "image/jpeg"

    return response

@app.route('/submit', methods=['POST'])
def submit():
    form_data = request.form
    name = form_data.get('name')
    email = form_data.get('email')
    password = form_data.get('password')

    # Do something with the form data
    # ...

    return "Form data received. Name: {}, Email: {}, Password: {}".format(name, email, password)

if __name__ == '__main__':
   app.run(host="0.0.0.0", debug=True)