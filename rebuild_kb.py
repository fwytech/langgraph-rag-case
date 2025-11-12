#!/usr/bin/env python3
"""
重建知识库向量数据库
"""
import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import MarkdownTextSplitter
from langchain_chroma import Chroma
from utils import get_embedding_model
import chromadb.api

print("=" * 60)
print("重建知识库向量数据库")
print("=" * 60)

# 知识库配置
kb_name = "bank"
kb_root = os.path.join(os.path.dirname(__file__), "kb")
kb_path = os.path.join(kb_root, kb_name)
file_storage_path = os.path.join(kb_path, "files")
vs_path = os.path.join(kb_path, "vectorstore")

print(f"\n知识库名称: {kb_name}")
print(f"文档路径: {file_storage_path}")
print(f"向量库路径: {vs_path}")

# 检查文件是否存在
if not os.path.exists(file_storage_path):
    print(f"\n✗ 错误: 文档路径不存在: {file_storage_path}")
    exit(1)

files = [f for f in os.listdir(file_storage_path) if f.endswith('.md')]
print(f"\n找到 {len(files)} 个文档文件:")
for f in files:
    print(f"  - {f}")

if not files:
    print("\n✗ 错误: 没有找到任何 .md 文件")
    exit(1)

# 加载文档
print("\n步骤 1: 加载文档...")
text_loader_kwargs = {"autodetect_encoding": True}
loader = DirectoryLoader(
    file_storage_path,
    glob="**/*.md",
    show_progress=True,
    use_multithreading=True,
    loader_cls=TextLoader,
    loader_kwargs=text_loader_kwargs,
)

docs_list = loader.load()
print(f"✓ 加载了 {len(docs_list)} 个文档")

# 分割文档
print("\n步骤 2: 分割文档...")
text_splitter = MarkdownTextSplitter(
    chunk_size=500, chunk_overlap=100
)
doc_splits = text_splitter.split_documents(docs_list)
print(f"✓ 分割为 {len(doc_splits)} 个文档块")

# 添加源信息到内容
print("\n步骤 3: 处理文档块...")
for doc in doc_splits:
    doc.page_content = doc.metadata["source"] + "\n\n" + doc.page_content
print(f"✓ 已处理 {len(doc_splits)} 个文档块")

# 清除 Chroma 缓存
print("\n步骤 4: 清除旧缓存...")
chromadb.api.client.SharedSystemClient.clear_system_cache()
print("✓ 缓存已清除")

# 创建向量存储
print("\n步骤 5: 创建向量存储...")
print("  - 获取 Embedding 模型...")
embedding = get_embedding_model(platform_type="OpenAI")
print("  - 创建 Chroma 向量存储...")

vectorstore = Chroma(
    collection_name=kb_name,
    embedding_function=embedding,
    persist_directory=vs_path,
)

print("  - 添加文档到向量存储...")
vectorstore.add_documents(doc_splits)
print(f"✓ 向量存储创建完成")

# 验证
print("\n步骤 6: 验证向量存储...")
retriever = vectorstore.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={
        "k": 3,
        "score_threshold": 0.15,
    }
)

test_query = "如何查询账户余额"
results = retriever.invoke(test_query)
print(f"✓ 测试查询: '{test_query}'")
print(f"✓ 检索到 {len(results)} 条结果")

if results:
    print("\n示例结果:")
    for i, doc in enumerate(results[:2], 1):
        content = doc.page_content[:100].replace('\n', ' ')
        print(f"  {i}. {content}...")

print("\n" + "=" * 60)
print("✓ 知识库向量数据库重建完成！")
print("=" * 60)
