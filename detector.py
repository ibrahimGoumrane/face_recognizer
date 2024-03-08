from pathlib import Path
import face_recognition
import pickle
from collections import Counter
import numpy as np

DEFAULT_ENCODINGS_PATH = Path("output")
Path('training').mkdir(exist_ok=True)
Path("output").mkdir(exist_ok=True)
Path("validation").mkdir(exist_ok=True)


def save_encodings(name_encodings: dict, encodings_location: Path = DEFAULT_ENCODINGS_PATH) -> None:
    """Save the encoding in the format of a pickle file."""
    if not name_encodings['names']:
        return

    with encodings_location.joinpath('{}'.format(name_encodings['names'][0])).open(mode="wb") as f:
        pickle.dump({'names': name_encodings['names'], 'encodings': name_encodings['encodings']}, f)


def handle_encodings(name: str,show_file_error=True) -> dict:
    """Function used to optimize saving in case we want to upgrade our model."""
    old_encodings = load_encoded_faces(name,show_file_error==True)
    if old_encodings:  # If there are no encodings saved yet
        return old_encodings
    return {'names': [], 'encodings': []}


def load_encoded_faces(name,show_file_error=True, encodings_location: Path = DEFAULT_ENCODINGS_PATH) -> dict:
    try:
        with encodings_location.joinpath('{}'.format(name)).open(mode="rb") as f:
            loaded_encodings = pickle.load(f)
    except OSError as e:
        if show_file_error :
             print(f"An IOError occurred: {e}")
        return {'names': [], 'encodings': []}
    return loaded_encodings


def encode_known_faces(model: str = "CNN", encodings_location: Path = DEFAULT_ENCODINGS_PATH) -> None:
    for filepath in Path("training").glob("elon_musk/*"):
        name = filepath.parent.name+'_encodings.pkl'
        image = face_recognition.load_image_file(filepath)
        face_encodings_old = handle_encodings(name,show_file_error=False)
        face_locations = face_recognition.face_locations(image, model=model)
        face_encodings = face_recognition.face_encodings(image, face_locations)

        if face_encodings_old['encodings']:
            for encoding in face_encodings:
                if any(np.array_equal(encoding, old_encoding) for old_encoding in face_encodings_old['encodings']):
                    continue  # Do not overwrite existing encoding
                face_encodings_old['encodings'].append(encoding)

        # Saving the encodings
        name_encodings = {"names": [name], "encodings": face_encodings}
        save_encodings(name_encodings, encodings_location)



def recognize_faces(
    image_location: str,
    model: str = "CNN",
    encodings_location: Path = DEFAULT_ENCODINGS_PATH,
) -> None:
    """The function will show on screen who is in the img."""
    input_image = face_recognition.load_image_file(image_location)
    input_face_locations = face_recognition.face_locations(
        input_image, model=model
    )
    input_face_encodings = face_recognition.face_encodings(
        input_image, input_face_locations
    )
    searched_name=''
    for files in encodings_location.glob('*_encodings.pkl'):
        file_name=files.stem+'.pkl'
        loaded_encodings = load_encoded_faces(file_name)
        if not loaded_encodings['encodings']:
            return  # Skip if there are no encodings

        for bounding_box, unknown_encoding in zip(input_face_locations, input_face_encodings):
            # We use this block to define the user name
            searched_name = _recognize_face(unknown_encoding, loaded_encodings)
            if searched_name:
                print(searched_name, bounding_box)
                break
            


def _recognize_face(unknown_encoding, reference_encoding):
    """Function returns the match between the encoding img and the reference imgs."""
    # Test the correspondence between the images
    boolean_matches = face_recognition.compare_faces(reference_encoding['encodings'], unknown_encoding)
    votes = Counter(
        name
        for match, name in zip(boolean_matches, reference_encoding["names"])
        if match
    )  # Count the number of correspondence

    if votes:
        name:str=votes.most_common(1)[0][0]
        ele_len=name.rfind('_encodings.pkl')
        # Return the name of the encoding that had a higher count
        return name[:ele_len]



# training_path = Path("validation/ben_afflek_1.jpg")
# training_path = Path("validation/ben_afflek_2.jpg")
training_path = Path("validation/elon-musk-celeb-fan-boys.jpg")
recognize_faces(training_path.absolute())
