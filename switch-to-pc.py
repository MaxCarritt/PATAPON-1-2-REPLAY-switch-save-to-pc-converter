import json
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# === Crypto parameters (verified) ===
KEY = b"H2AYuFL!VGW~tQU2"      # 16 bytes
IV  = b"Q4TmjuN,9sFcZjkJ"      # 16 bytes
BLOCK = 16

# === Paths ===
SWITCH_SAV = r"PATH-to-your-switch-save-here!!"
OUT_PC_SAV = r"patapon 1+2 replay_savedata_p1.sav"

# --- Load Switch JSON ---
with open(SWITCH_SAV, "r", encoding="utf-8") as f:
    switch_json = json.load(f)

# --- Minify JSON exactly as PC expects ---
plain = json.dumps(
    switch_json,
    separators=(",", ":"),
    ensure_ascii=False
).encode("utf-8")

# --- Encrypt ---
cipher = AES.new(KEY, AES.MODE_CBC, IV)
encrypted = cipher.encrypt(pad(plain, BLOCK))

# --- Base64 wrap ---
pc_save = base64.b64encode(encrypted)

# --- Write PC save ---
with open(OUT_PC_SAV, "wb") as f:
    f.write(pc_save)

print("PC save written:", OUT_PC_SAV)
