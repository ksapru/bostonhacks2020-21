from config import Constants

class ImageHandle:
    def __init__(self):
        pass

    @staticmethod
    def allowed_image(filename):

        if not "." in filename:
            return False

        ext = filename.rsplit(".", 1)[1]

        if ext.lower() in Constants.ALLOWED_EXTENSIONS:
            return True
        else:
            return False