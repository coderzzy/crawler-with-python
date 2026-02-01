# https://www.kickstarter.com/

import cloudscraper
from bs4 import BeautifulSoup
import time
import random
import json
import traceback
from typing import TypedDict


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
    # 理论上可以爬取，这里直接人工维护写死
    return [
        SubCategory(id="287", name="陶瓷", main_id="1", main_name="艺术"),
    ]


class IdeaResult(TypedDict):
    id: str
    项目名称: str
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
