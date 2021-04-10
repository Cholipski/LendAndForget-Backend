def user_directory_path(instance, filename):
    return "images/user_{id}/{file}".format(id=instance.lenderID.id, file=filename)