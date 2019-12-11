import requests
from retrying import retry
import json


class DoubanTv:

    def __init__(self):
        self.start_url_list = [
            "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?os=ios&for_mobile=1&start={}&count=18&loc_id=108288",
            "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_english_hot/items?os=ios&for_mobile=1&start={}&count=18&loc_id=108288"
        ]
        # self.headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}
        self.headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}
    @retry(stop_max_attempt_number=3)
    def _parse_url(self,url):
        print(url)
        response = requests.get(url,headers=self.headers,timeout=5)
        assert response.status_code == 200
        return response.content.decode()
    def parse_url(self,url):
        try:
            html_str = self.parse_url(url)
        except Exception as e:
            print(e)
            html_str = None
        return html_str

    def get_content_list(self, html_str):  # 提取数据
        dict_response = json.loads(html_str)
        content_list = dict_response["subject_collection_items"]
        total = dict_response["total"]
        return content_list, total

    def save_content_list(self, content_list):  # 数据的保存
        with open("douban_tv.txt", "a") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False, indent=2))
                f.write("\n")
        print("保存成功")
    def run(self):
        # 1. url_list,headers
        for url in self.start_url_list:
            print(url)
            num = 0
            total = 100
            while num <= total+18:
                url = url.format(num)
                # 2. 发送请求，获取响应
                html_str = self._parse_url(url)
                # 3. 提取数据
                content_list,total = self.get_content_list(html_str)
                # 4. 保存
                self.save_content_list(content_list)
                num += 18

if __name__ == '__main__':
    dou = DoubanTv()
    dou.run()