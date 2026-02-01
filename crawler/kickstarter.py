# https://www.kickstarter.com/

import cloudscraper
from bs4 import BeautifulSoup
import time
import random
import json
import traceback
from typing import TypedDict
from utils.translator import translate_text_to_chinese


def _get_html_content(url):
    # 1. 使用更逼真的 Headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.kickstarter.com",
        "DNT": "1",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",  # 如果是从站内跳转，这个值更合适
        "Cookie": "last_page=https%3A%2F%2Fwww.kickstarter.com%2F;lang=zh",
    }

    # 如果需要使用代理，在这里配置
    proxies = {"https": "http://127.0.0.1:7890"}

    # cloudscraper 也可以配置浏览器特性，让它更像
    scraper = cloudscraper.create_scraper(
        browser={"browser": "chrome", "platform": "windows", "mobile": False},
        auto_refresh_on_403=False,
    )

    try:
        # 增加随机延迟
        sleep_time = random.uniform(2, 5)
        print(f"等待 {sleep_time:.2f} 秒...")
        time.sleep(sleep_time)

        response = scraper.get(url, headers=headers, proxies=proxies)
        response.raise_for_status()  # 如果请求失败 (例如 404, 500)，会抛出异常
        html_content = response.text
        return html_content
    except Exception as e:
        raise Exception(f"爬取或解析{url}过程中发生错误: {traceback.format_exc()}")


class SubCategory(TypedDict):
    id: str
    name: str
    main_id: str
    main_name: str


