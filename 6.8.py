import random
import string

char = string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation

def check_in_str(word, str_):
    if word in str_:
        return True
    else:
        return False
def pass_gen():
    password_li = random.sample(char,10)
    for i in password_li:
        if check_in_str(i, string.ascii_lowercase) or check_in_str(i, string.digits) or check_in_str(i, string.ascii_uppercase) or check_in_str(i, string.punctuation):
            return password_li
        else:
            pass
        
print(pass_gen())