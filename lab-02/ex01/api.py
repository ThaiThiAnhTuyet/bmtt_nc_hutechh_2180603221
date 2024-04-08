from flask import Flask, request, jsonify
from cipher.ceasar import CeasarCipher
app = Flask(_name_)

#CAESAR CIPHER ALGORITHM 
ceasar_cipher = CeasarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.cipher
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypt_text = ceasar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.cipher
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypt_text = ceasar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypt_text})

#main function 
if _name_== "_main_":
    app.run(host="0.0.0.0", port=5000, debug=True)