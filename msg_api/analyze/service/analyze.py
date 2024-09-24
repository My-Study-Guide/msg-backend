import random
from typing import List

# import requests
# from bs4 import BeautifulSoup

from msg_api.analyze.model.analyze import MsgAnalyzePostResponse, UrlInfo


class MsgAnalyzeService:
    def __init__(self):
        pass

    def analyze_urls(self, topic: str, urls: List) -> MsgAnalyzePostResponse:
        results: List[UrlInfo] = []
        for url in urls:
            try:
                # response = requests.get(url)
                # soup = BeautifulSoup(response.text, 'html.parser')
                # page_text = soup.get_text()
                results.append(
                    UrlInfo(
                        url=url,
                        status="success",
                        score=round(random.uniform(0, 1), 2),
                        summary="test",
                    )
                )
            except Exception:
                results.append(
                    UrlInfo(url=url, status="fail", score=0, summary="test")
                )
        return MsgAnalyzePostResponse(results=results)
