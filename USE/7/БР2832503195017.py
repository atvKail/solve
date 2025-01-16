resolution = 3840 * 2160
bytes_per_pixel = 3  # 24 бита = 3 байта
card_capacity_gb = 16
photos_total = 3742

size_per_photo = resolution * bytes_per_pixel
card_capacity_bytes = card_capacity_gb * 1024**3
photos_per_card = card_capacity_bytes // size_per_photo

photos_last_card = photos_total % photos_per_card

print(photos_last_card)
