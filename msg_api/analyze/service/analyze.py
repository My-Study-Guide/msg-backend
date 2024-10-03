import json
from typing import List

import requests
from bs4 import BeautifulSoup

from msg_api import config
from msg_api.analyze.model.analyze import MsgAnalyzePostResponse, UrlInfo


class MsgAnalyzeService:
    def __init__(self):
        pass

    def analyze_urls(self, topic: str, urls: List) -> MsgAnalyzePostResponse:
        results: List[UrlInfo] = []
        for url in urls:
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.text, "html.parser")
                page_text = soup.get_text()
                model_url = config.MODEL_URL
                data = {"text": page_text, "topics": topic}
                max_retries = 3
                for i in range(max_retries):
                    response = requests.post(model_url, json=data)
                    if response.status_code == 200:
                        text = json.loads(response.text)
                        print(text["score"])
                        results.append(
                            UrlInfo(
                                url=url,
                                status="success",
                                score=round(float(text["score"]) / 100, 2),
                                summary=text["reason"],
                            )
                        )
                        break
            except Exception:
                results.append(
                    UrlInfo(url=url, status="fail", score=0, summary="test")
                )
        return MsgAnalyzePostResponse(results=results)
