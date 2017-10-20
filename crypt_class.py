from cryptography.fernet import Fernet

def crypt(s):
    key = Fernet.generate_key()
    model = Fernet(key)
    bs = bytes(s, 'utf-8')
    encrypted_text = model.encrypt(bs)
    return(str(encrypted_text, 'utf-8')+'#(0-0)#'+str(key, 'utf-8'))

def dcrypt(s):
    s = [bytes(x,'utf-8') for x in s.split('#(0-0)#')]
    model = Fernet(s[1])
    decrypted_text = model.decrypt(s[0])
    return str(decrypted_text, 'utf-8')