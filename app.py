from fastapi import FastAPI, UploadFile, File, HTTPException
import face_recognition
from typing import Dict
import io

app = FastAPI()

@app.post("/compare_faces", response_model=Dict[str, float])
async def compare_faces(image_a: UploadFile, image_b: UploadFile):
    try:
        # Load and encode the faces
        image_a_data = await image_a.read()
        image_b_data = await image_b.read()

        image_a_io = io.BytesIO(image_a_data)
        image_b_io = io.BytesIO(image_b_data)

        image_a_np = face_recognition.load_image_file(image_a_io)
        image_b_np = face_recognition.load_image_file(image_b_io)

        encoding_a = face_recognition.face_encodings(image_a_np)[0]
        encoding_b = face_recognition.face_encodings(image_b_np)[0]

        # Compare the face encodings
        match_score = float(face_recognition.compare_faces([encoding_a], encoding_b)[0])

        return {"match_score": match_score}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"error: No Match") #{str(e)}"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8502)
