import os
from flask import Flask, render_template, url_for, request, send_file
from PIL import Image
from arguments import site_name, output_menu, site_menu

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def index():
    return render_template("index.html", title = site_name, site_menu=site_menu)

@app.route("/index")
def kek():
    return render_template("index.html", title = site_name, site_menu=site_menu)

@app.route("/about")
def about():
    return render_template("about.html", title = "Обо мне", site_menu=site_menu)

@app.route('/change-format', methods=['POST'])
def change_format():
    print(request.files)
    if 'file' not in request.files:
        return 'Нет файла!'
    file = request.files['file']
    if file.filename == '':
        return 'Нет выбранного файла!'
    input_format = request.form['input-format']
    output_format = request.form['output-format']
    filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filename)
    img = Image.open(filename)
    output_filename = f"{os.path.splitext(file.filename)[0]}.{output_format.lower()}"
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
    if output_format.upper() == 'JPG':
       output_format = 'JPEG'
    img.save(output_path, format=output_format)
    os.remove(filename)
    return render_template("result-download.html", title = "Готово!", site_menu=site_menu, filePath = output_path)

@app.route('/get-img', methods=['GET'])
def get_img():
    # Получаем путь к файлу, который нужно скачать
    file_path = request.args.get('filePath')

    if file_path and os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    return "Файл не найден", 40

if __name__ == "__main__":
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)


#with app.test_request_context():
# print(url_for("index"))