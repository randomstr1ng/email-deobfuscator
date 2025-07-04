# E-Mail deobfuscator für die Webseite der Gemeinde Neuhausen-Enzkreis

The app is available at [https://email-deobfuscator.str1ng.org/](https://email-deobfuscator.str1ng.org/).

A Flask web application to extract and decrypt obfuscated e-mail addresses from pages on https://www.neuhausen-enzkreis.de.

## Features

- Modern, mobile-friendly UI for submitting a URL.
- Only supports URLs from https://www.neuhausen-enzkreis.de.
- Extracts all `data-mailto-token` and `data-mailto-vector` attributes from the page.
- Decrypts and displays all unique e-mail addresses, with a copy-to-clipboard button.
- Docker support and GitHub Actions workflow for automated container builds and publishing to GHCR.

## Quickstart

### Local Development

1. **Install dependencies:**
    ```bash
    cd app
    pip install -r requirements.txt
    ```

2. **Run the app:**
    ```bash
    python app.py
    ```

3. Open your browser to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and submit a supported URL.

### Docker

1. **Build the Docker image:**
    ```bash
    docker build -t email-deobfuscator:latest .
    ```

2. **Run the container:**
    ```bash
    docker run -p 8000:8000 email-deobfuscator:latest
    ```

3. Visit [http://localhost:8000/](http://localhost:8000/).

### GitHub Actions & GHCR

- On every push to `main`, the Docker image is built and pushed to GitHub Container Registry (GHCR) as `ghcr.io/<owner>/<repo>:latest`.
- See `.github/workflows/docker-ghcr.yml` for details.

## Project Structure

- `app/` - Flask app source code and requirements.
- `app/templates/` - HTML templates.
- `app/static/` - Static files (e.g., favicon).
- `Dockerfile` - Container build instructions.
- `.github/workflows/` - GitHub Actions workflow for Docker/GHCR.

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0).
See the [LICENSE](LICENSE) file for details.

## Attribution

If you use or modify this project, you **must** provide attribution to the original author as required by the GPL-3.0 license.
All copies and substantial portions of the project must retain the copyright notice and this permission notice.
