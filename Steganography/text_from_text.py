
import Steganography.text_cryption as tc

def binaryToDecimal(binary):
  b = int(binary)
  decimal = 0
  p=0
  while b != 0:
    decimal = decimal + (b%10)*pow(2,p)
    b = int(b/10)
    p = p + 1
  return(decimal)

class TextSteganography:
  def __init__(self, cover_txtfile):
    self.cover_txtfile = str(cover_txtfile)
    c_file = open(self.cover_txtfile,'r')
    self.cover_text = c_file.read()
    c_file.close()
    self.text_crypto = tc.TextCryptography()

  def decodeFromText(self):
    txt_msg = []
    temp_msg = []
    c_iter = iter(self.cover_text)
    for i in range(len(self.cover_text)):
      k = next(c_iter)
      if ord(k) == 32:
          k = next(c_iter)
          if   ord(k) == 32:
            temp_msg.append('0')
          elif k.isupper() and k.isalpha():
            temp_msg.append('1')
          elif k.isalpha() and k.islower and ord(k) != 46:
            break
      elif ord(k) == 46:
          next(c_iter)
      if len(temp_msg) == 7:
        txt_msg.append(chr(binaryToDecimal("".join(temp_msg))))
        temp_msg = []
    return self.text_crypto.decryptText("".join(txt_msg))