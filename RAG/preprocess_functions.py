import pandas as pd
import numpy as np
import re
from langchain_core.documents import Document



# 특수 문자와 각종 필요없는 글자들 제거하는 함수
def remove_nonwords(text):
    text = text.replace(':)',"")    # :) 제거
    text = text.replace('\n더보기','')      # \n 더보기, \n 닫기, \n 제거
    text = text.replace('\n닫기','')
    text = text.replace('\r\n',' ')
    text = text.replace('\n',' ')
    text = text.replace('\r', ' ')
    text = re.sub('[^a-zA-Z가-힣\'"· 0-9.,()㎡[0-9]~[0-9]]','',text) # 숫자와 숫자 사이에 있는 ~ 남겨야함
    return text     # 제거한 텍스트 반환


# 상세 정보와 리뷰가 따로 Document에 있는 버전
def make_csv_to_documents_sep(file_path):
    data = []
    new_df = pd.read_csv(file_path)
    # new_df.drop('Unnamed: 0',axis=1,inplace=True)     혹시 컬럼에 Unnamed: 0 있으면 제거하는 코드

    for idx in range(len(new_df)):
        location_data = {}
        meta_data = {}
        row = new_df.iloc[idx][new_df.iloc[idx].notna()]

        for col in list(row.index):
            if col == 'info':
                modified_info = remove_nonwords(row['info'])
                location_data['description']= modified_info
                
            elif col == 'review':
                if len(row['review'])<10:       # 10글자 미만이면 아예 삭제
                    location_data['review'] = ''
                else:
                    modified_review = remove_nonwords(row['review'])
                    location_data['review'] = modified_review
            else:
                row[col] = row[col].replace('\r\n',' ')
                row[col] = row[col].replace('\n', ' ')
                row[col] = row[col].replace('\r',' ')
                meta_data[col] = row[col]
        if 'review' not in list(row.index):           # 리뷰랑 info가 row.index에 없으면 review 항목과 description 항목 추가
            location_data['review'] = ''
        if 'info' not in list(row.index):
            location_data['description'] = ''

        data.append(Document(
            page_content=location_data['description'],
            metadata=meta_data
        ))
        
        if len(location_data['review']) >= 10:
            data.append(Document(
            page_content=location_data['review'],
            metadata=meta_data
            ))

    return data



# 상세 정보와 리뷰가 같이 하나의 Document에 저장되어 있는 버전
def make_csv_to_documents_with(file_path):
    data = []
    new_df = pd.read_csv(file_path)
    # new_df.drop('Unnamed: 0',axis=1,inplace=True)             # 혹시 컬럼에 Unnamed: 0 있으면 제거하는 코드

    for idx in range(len(new_df)):
        location_data = {}
        meta_data = {}
        row = new_df.iloc[idx][new_df.iloc[idx].notna()]

        for col in list(row.index):
            if col == 'info':
                location_data['description']= row['info']
            elif col == 'review':
                if len(row['review'])<10:       # 10글자 미만이면 아예 삭제
                    location_data['review'] = ''
                else:
                    row['review'] = remove_nonwords(row['review'])
                    location_data['review'] = row['review']
            else:
                row[col] = row[col].replace('\r\n',' ')
                row[col] = row[col].replace('\n', ' ')
                row[col] = row[col].replace('\r',' ')
                meta_data[col] = row[col]
        if 'review' not in list(row.index):           # 리뷰가 아예 없어서 row에 없으면 
            location_data['review'] = ''
        if 'info' not in list(row.index):
            location_data['description'] = ''

        data.append(Document(
            page_content="".join(location_data['description'] + location_data['review']),
            metadata=meta_data
        ))

    return data