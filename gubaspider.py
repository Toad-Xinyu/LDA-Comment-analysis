import requests
import re
import pandas as pd
import os

class GuBaSpdier():
    def get_html(self, page):
        cookies = {
            'qgqp_b_id': '9464b75642fe28c71ab93d780c3ece20',
            'websitepoptg_api_time': '1730045187629',
            'st_si': '49551077203344',
            'st_pvi': '05987046565435',
            'st_sp': '2024-10-28%2000%3A06%3A27',
            'st_inirUrl': 'https%3A%2F%2Fwww.baidu.com%2Flink',
            'st_sn': '4',
            'st_psi': '20241028000927259-117001356556-3947260030',
            'st_asi': '20241028000927259-117001356556-3947260030-gb.webggb.dbqy-1',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            # 'Cookie': 'qgqp_b_id=9464b75642fe28c71ab93d780c3ece20; websitepoptg_api_time=1730045187629; st_si=49551077203344; st_pvi=05987046565435; st_sp=2024-10-28%2000%3A06%3A27; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=4; st_psi=20241028000927259-117001356556-3947260030; st_asi=20241028000927259-117001356556-3947260030-gb.webggb.dbqy-1',
            'Referer': 'https://guba.eastmoney.com/list,zssh000001_2.html',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        response = requests.get('https://guba.eastmoney.com/list,zssh000001_{}.html'.format(page), cookies=cookies, headers=headers)
        return response.text


    def parse_data(self, html):
        pattern = r'"post_title":"(.*?)"'
        result = re.findall(pattern,html)
        return result


    def sava_data(self, result):
        df = pd.DataFrame(result)
        file_path = 'result.csv'
        file_exists = os.path.isfile(file_path)
        if not file_exists or os.stat(file_path).st_size == 0:
            header = ['content']
            mode = 'w'
        else:
            header = False
            mode = 'a'
        df.to_csv(file_path, index=False, header=header, mode=mode)



    def run(self):
        for page in range(1, 21):
            print('正在爬取第{}页'.format(str(page)))
            html = self.get_html(page)
            result = self.parse_data(html)
            self.sava_data(result)


if __name__ == '__main__':
    gb = GuBaSpdier()
    gb.run()
