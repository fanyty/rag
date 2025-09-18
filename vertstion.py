# 确保你已经安装了必要的库
# pip install sentence-transformers torch

from sentence_transformers import SentenceTransformer

# 假设这是我们上一步得到的文本块
text_chunks = [
    "检索增强生成（RAG）是一种先进的人工智能技术，它将大型语言模型（LLM）的强大生成能力与外部知识库的实时信息检索相结合。",
    "该模型在生成回答之前，会先从一个庞大的数据源（如公司的内部文档或最新的网络文章）中检索相关信息。",
    "这个过程确保了答案不仅基于模型预训练的知识，还包含了最新、最具体的数据，从而显著提高了回答的准确性和相关性。"
]

# 1. 加载一个预训练好的模型作为我们的“翻译官”
#    'all-MiniLM-L6-v2' 是一个非常流行的高效模型
model = SentenceTransformer('all-MiniLM-L6-v2')

# 2. 使用模型对每一个文本块进行编码（向量化）
chunk_embeddings = model.encode(text_chunks)

# 3. 打印结果，看看向量长什么样
for chunk, embedding in zip(text_chunks, chunk_embeddings):
    print(f"--- Text Chunk ---")
    print(chunk)
    print(f"\n--- Vector (Embedding) ---")
    print(embedding)
    print(f"\nVector Dimension: {len(embedding)}") # 看看这个向量有多长
    print("-" * 30)
    


user_question = "RAG技术相比传统方法有什么优势？"

