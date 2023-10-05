import face_recognition
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/compare_faces', methods=['POST'])
def compare_faces():
    try:
        # Get the input images from the request
        image_a = face_recognition.load_image_file(request.files['image_a'])
        image_b = face_recognition.load_image_file(request.files['image_b'])

        # Encode the faces
        encoding_a = face_recognition.face_encodings(image_a)[0]
        encoding_b = face_recognition.face_encodings(image_b)[0]

        # Compare the face encodings
        match_score = float(face_recognition.compare_faces([encoding_a], encoding_b)[0])

        # Respond with the matching score in JSON format
        response_data = {'match_score': match_score}
        return jsonify(response_data)
    except Exception as e:
        # Handle all exceptions with a generic error message
        error_message = f'No Match' # {str(e)}
        return jsonify({'error': error_message}), 500  # Return a 500 Internal Server Error status code

if __name__ == '__main__':
    app.run(debug=True,port=8502)
