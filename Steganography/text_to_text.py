
import Steganography.text_cryption as tc


class EncodeTextSteg:
    def __init__(self,cover_txtfile):
        self.cover_txtfile = cover_txtfile
        c_file = open(str(self.cover_txtfile)[5:-2],'r')
        self.cover_text = c_file.read()
        c_file.close()
        self.text_crypto = tc.TextCryptography()

    def encodeIntoText(self,msg_text):
        self.msg_text = self.text_crypto.encryptText(msg_text)
        index = -1
        l = [format(ord(i), 'b') for i in self.msg_text]
        for i in range(len(l)):
            if len(l[i]) == 6:
                ll = list(l[i])
                ll.insert(0,'0')
                l[i] = ''.join(ll)
        txt_b = ''.join(l)
        l = list(self.cover_text)
        iter_ctext = iter(self.cover_text)
        for i in txt_b:
            for j in range(len(self.cover_text)):
                k = next(iter_ctext)
                index = index + 1
                if ord(k) == 32:
                    k = next(iter_ctext)
                    index = index + 1
                    if i == '0':
                        l.insert(index,' ')
                        index = index + 1
                    elif k.isalpha() and i == '1':
                        l[index] = l[index].upper()
                    break
                elif ord(k) == 46 and (not k.isalpha()):
                    next(iter_ctext)
                    index = index + 1
                else:
                    continue
        self.cover_text = "".join(l)
        c_file = open('ecover.txt','w')
        c_file.write(str(self.cover_text))
        c_file.close()