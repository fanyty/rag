import numpy as np
from sentence_transformers import SentenceTransformer

# We'll use FAISS, a library for efficient similarity search.
import faiss

# --- Phase 1: Preparation (The "Offline" work) ---
print("--- Phase 1: Preparing the Knowledge Base ---")

# 1a. The Knowledge Base: Our document(s)
knowledge_base_text = """
检索增强生成（RAG）是一种先进的人工智能技术，它将大型语言模型（LLM）的强大生成能力与外部知识库的实时信息检索相结合。
该模型在生成回答之前，会先从一个庞大的数据源（如公司的内部文档或最新的网络文章）中检索相关信息。
这个过程确保了答案不仅基于模型预训练的知识，还包含了最新、最具体的数据，从而显著提高了回答的准确性和相关性。
RAG通过引用外部知识源，可以有效减少大语言模型‘幻觉’（Hallucination）的现象，让回答更加可靠。
由于知识库可以随时更新，RAG模型能够回答关于最新事件的问题，而无需重新训练整个模型，这大大降低了维护成本。
"""

# 1b. Chunking: Split the text into smaller, meaningful pieces
text_chunks = [chunk.strip() for chunk in knowledge_base_text.strip().split('\n') if chunk.strip()]
print(f"Step 1: Document split into {len(text_chunks)} chunks.")

# 1c. Vectorization: Convert text chunks into numerical vectors
print("Step 2: Vectorizing text chunks...")
model = SentenceTransformer('all-MiniLM-L6-v2')
chunk_embeddings = model.encode(text_chunks)
print(f"Successfully created embeddings of dimension: {chunk_embeddings.shape[1]}")

# 1d. Indexing: Create a FAISS index to store and search the vectors
vector_dimension = chunk_embeddings.shape[1]
index = faiss.IndexFlatL2(vector_dimension) # Using a simple L2 distance index
index.add(chunk_embeddings) # Add our vectors to the index
print(f"Step 3: Stored {index.ntotal} vectors in the FAISS index.\n")


# --- Phase 2: Application (The "Live" RAG process) ---
print("--- Phase 2: Answering a User Question ---")

# 2a. The User's Question
user_question = "RAG技术有什么好处？"
print(f"User Question: {user_question}")

# 2b. Vectorize the question
question_embedding = model.encode([user_question])

# 2c. Search: Retrieve the most relevant chunks from our index
k = 2 # Number of relevant chunks to retrieve
distances, indices = index.search(question_embedding, k)
relevant_chunks = [text_chunks[i] for i in indices[0]]
print(f"\nStep 4: Retrieved the following {k} relevant chunks:")
for i, chunk in enumerate(relevant_chunks):
    print(f"  - Chunk {i+1}: {chunk}")

# 2d. Augment the Prompt: Combine the question and the retrieved context
context = "\n".join(relevant_chunks)
augmented_prompt = f"""
请根据以下背景信息来回答问题:

背景信息:
---
{context}
---

问题: {user_question}
"""

print("\nStep 5: Constructed the Augmented Prompt for the LLM:")
print(augmented_prompt)

# 2e. Generation (Simulated): Pass the augmented prompt to an LLM
# In a real application, this is where you would make an API call to an LLM like Gemini.
print("--- SIMULATING LLM GENERATION ---")
simulated_answer = "根据提供的资料，RAG技术的好处主要包括：通过结合外部知识提高了回答的准确性和相关性，并能有效减少模型产生‘幻觉’。"
print(f"Final Answer: {simulated_answer}")