# 假设这是我们从一个文件里读取的长篇文章
long_text = """检索增强生成（RAG）是一种先进的人工智能技术，它将大型语言模型（LLM）的强大生成能力与外部知识库的实时信息检索相结合。

该模型在生成回答之前，会先从一个庞大的数据源（如公司的内部文档或最新的网络文章）中检索相关信息。

这个过程确保了答案不仅基于模型预训练的知识，还包含了最新、最具体的数据，从而显著提高了回答的准确性和相关性。"""

# 一个非常简单的分块函数，根据段落（两个换行符）来切分
def chunk_text_by_paragraph(text):
  """根据段落切分文本"""
  chunks = text.split('\n\n')
  return [chunk.strip() for chunk in chunks if chunk.strip()] # 移除空白块

# 执行分块
text_chunks = chunk_text_by_paragraph(long_text)

# 打印结果，看看效果
for i, chunk in enumerate(text_chunks):
  print(f"--- Chunk {i+1} ---")
  print(chunk)
  print()