# test_15.py
from Backend.Model import FirstLayerDMM

TESTS = [
    ("Open WhatsApp", "open whatsapp"),
    ("How many followers on Instagram?", "instagram follower count"),
    ("How many following on Instagram?", "instagram following count"),
    ("Show me my Instagram followers", "instagram followers list"),
    ("Show me my Instagram following", "instagram following list"),
    ("Play Shape of You", "play shape of you"),
    ("Google search Python tutorial", "google search python tutorial"),
    ("Write application for leave", "content application for leave"),
    ("Mute karo", "system mute"),
    ("Time kya hua?", "system time"),
    ("Image to PDF banao", "image to pdf"),
    ("Open YouTube", "open youtube"),
    ("Open ChatGPT", "open chatgpt"),
    ("Close Notepad", "close notepad"),
    ("YouTube search lofi music", "youtube search lofi music"),
]

pass_count = 0
fail_count = 0

for query, expected in TESTS:
    result = FirstLayerDMM(query)
    got = result[0] if result else "EMPTY"
    status = "✅" if expected in got else "❌"
    if expected in got:
        pass_count += 1
    else:
        fail_count += 1
    print(f"{status} {query!r:45}")
    print(f"   Expected: {expected}")
    print(f"   Got:      {got}")
    print()

print(f"\n{'='*60}")
print(f"RESULT: {pass_count} pass, {fail_count} fail")
print(f"{'='*60}")