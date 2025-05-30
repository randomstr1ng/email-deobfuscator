from flask import Flask, render_template, request, redirect, url_for, flash
import requests, os
from bs4 import BeautifulSoup

app = Flask(__name__)
app.secret_key = "replace_this_with_a_random_secret_as_this_is_not_used_anywhere_I_don't_give_a_fuck"

def decrypt_charcode(char_code, start, end, offset):
    char_count = end - start + 1
    shifted = (char_code - start + offset) % char_count
    return chr(start + shifted)

def decrypt_string(value, offset):
    result = ''
    for char in value:
        char_code = ord(char)
        if 0x2B <= char_code <= 0x3A:
            result += decrypt_charcode(char_code, 0x2B, 0x3A, offset)
        elif 0x40 <= char_code <= 0x5A:
            result += decrypt_charcode(char_code, 0x40, 0x5A, offset)
        elif 0x61 <= char_code <= 0x7A:
            result += decrypt_charcode(char_code, 0x61, 0x7A, offset)
        else:
            result += char
    return result

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    url = ""
    if request.method == "POST":
        url = request.form.get("url", "").strip()
        if not url:
            flash("Please enter a URL.", "danger")
        elif not url.startswith("https://www.neuhausen-enzkreis.de"):
            flash("Only URLs from https://www.neuhausen-enzkreis.de are supported.", "danger")
        else:
            try:
                resp = requests.get(url, timeout=10)
                resp.raise_for_status()
                soup = BeautifulSoup(resp.text, "html.parser")
                links = soup.find_all("a", attrs={"data-mailto-token": True, "data-mailto-vector": True})
                decoded_set = set()
                for link in links:
                    token = link.get("data-mailto-token")
                    vector = link.get("data-mailto-vector")
                    try:
                        offset = -int(vector)
                        decoded = decrypt_string(token, offset)
                        if decoded.startswith("mailto:"):
                            decoded = decoded[len("mailto:"):]
                        if decoded not in decoded_set:
                            decoded_set.add(decoded)
                            results.append({
                                "decoded": decoded
                            })
                    except Exception as e:
                        err_msg = f"Error decoding: {e}"
                        if err_msg not in decoded_set:
                            decoded_set.add(err_msg)
                            results.append({
                                "decoded": err_msg
                            })
                if not results:
                    flash("No mailto tokens found on the page.", "info")
            except Exception as e:
                flash(f"Error fetching or parsing URL: {e}", "danger")
    return render_template("index.html", results=results, url=url)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port, debug=False)
