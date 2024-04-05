import requests
import bs4 # beautifulsoup4와 lxml을 모두 설치

url="https://comic.naver.com/webtoon/weekday"
response=requests.get(url)
response.raise_for_status()
soup=bs4.BeautifulSoup(response.text,"html.parser")
count=1

print("%d. %s"%(count,soup.title)) # 1. 처음의 html 태그 추출
count+=1

print("%d. %s"%(count,soup.title.get_text())) # 2. 텍스트 추출
count+=1

print("%d. %s"%(count,soup.a.attrs)) # 3. 태그의 속성 추출
count+=1

print("%d. %s %s"%(count,soup.a["href"],soup.a.attrs["href"])) # 4. 특정 속성 추출
count+=1

webtoon_rank_1=soup.find("li",attrs={"class":"rank01"}) # 속성을 이용한 태그추출
title=webtoon_rank_1.a["title"]
rank1_text=soup.find("a",text=title).get_text() # 태그의 텍스트 이용
print("%d. (rank1) %s %s"%(count,title,webtoon_rank_1.a["title"])) # 5. 처음의 특정 html 태그 추출
count+=1

webtoon_title=soup.find_all("a",attrs={"class":"title"}) # 모든 태그를 리스트의 형태로 반환
print("%d. "%count,end="")
for title in webtoon_title[:3]:
    print(title.get_text(),end=" ") # 6. 모든 특정 html 태그 추출
count+=1

webtoon_rank=webtoon_rank_1.parent
print("%d. %s"%(count,webtoon_rank["class"])) # 7. 부모 태그 추출
count+=1

webtoon_rank_2=webtoon_rank_1.next_sibling.next_sibling # 설정에 따라 여러번 sibling을 해야 할 수 있음
webtoon_rank_1=webtoon_rank_2.previous_sibling.previous_sibling
print("%d. (rank1) %s (rank2) %s"%(count,webtoon_rank_1.a["title"],webtoon_rank_2.a["title"])) # 8. 다음 태그 추출
count+=1

webtoon_rank_2=webtoon_rank_1.find_next_sibling("li") # find_next_sibling 을 이용해 다음 태그를 설정할 수 있음
webtoon_rank_1=webtoon_rank_2.find_previous_sibling("li")
print("%d. (rank1) %s (rank2) %s"%(count,webtoon_rank_1.a["title"],webtoon_rank_2.a["title"])) # 9. 다음 태그 추출
count+=1