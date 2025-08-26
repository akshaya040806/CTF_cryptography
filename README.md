Playful implementation of the Playfair Cipher with an extra puzzle layer:

Instead of just encoding messages normally, it maps letters into a Left (L) / Right (R) sequence based on odd/even index positions.
Also, hints are there along the way to help figure out the pattern.

This project adds a modern, humorous twist:

Odd-index letters → R (Right)
Even-index letters → L (Left)

A sarcastic narrator drops hints like:

“Oh sure, go Left when things are even. Because being odd is apparently soooo Right.”

Features

✅ Classical SHA256 decryption
✅ Then the playfair cipher
✅ LR sequence generator (odd = R, even = L)
✅ Then the flag yay

Usage

Hash - crack the cheese name.

Use: https://www.dcode.fr/sha256-hash

Cheese name - encode it using Playfair encryption.

Use: https://encryptdecrypt.tools/tools/ciphers/playfair.php

Player must supply the correct ciphertext.
Asks for L/R sequence (based on odd/even alphabet positions).
If right - flag is revealed.
