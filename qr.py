import segno
from urllib.request import urlopen

#@November_monkey -> tg
qr_code = segno.make_qr("t.me/November_monkey")
qr_code.save(
    "basic_qr_code.png",
    scale = 5
)

#gif
qrcode = segno.make_qr("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
url = urlopen("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMzN1ZWRtNGF3eHBudHdzc3ZlZXR4MWl3bHNvY3NycDlmZWU3MmV3aiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Vuw9m5wXviFIQ/giphy.gif")
qrcode.to_artistic(
    background = url,
    target = "animated_qrcode.gif",
    scale = 5,
)