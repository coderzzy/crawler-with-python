from dotenv import load_dotenv
import os
import csv
import time

from crawler.kickstarter import (
    get_kickstarter_sub_categories,
    get_kickstarter_ideas_with_page_index,
    IdeaResult,
)


load_dotenv()


def run_kickstarter_crawler_and_save_csv(output_csv_path: str):
    print("开始爬取 Kickstarter 项目")

    # 初始化 csv 文件，写入表头
    with open(output_csv_path, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(IdeaResult.__annotations__.keys())

    sub_categories = get_kickstarter_sub_categories()
    print(f"总分类数: {len(sub_categories)}")
    for sub_category in sub_categories:
        print(f"开始爬取子分类: {sub_category['name']}")
        # 先获取第一页
        data_seed, total_page, idea_results = get_kickstarter_ideas_with_page_index(
            sub_category, page=1
        )
        print(
            f"第一页数据种子: {data_seed}, 总页数: {total_page}, 项目数: {len(idea_results)}"
        )
        # 数据存储到 csv 文件
        with open(output_csv_path, "a", encoding="utf-8") as f:
            writer = csv.writer(f)
            # 将字典列表转换为值列表，确保写入的是实际数据而不是键名
            writer.writerows([list(result.values()) for result in idea_results])

        # # 接着剩下的page
        # for page in range(2, total_page + 1):
        #     _, _, page_idea_results = get_kickstarter_ideas_with_page_index(
        #         sub_category, page=page, seed=data_seed
        #     )
        #     print(f"第{page}页数据种子: {data_seed}, 项目数: {len(page_idea_results)}")
        #     # 数据追加存储到 csv 文件
        #     with open(output_csv_path, "a", encoding="utf-8") as f:
        #         writer = csv.writer(f)
        #         # 将字典列表转换为值列表，确保写入的是实际数据而不是键名
        #         writer.writerows([list(result.values()) for result in page_idea_results])


if __name__ == "__main__":
    print("hello world")

    os.makedirs("output", exist_ok=True)
    run_kickstarter_crawler_and_save_csv(
        f"output/kickstarter_{time.strftime('%Y%m%d%H%M%S')}.csv"
    )
