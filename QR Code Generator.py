import qrcode

# লিঙ্কগুলো একটি লিস্টে রাখুন
links = [
    "https://www.linkedin.com/in/akibahmedtahcin/",
    "https://www.facebook.com/akib.ahmed.tahcin.2024",
    "https://www.instagram.com/akibahmedtahcin/"
]

# লুপ ব্যবহার করে প্রতিটি লিঙ্কের জন্য আলাদা QR কোড তৈরি করুন
for i, url in enumerate(links):
    img = qrcode.make(url)
    filename = f"qr_code_{i+1}.png" # ফাইলের নাম হবে qr_code_1.png, qr_code_2.png ইত্যাদি
    img.save(filename)
    print(f"QR code generated successfully for: {url} -> Saved as {filename}")