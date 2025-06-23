from cryptography.fernet import Fernet
import re
import requests
import urllib.parse

# Provided Key and Encrypted Text
key = b"o8ufQJheHx5CcqrRDwpy3EMsgO2LYuE--kiGcqy24k0="  # Key should be in bytes
encrypted_text = "gAAAAABnPrBM3jvc5hBQDldxwdT9x3NXFzDR_3bpN4rCo3EtZlyajdF1f_2omRU5_k9yh-uv8LFOTFnKmp792xY_IzE_n2eyzC25k0ZZfscGXRrNdVM9e7jGB61Rv6sl7guLPsO8PhKIiD13X6R3xVQPetkoF4oT771b0eKJ9zV_hal66AgsPuDLv0Rzks2azBmAwoZotwbR_2LVkreCLgnc2uf4ul7hj514l2OGuYfxu1oc8GbwVLxRbK4_5ZogI4HcuAJfw6Al0WhHp8FRwQZNDTFGFluPDeAND-EKJswLAjyRrSRGXvLIEeM5ApTc4JeA9-3_23pmFx5XHb1Zx8ii011jvwKEqgSb4l2MaZKW3Uo-3-ruHBKJjBKeT8WbOFNbHOhqP74j3-nwbjbBd0JSRb9jLBBDQEK0zDiwk998TJQhWtFgUhAQ9RTZmMznz9L_6RyUlaqacUn8IrHDjdGoISNNOEjSylrF_gxp_6pEnDor--0zkftYpMwG6UEpmF-JtgyUqvlTnofbEIRbkrDbUo3rfOwq3JlpW8ukN_fYxeGNiv9nTnuWIMqZjhrNT3Hj6azeRH73l-hBNfhd5qiz9tq3IaA3MBBTOJFkEigwwliv8m6__1KXAbLZO8gRuoLtmM0KMTL6OJK3QAizYNCUHdC-TRSPWaleUjSK-icyuUvZn9q0LcxpWK08ICFqXYomXoDra1pcHPW8wQvbJgJty-r9OixBLyNxMtPPHmHmQGjs1EKvp8Q7AbpWgZrqYw2-lA3BYXepCdqnOM3f25RyTab7tfXgiSzJqFv2la1yOLd1nE-EqIJN_6_HzCduTSC3bmvJyOM7Aou42DIFrnKbHUO7CLCD-PFswM3htfi8GWii11UVi4d0zm8rlFkxKG7IZVXzalTHy-AaZVzhbse1wtgrq-znJw=="

# Step 1: Decrypt the encrypted text
fernet = Fernet(key)
decrypted_text = fernet.decrypt(encrypted_text.encode()).decode()

# Step 2: Replace Unicode representations of emojis with actual emojis
def replace_unicode_with_emojis(text):
    emoji_pattern = r'\\U[0-9A-Fa-f]{8}'
    
    def unicode_to_emoji(match):
        return chr(int(match.group(0)[2:], 16))

    return re.sub(emoji_pattern, unicode_to_emoji, text)

decrypted_text_with_emojis = replace_unicode_with_emojis(decrypted_text)

# Step 3: URL encode the answer
encoded_answer = urllib.parse.quote(decrypted_text_with_emojis)

# Step 4: Submit the answer (Here you will prepare the submission URL)
submission_url = f"https://quest.squadcast.tech/api/1OX21CS085/submit/emoji?answer={encoded_answer}&extension=py"

# To submit the code, you would post it (but for now, let's just print the submission URL)
print(f"Submission URL: {submission_url}")

# If you want to post the code:
code = '''from cryptography.fernet import Fernet
import re
import requests
import urllib.parse

key = b"o8ufQJheHx5CcqrRDwpy3EMsgO2LYuE--kiGcqy24k0="
encrypted_text = "gAAAAABnPrBM3jvc5hBQDldxwdT9x3NXFzDR_3bpN4rCo3EtZlyajdF1f_2omRU5_k9yh-uv8LFOTFnKmp792xY_IzE_n2eyzC25k0ZZfscGXRrNdVM9e7jGB61Rv6sl7guLPsO8PhKIiD13X6R3xVQPetkoF4oT771b0eKJ9zV_hal66AgsPuDLv0Rzks2azBmAwoZotwbR_2LVkreCLgnc2uf4ul7hj514l2OGuYfxu1oc8GbwVLxRbK4_5ZogI4HcuAJfw6Al0WhHp8FRwQZNDTFGFluPDeAND-EKJswLAjyRrSRGXvLIEeM5ApTc4JeA9-3_23pmFx5XHb1Zx8ii011jvwKEqgSb4l2MaZKW3Uo-3-ruHBKJjBKeT8WbOFNbHOhqP74j3-nwbjbBd0JSRb9jLBBDQEK0zDiwk998TJQhWtFgUhAQ9RTZmMznz9L_6RyUlaqacUn8IrHDjdGoISNNOEjSylrF_gxp_6pEnDor--0zkftYpMwG6UEpmF-JtgyUqvlTnofbEIRbkrDbUo3rfOwq3JlpW8ukN_fYxeGNiv9nTnuWIMqZjhrNT3Hj6azeRH73l-hBNfhd5qiz9tq3IaA3MBBTOJFkEigwwliv8m6__1KXAbLZO8gRuoLtmM0KMTL6OJK3QAizYNCUHdC-TRSPWaleUjSK-icyuUvZn9q0LcxpWK08ICFqXYomXoDra1pcHPW8wQvbJgJty-r9OixBLyNxMtPPHmHmQGjs1EKvp8Q7AbpWgZrqYw2-lA3BYXepCdqnOM3f25RyTab7tfXgiSzJqFv2la1yOLd1nE-EqIJN_6_HzCduTSC3bmvJyOM7Aou42DIFrnKbHUO7CLCD-PFswM3htfi8GWii11UVi4d0zm8rlFkxKG7IZVXzalTHy-AaZVzhbse1wtgrq-znJw=="

fernet = Fernet(key)
decrypted_text = fernet.decrypt(encrypted_text.encode()).decode()

def replace_unicode_with_emojis(text):
    emoji_pattern = r'\\U[0-9A-Fa-f]{8}'
    def unicode_to_emoji(match):
        return chr(int(match.group(0)[2:], 16))

    return re.sub(emoji_pattern, unicode_to_emoji, text)

decrypted_text_with_emojis = replace_unicode_with_emojis(decrypted_text)

encoded_answer = urllib.parse.quote(decrypted_text_with_emojis)

submission_url = f"https://quest.squadcast.tech/api/1OX21CS085/submit/emoji?answer={encoded_answer}&extension=py"
'''

# Post the code (if needed)
response = requests.post(submission_url, data={"code": code})
print(f"Response: {response.text}")
