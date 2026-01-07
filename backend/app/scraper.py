import requests
from bs4 import BeautifulSoup


def scrape_wikipedia(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    response = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    title_tag = soup.find("h1")
    title = title_tag.text if title_tag else "Unknown Title"

    paragraphs = soup.find_all("p")

    summary = ""
    content = ""

    for p in paragraphs:
        text = p.get_text().strip()
        if text:
            summary += text + " "
            content += text + " "
        if len(summary) > 500:
            break

    return {
        "title": title,
        "summary": summary.strip(),
        "content": content.strip()
    }
