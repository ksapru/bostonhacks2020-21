from ultils import Utils

class Constants:
    BASEDIR = Utils.get_home_dir()
    UPLOAD_FOLDER = BASEDIR + '/app/static/img/uploads/'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

    USERCOLS = ['Username', 'Email', 'Password']
    RESEARCHCOLS = ['ResearchID', 'ResearchTitle', 'ResearchDescription', 'Categories']
    IMAGECOLS = ['ImageId','Username','ImageName','ResearchId', 'MetaData']