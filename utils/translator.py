import unicodedata
from deep_translator import GoogleTranslator
import time
import re


def translate_text_to_chinese(text: str) -> str:
    """
    使用deep_translator翻译文本，支持长文本分段翻译

    Args:
        text (str): 要翻译的文本

    Returns:
        str: 翻译后的文本
    """
    if not text or len(text.strip()) == 0:
        return text

    try:
        # Google翻译API字符限制（通常为5000字符）
        MAX_CHAR_LIMIT = 4500  # 留一些余量

        # 如果文本长度在限制内，直接翻译
        if len(text) <= MAX_CHAR_LIMIT:
            translation = GoogleTranslator(
                source="auto", target="chinese (simplified)"
            ).translate(text)
            return translation

        # 长文本需要分段翻译
        print(f"⚠️  长文本检测到 ({len(text)} 字符)，开始分段翻译...")

        # 按句子或段落分割文本，尽量在自然断点处分割
        segments = []
        current_segment = ""

        # 尝试按句子分割（句号、问号、感叹号）
        sentences = re.split(r"(?<=[.!?])\s+", text)

        for sentence in sentences:
            # 如果当前句子加上当前分段会超过限制，且当前分段不为空
            if (
                len(current_segment) + len(sentence) > MAX_CHAR_LIMIT
                and current_segment
            ):
                segments.append(current_segment)
                current_segment = sentence
            else:
                if current_segment:
                    current_segment += " " + sentence
                else:
                    current_segment = sentence

        # 添加最后一个分段
        if current_segment:
            segments.append(current_segment)

        # 如果按句子分割后仍然有分段超过限制，按字符数硬分割
        final_segments = []
        for segment in segments:
            if len(segment) > MAX_CHAR_LIMIT:
                # 硬分割，每MAX_CHAR_LIMIT字符分割一次
                for i in range(0, len(segment), MAX_CHAR_LIMIT):
                    final_segments.append(segment[i : i + MAX_CHAR_LIMIT])
            else:
                final_segments.append(segment)

        # 翻译每个分段
        translated_segments = []
        for i, segment in enumerate(final_segments):
            print(f"  正在翻译分段 {i+1}/{len(final_segments)} ({len(segment)} 字符)")
            try:
                translated = GoogleTranslator(
                    source="auto", target="chinese (simplified)"
                ).translate(segment)
                translated_segments.append(translated)
                # 添加短暂延迟避免API限制
                time.sleep(0.1)
            except Exception as e:
                raise Exception(f"  分段翻译错误: {str(e)}")

        # 合并翻译结果
        return " ".join(translated_segments)

    except Exception as e:
        print(f"翻译错误: {str(e)}")
        return ""


# def chunk_text(text: str, max_len: int = 3000):
#     """按字符数切块"""
#     text = text.replace("\n", " ")  # 先去掉换行，保证块大小均匀
#     chunks = []
#     start = 0
#     while start < len(text):
#         end = start + max_len
#         chunks.append(text[start:end])
#         start = end
#     return chunks


# def translate_long_text_fast(text: str, src="auto", dest="en") -> str:
#     text = unicodedata.normalize("NFKC", text)
#     translator = GoogleTranslator(source=src, target=dest)
#     chunks = chunk_text(text, max_len=2000)  # 每块 2000 字
#     translated_chunks = []

#     for chunk in chunks:
#         try:
#             translated_chunks.append(translator.translate(chunk))
#         except Exception as e:
#             print(f"翻译失败: {e}")
#             translated_chunks.append(chunk)

#     return " ".join(translated_chunks)
