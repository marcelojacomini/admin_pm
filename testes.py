import hashlib


def md5_password_converter(password):
    # encode the password string to bytes
    password_bytes = password.encode('utf-8')
    # create the hash object
    m = hashlib.md5(password_bytes)
    # return the converted password
    return m.hexdigest()


print(md5_password_converter('105Mai2078'))