def get_kickstarter_sub_categories():
    # url = "https://www.kickstarter.com"
    # html_content = _get_html_content(url)
    # soup = BeautifulSoup(html_content, "lxml")
    # category_nav_div = soup.find("div", id="global-header")
    # if not category_nav_div:
    #     raise Exception(f"未找到id为'global-header'的div标签")

    # sub_categories_str = category_nav_div.get('data-subcategories')
    # if not sub_categories_str:
    #     raise Exception(f"未找到id为'global-header'的div标签下的data-subcategories属性")
    # 理论上可以爬取，这里直接人工维护写死
    return [
        SubCategory(id="287", name="陶瓷", main_id="1", main_name="藝術"),
        SubCategory(id="20", name="概念藝術", main_id="1", main_name="藝術"),
        SubCategory(id="21", name="數位藝術", main_id="1", main_name="藝術"),
        SubCategory(id="22", name="繪圖", main_id="1", main_name="藝術"),
        SubCategory(id="288", name="裝置藝術", main_id="1", main_name="藝術"),
        SubCategory(id="54", name="混合媒體", main_id="1", main_name="藝術"),
        SubCategory(id="23", name="繪畫", main_id="1", main_name="藝術"),
        SubCategory(id="24", name="表演藝術", main_id="1", main_name="藝術"),
        SubCategory(id="53", name="公共藝術", main_id="1", main_name="藝術"),
        SubCategory(id="25", name="雕塑", main_id="1", main_name="藝術"),
        SubCategory(id="395", name="社會參與", main_id="1", main_name="藝術"),
        SubCategory(id="289", name="紡織品", main_id="1", main_name="藝術"),
        SubCategory(id="290", name="影片藝術", main_id="1", main_name="藝術"),
        SubCategory(id="249", name="作品選集", main_id="3", main_name="漫畫"),
        SubCategory(id="250", name="漫畫書", main_id="3", main_name="漫畫"),
        SubCategory(id="251", name="活動", main_id="3", main_name="漫畫"),
        SubCategory(id="252", name="圖畫小說", main_id="3", main_name="漫畫"),
        SubCategory(id="253", name="網路漫畫", main_id="3", main_name="漫畫"),
        SubCategory(id="254", name="演出", main_id="6", main_name="舞蹈"),
        SubCategory(id="256", name="太空", main_id="6", main_name="舞蹈"),
        SubCategory(id="257", name="工作坊", main_id="6", main_name="舞蹈"),
        SubCategory(id="258", name="建築", main_id="7", main_name="設計"),
        SubCategory(id="259", name="城市設計", main_id="7", main_name="設計"),
        SubCategory(id="27", name="平面設計", main_id="7", main_name="設計"),
        SubCategory(id="260", name="互動式設計", main_id="7", main_name="設計"),
        SubCategory(id="28", name="產品設計", main_id="7", main_name="設計"),
        SubCategory(id="396", name="玩具", main_id="7", main_name="設計"),
        SubCategory(id="262", name="配件", main_id="9", main_name="時尚"),
        SubCategory(id="263", name="服飾", main_id="9", main_name="時尚"),
        SubCategory(id="264", name="童裝", main_id="9", main_name="時尚"),
        SubCategory(id="265", name="時裝", main_id="9", main_name="時尚"),
        SubCategory(id="266", name="鞋類", main_id="9", main_name="時尚"),
        SubCategory(id="267", name="珠寶", main_id="9", main_name="時尚"),
        SubCategory(id="268", name="寵物時尚", main_id="9", main_name="時尚"),
        SubCategory(id="269", name="Ready-to-wear", main_id="9", main_name="時尚"),
        SubCategory(id="305", name="社區花園", main_id="10", main_name="食品"),
        SubCategory(id="306", name="料理書", main_id="10", main_name="食品"),
        SubCategory(id="307", name="飲料", main_id="10", main_name="食品"),
        SubCategory(id="308", name="活動", main_id="10", main_name="食品"),
        SubCategory(id="310", name="農產品市場", main_id="10", main_name="食品"),
        SubCategory(id="309", name="農場", main_id="10", main_name="食品"),
        SubCategory(id="311", name="美食車", main_id="10", main_name="食品"),
        SubCategory(id="312", name="餐廳", main_id="10", main_name="食品"),
        SubCategory(id="313", name="少量生產", main_id="10", main_name="食品"),
        SubCategory(id="314", name="太空", main_id="10", main_name="食品"),
        SubCategory(id="315", name="素食", main_id="10", main_name="食品"),
        SubCategory(id="291", name="動作", main_id="11", main_name="影片"),
        SubCategory(id="29", name="動畫", main_id="11", main_name="影片"),
        SubCategory(id="292", name="喜劇", main_id="11", main_name="影片"),
        SubCategory(id="30", name="紀錄片", main_id="11", main_name="影片"),
        SubCategory(id="293", name="話劇", main_id="11", main_name="影片"),
        SubCategory(id="294", name="實驗性", main_id="11", main_name="影片"),
        SubCategory(id="330", name="家庭", main_id="11", main_name="影片"),
        SubCategory(id="296", name="奇幻", main_id="11", main_name="影片"),
        SubCategory(id="295", name="節慶", main_id="11", main_name="影片"),
        SubCategory(id="297", name="恐怖", main_id="11", main_name="影片"),
        SubCategory(id="298", name="電影院", main_id="11", main_name="影片"),
        SubCategory(id="299", name="MV", main_id="11", main_name="影片"),
        SubCategory(id="31", name="敘事電影", main_id="11", main_name="影片"),
        SubCategory(id="300", name="浪漫", main_id="11", main_name="影片"),
        SubCategory(id="301", name="科幻", main_id="11", main_name="影片"),
        SubCategory(id="32", name="短片", main_id="11", main_name="影片"),
        SubCategory(id="303", name="電視", main_id="11", main_name="影片"),
        SubCategory(id="302", name="驚悚", main_id="11", main_name="影片"),
        SubCategory(id="33", name="網路劇集", main_id="11", main_name="影片"),
        SubCategory(id="270", name="遊戲相關硬體", main_id="12", main_name="遊戲"),
        SubCategory(id="271", name="實況遊戲", main_id="12", main_name="遊戲"),
        SubCategory(id="272", name="手機遊戲", main_id="12", main_name="遊戲"),
        SubCategory(id="273", name="撲克牌", main_id="12", main_name="遊戲"),
        SubCategory(id="274", name="拼圖", main_id="12", main_name="遊戲"),
        SubCategory(id="34", name="桌上遊戲", main_id="12", main_name="遊戲"),
        SubCategory(id="35", name="電玩", main_id="12", main_name="遊戲"),
        SubCategory(id="357", name="音訊", main_id="13", main_name="新聞"),
        SubCategory(id="358", name="照片", main_id="13", main_name="新聞"),
        SubCategory(id="359", name="出版", main_id="13", main_name="新聞"),
        SubCategory(id="360", name="影片", main_id="13", main_name="新聞"),
        SubCategory(id="361", name="網站", main_id="13", main_name="新聞"),
        SubCategory(id="36", name="古典音樂", main_id="14", main_name="音樂"),
        SubCategory(id="386", name="喜劇", main_id="14", main_name="音樂"),
        SubCategory(id="37", name="鄉村 & 民謠音樂", main_id="14", main_name="音樂"),
        SubCategory(id="38", name="電子音樂", main_id="14", main_name="音樂"),
        SubCategory(id="318", name="信仰", main_id="14", main_name="音樂"),
        SubCategory(id="39", name="Hip-Hop", main_id="14", main_name="音樂"),
        SubCategory(id="40", name="獨立搖滾", main_id="14", main_name="音樂"),
        SubCategory(id="41", name="爵士", main_id="14", main_name="音樂"),
        SubCategory(id="319", name="兒童", main_id="14", main_name="音樂"),
        SubCategory(id="320", name="拉丁", main_id="14", main_name="音樂"),
        SubCategory(id="241", name="金屬", main_id="14", main_name="音樂"),
        SubCategory(id="42", name="流行音樂", main_id="14", main_name="音樂"),
        SubCategory(id="321", name="龐克", main_id="14", main_name="音樂"),
        SubCategory(id="322", name="R&B", main_id="14", main_name="音樂"),
        SubCategory(id="43", name="搖滾", main_id="14", main_name="音樂"),
        SubCategory(id="44", name="世界音樂", main_id="14", main_name="音樂"),
        SubCategory(id="275", name="動物", main_id="15", main_name="攝影"),
        SubCategory(id="276", name="藝術", main_id="15", main_name="攝影"),
        SubCategory(id="277", name="自然", main_id="15", main_name="攝影"),
        SubCategory(id="278", name="人物", main_id="15", main_name="攝影"),
        SubCategory(id="280", name="相片書", main_id="15", main_name="攝影"),
        SubCategory(id="279", name="場所", main_id="15", main_name="攝影"),
        SubCategory(id="331", name="3D 列印", main_id="16", main_name="科技"),
        SubCategory(id="332", name="應用程式", main_id="16", main_name="科技"),
        SubCategory(id="333", name="相機器材", main_id="16", main_name="科技"),
        SubCategory(id="334", name="電子類 DIY", main_id="16", main_name="科技"),
        SubCategory(id="335", name="製造工具", main_id="16", main_name="科技"),
        SubCategory(id="336", name="航空", main_id="16", main_name="科技"),
        SubCategory(id="337", name="小工具", main_id="16", main_name="科技"),
        SubCategory(id="52", name="硬體", main_id="16", main_name="科技"),
        SubCategory(id="362", name="創客空間", main_id="16", main_name="科技"),
        SubCategory(id="338", name="機器人", main_id="16", main_name="科技"),
        SubCategory(id="51", name="軟體", main_id="16", main_name="科技"),
        SubCategory(id="339", name="聲音", main_id="16", main_name="科技"),
        SubCategory(id="340", name="太空探索", main_id="16", main_name="科技"),
        SubCategory(id="341", name="穿戴式裝置", main_id="16", main_name="科技"),
        SubCategory(id="342", name="網站", main_id="16", main_name="科技"),
        SubCategory(id="388", name="喜劇", main_id="17", main_name="劇院"),
        SubCategory(id="281", name="實驗性", main_id="17", main_name="劇院"),
        SubCategory(id="282", name="節慶", main_id="17", main_name="劇院"),
        SubCategory(id="283", name="沉浸式", main_id="17", main_name="劇院"),
        SubCategory(id="284", name="音樂劇", main_id="17", main_name="劇院"),
        SubCategory(id="285", name="演出", main_id="17", main_name="劇院"),
        SubCategory(id="323", name="學術", main_id="18", main_name="出版"),
        SubCategory(id="324", name="作品選集", main_id="18", main_name="出版"),
        SubCategory(id="45", name="畫冊", main_id="18", main_name="出版"),
        SubCategory(id="325", name="行事曆", main_id="18", main_name="出版"),
        SubCategory(id="46", name="童書", main_id="18", main_name="出版"),
        SubCategory(id="387", name="喜劇", main_id="18", main_name="出版"),
        SubCategory(id="47", name="虛構小說", main_id="18", main_name="出版"),
        SubCategory(id="349", name="活版印刷", main_id="18", main_name="出版"),
        SubCategory(id="326", name="文學期刊", main_id="18", main_name="出版"),
        SubCategory(id="389", name="文學空間", main_id="18", main_name="出版"),
        SubCategory(id="48", name="非虛構小說", main_id="18", main_name="出版"),
        SubCategory(id="49", name="期刊", main_id="18", main_name="出版"),
        SubCategory(id="50", name="詩詞", main_id="18", main_name="出版"),
        SubCategory(id="239", name="廣播 & 播客", main_id="18", main_name="出版"),
        SubCategory(id="327", name="翻譯", main_id="18", main_name="出版"),
        SubCategory(id="328", name="年輕人", main_id="18", main_name="出版"),
        SubCategory(id="329", name="雜誌", main_id="18", main_name="出版"),
        SubCategory(id="343", name="蠟燭", main_id="26", main_name="手工藝"),
        SubCategory(id="344", name="鉤針編織", main_id="26", main_name="手工藝"),
        SubCategory(id="345", name="DIY", main_id="26", main_name="手工藝"),
        SubCategory(id="346", name="刺繡", main_id="26", main_name="手工藝"),
        SubCategory(id="347", name="玻璃", main_id="26", main_name="手工藝"),
        SubCategory(id="348", name="編織", main_id="26", main_name="手工藝"),
        SubCategory(id="350", name="陶藝", main_id="26", main_name="手工藝"),
        SubCategory(id="351", name="出版", main_id="26", main_name="手工藝"),
        SubCategory(id="352", name="拼布", main_id="26", main_name="手工藝"),
        SubCategory(id="353", name="文具", main_id="26", main_name="手工藝"),
        SubCategory(id="355", name="織造", main_id="26", main_name="手工藝"),
        SubCategory(id="356", name="木工", main_id="26", main_name="手工藝"),
    ]


