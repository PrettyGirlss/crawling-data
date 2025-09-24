from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS, Chroma
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain_core.prompts.chat import SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_huggingface import HuggingFacePipeline
import os

HF_TOKEN = os.getenv('HF_TOKEN')

# 0. lcoal vectorestore path 설정
faiss_path = './faiss_file/FAISS(500,0,L6-v2)'
faiss_path2 = './faiss_file/FAISS(1000,200,L6-v2)'
chroma_path = 'vectorstore'

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
device

def get_response(query):

    # 1. 임베딩 모델 로드
    embeddings_model = HuggingFaceEmbeddings(
        model_name = 'all-MiniLM-L6-v2',
        model_kwargs = {'device':'cpu'},
        encode_kwargs = {'normalize_embeddings':True}
    )

    # 2-1. local에서 FAISS load
    # vectorstore = FAISS.load_local(
    #     folder_path=faiss_path,
    #     embeddings=embeddings_model,
    #     allow_dangerous_deserialization=True
    # )

    # 2-2. local에서 Chroma load
    vectorstore = Chroma(
        persist_directory=chroma_path,
        embedding_function=embeddings_model
    )

    # 3. retriever 설정
    # mmr: query 검색 시 중복되는 문서 피하는 방법
    retriever = vectorstore.as_retriever(search_type='similarity', search_kwargs={'k':5})

    # 4. chain 생성
    # 4-1. prompt
    # 일단 단일 prompt로 시작
    template = '''당신은 대한민국 관광지에 대해 잘 알려주는 친절한 챗봇입니다.
    context만을 이용해 답변하세요. context에서 확인할 수 없는 질문이라면 모른다고 답변해야합니다.
    답변은 prompt 내용 제외하고 Answer만 출력하세요.

    #Question:
    {query}
    #Context:
    {context}

    #Answer:'''
    prompt_template = PromptTemplate.from_template(template)

    # 4-2. llm
    # sllm 모델 생성
    model_name = "trillionlabs/Trillion-7B-preview"

    sllm = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.bfloat16,
    ).to(device)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    llm_pipe = pipeline(
        'text-generation',
        model=sllm,
        tokenizer=tokenizer,
        pad_token_id=tokenizer.eos_token_id
    )

    llm = HuggingFacePipeline(pipeline=llm_pipe)

    chain = (
    {'context': retriever, 'query': RunnablePassthrough()}
    | prompt_template 
    | llm 
    | StrOutputParser())

    response = chain.invoke(query)

    return response

if __name__=="__main__":
    res = get_response('서울에 가기 좋은 명소 알려줘')
    print(res)
