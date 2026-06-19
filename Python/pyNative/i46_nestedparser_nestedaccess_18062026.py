import json

user_json = '{"id": 1, "profile": {"nama": "Alice", "settings": {"tema": "terang"}}}'

# ubah string ke dictionary
#
data = json.loads(user_json)

# akses nested key dan update

data["profile"]["settings"]["tema"] = "gelap"

#  konversi kembali ke JSON string dengan cetakan yang cuantikkk
updated_json = json.dumps(data, indent=4)

print("Updated profile Setting:")
print(updated_json)