class IdeaResult(TypedDict):
    id: str
    项目名称: str
    项目名称_中: str
    项目详情: str
    项目详情_中: str
    众筹进度: str
    主分类名称: str
    子分类名称: str
    缩略图链接: str
    详情链接: str
    宣传视频链接: str
    完整原始信息: str


def get_kickstarter_ideas_with_page_index(
    sub_category: SubCategory, page: int = 1, seed: str = ""
) -> tuple[str, int, list[IdeaResult]]:
    """
    获取 Kickstarter 子分类下的项目列表
    :param sub_category: 子分类信息
    :param page: 页码，默认第一页
    :param seed: 随机种子，用于分页
    :return: 包含 data-seed, 总页数, 项目列表的元组
    """

    sub_category_id = sub_category["id"]
    url = f"https://www.kickstarter.com/discover/advanced?category_id={sub_category_id}&sort=popularity&page={page}"
    if seed:
        url += f"&seed={seed}"
    try:
        html_content = _get_html_content(url)
        # 1. 进行html字符转义 (BeautifulSoup 在解析时会自动完成)
        soup = BeautifulSoup(html_content, "lxml")
        # 2. 获取id="project_list"的div标签，并得到它的属性值
        project_list_div = soup.find("div", id="projects_list")
        if not project_list_div:
            raise Exception(f"未找到id为'projects_list'的div标签")

        data_seed = project_list_div.get("data-seed")
        if not data_seed:
            raise Exception(f"未找到id为'projects_list'的div标签下的data-seed属性")

        data_total_hits = project_list_div.get("data-total_hits")
        if not data_total_hits:
            raise Exception(
                f"未找到id为'projects_list'的div标签下的data-total_hits属性"
            )
        total_page = int(data_total_hits) // 12 + 1

        project_divs = project_list_div.find_all("div", attrs={"data-project": True})
        if len(project_divs) == 0:
            raise Exception(f"未找到id为'projects_list'的div标签下的data-project属性")

        # 遍历所有找到的项目 div，并打印它们的 data-project 属性值
        # 这里的 data-project 属性通常是一个 JSON 字符串，包含了项目的详细信息
        idea_results = []
        for i, project_div in enumerate(project_divs):
            # 获取 data-project 属性的内容
            project_data_str = project_div.get("data-project")
            project_data_dict = json.loads(project_data_str)
            # 然后你就可以像操作字典一样操作它了
            idea_result: IdeaResult = {
                "id": project_data_dict.get("id"),
                "项目名称": project_data_dict.get("name"),
                "项目名称_中": "",
                "项目详情": "",
                "项目详情_中": "",
                "众筹进度": project_data_dict.get("percent_funded"),
                "主分类名称": sub_category["main_name"],
                "子分类名称": sub_category["name"],
                "缩略图链接": (project_data_dict.get("photo") or {}).get("full"),
                "详情链接": (
                    (project_data_dict.get("urls") or {}).get("web") or {}
                ).get("project"),
                "宣传视频链接": (project_data_dict.get("video") or {}).get("hls"),
                "完整原始信息": project_data_str,
            }
            idea_result["项目名称_中"] = translate_text_to_chinese(
                idea_result["项目名称"]
            )
            # 请求详情链接
            # if idea_result["详情链接"]:
            #     print(
            #         f"项目{idea_result['项目名称']} 请求详情链接: {idea_result['详情链接']}"
            #     )
            #     try:
            #         detail_content = _get_html_content(idea_result["详情链接"])
            #         # 解析详情页的 HTML 内容
            #         detail_soup = BeautifulSoup(detail_content, "lxml")
            #         # 提取项目详情（例如，项目描述）
            #         project_details = detail_soup.find("div", class_="story-content")
            #         if project_details:
            #             idea_result["项目详情"] = project_details.get_text(
            #                 separator="\n", strip=True
            #             )
            #             idea_result["项目详情_中"] = translate_text_to_chinese(
            #                 idea_result["项目详情"]
            #             )
            #     except Exception as e:
            #         # 单个详情获取失败，不影响其他项目
            #         print(
            #             f"获取项目{idea_result['项目名称']}详情失败: {traceback.format_exc()}"
            #         )
            idea_results.append(idea_result)
        return data_seed, total_page, idea_results
    except Exception as e:
        raise Exception(f"获取{url}失败: {traceback.format_exc()}")


if __name__ == "__main__":
    """
    非正式主函数，仅用于测试和示例用法
    """
    sub_categories = get_kickstarter_sub_categories()
    for i, sub_category in enumerate(sub_categories):
        if i > 0:
            # 只测一个分类
            break
        # 先获取第一页
        data_seed, total_page, idea_results = get_kickstarter_ideas_with_page_index(
            sub_category, page=1
        )
        print(
            f"第一页数据种子: {data_seed}, 总页数: {total_page}, 项目数: {len(idea_results)}"
        )
        # 接着剩下的page
        for page in range(2, total_page + 1):
            _, _, page_idea_results = get_kickstarter_ideas_with_page_index(
                sub_category, page=page, seed=data_seed
            )
            print(f"第{page}页数据种子: {data_seed}, 项目数: {len(page_idea_results)}")
            idea_results.extend(page_idea_results)
