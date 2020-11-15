from ultils import Utils

class Constants:
    BASEDIR = Utils.get_home_dir()
    UPLOAD_FOLDER = BASEDIR + '/app/static/img/uploads/'
    STATICDIR = 'static/img/uploads/'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

    USERCOLS = ['Username', 'Email', 'Password', 'Images']
    RESEARCHCOLS = ['ResearchID', 'ResearchTitle', 'ResearchDescription', 'Categories']
    IMAGECOLS = ['ImageId','Username','ImageName','ResearchId', 'MetaData']