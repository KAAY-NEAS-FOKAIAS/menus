import qrcode

# URL of your GitHub Pages site
url = "https://jimkiromitis.github.io/kaay_fokaia.github.io/"

# Create QR code
qr = qrcode.make(url)

# Save to file
qr.save("kaay_qr.png")

print("✅ QR code saved as 'kaay_qr.png'")