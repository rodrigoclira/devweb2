import os
from app import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from confluent_kafka import Producer
import time
import json
from uuid import uuid4

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
TOPIC='image'

def delivery_report(errmsg, data):
    """
    Reports the Failure or Success of a message delivery.
    Args:
        errmsg  (KafkaError): The Error that occured while message producing.
        data    (Actual message): The message that was produced.
    Note:
        In the delivery report callback the Message.key() and Message.value()
        will be the binary format as encoded by any configured Serializers and
        not the same object that was passed to produce().
        If you wish to pass the original object(s) for key and value to delivery
        report callback we recommend a bound callback or lambda where you pass
        the objects along.
    """
    if errmsg is not None:
        print("Delivery failed for Message: {} : {}".format(data.key(), errmsg))
        return
    print('Message: {} successfully produced to Topic: {} Partition: [{}] at offset {}'.format(
        data.key(), data.topic(), data.partition(), data.offset()))


def get_json_str(timestamp, filename):
    d = {
        'timestamp': timestamp,
        'new_file': filename,
    }
    return json.dumps(d)


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/upload-img', methods=['POST'])
def upload_image():
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		flash('No image selected for uploading')
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		if not os.path.exists(app.config['UPLOAD_FOLDER']):
			os.makedirs(app.config['UPLOAD_FOLDER'])
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		#print('upload_image filename: ' + filename)
		flash('Image successfully uploaded.')
		publish(TOPIC, filename)
		return render_template('upload.html', filename=filename)
	else:
		flash('Allowed image types are -> png, jpg, jpeg, gif')
		return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)

def publish(topic, filename):
    p = Producer({'bootstrap.servers': 'kafka1:19091,kafka2:19092,kafka3:19093'})
    p.produce(topic, key=str(uuid4()), value=get_json_str(time.time(), filename), on_delivery=delivery_report)
    p.flush()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
