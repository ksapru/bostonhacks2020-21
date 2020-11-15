import os
from werkzeug.utils import secure_filename
from app.dbManager import DbManager

from config import Constants


class ImageHandle:
    def __init__(self):
        pass

    @staticmethod
    def allowed_image(filename):
        if "." not in filename:
            return False

        ext = filename.rsplit(".", 1)[1]

        if ext.lower() in Constants.ALLOWED_EXTENSIONS:
            return ext
        else:
            return False

    @staticmethod
    def save_img(image, researchId=1, username='admin'):
        con = DbManager()
        if image.filename == "":
            print("No filename")
            return

        fileExt = ImageHandle.allowed_image(image.filename)
        if fileExt:
            uploadname = secure_filename(image.filename)
            table = 'Images'
            pk = 'ImageId'
            imid = con.last_entry(table, pk) + 1
            # imid = 2
            filename = str(imid) + '.' + str(fileExt)

            os.chdir(Constants.UPLOAD_FOLDER)
            image.save(os.path.join(Constants.UPLOAD_FOLDER, filename))
            os.chdir(Constants.BASEDIR)

            vals = [imid, username, filename, researchId, 'taken at:22-3-2020']

            con.insert(table, Constants.IMAGECOLS, vals)

            print("Image saved")

        else:
            print("That file extension is not allowed")

    @staticmethod
    def getPics(researchid=1, username='admin'):
        con = DbManager()
        data = con.select('Images', cols=Constants.IMAGECOLS)
        files = []
        print(data)
        for vals in data:
            file = vals[2]
            id = vals[0]
            if id == researchid:
                files.append(file)

        return files
