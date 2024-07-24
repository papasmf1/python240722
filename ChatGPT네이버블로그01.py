import requests
from bs4 import BeautifulSoup
from datetime import *

def crawl_naver_blog(search_keyword):
    # 검색어를 URL에 맞게 인코딩
    query = requests.utils.quote(search_keyword)
    url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={query}"

    # HTTP GET 요청
    response = requests.get(url)
    response.raise_for_status()  # 요청 실패 시 예외 발생

    # BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(response.text, 'lxml')

    # 블로그 정보 저장할 리스트
    blogs = []

    # 블로그 포스트 찾기
    for post in soup.find_all('div', class_='api_blog_post'):
        title_tag = post.find('a', class_='api_txt_lines')
        blog_name_tag = post.find('a', class_='api_txt_lines')
        blog_url_tag = post.find('a', class_='api_txt_lines')['href']
        date_tag = post.find('span', class_='sub_time')

        if title_tag and blog_name_tag and date_tag:
            title = title_tag.get_text(strip=True)
            blog_name = blog_name_tag.get_text(strip=True)
            blog_url = blog_url_tag
            date_text = date_tag.get_text(strip=True)
            date = convert_date(date_text)

            blogs.append({
                'title': title,
                'blog_name': blog_name,
                'blog_url': blog_url,
                'date': date
            })

    return blogs

def convert_date(date_text):
    try:
        if '일 전' in date_text:
            days_ago = int(date_text.split('일 전')[0])
            date = datetime.now() - timedelta(days=days_ago)
        elif '시간 전' in date_text:
            hours_ago = int(date_text.split('시간 전')[0])
            date = datetime.now() - timedelta(hours=hours_ago)
        elif '분 전' in date_text:
            minutes_ago = int(date_text.split('분 전')[0])
            date = datetime.now() - timedelta(minutes=minutes_ago)
        else:
            date = datetime.strptime(date_text, '%Y.%m.%d.')
        return date.strftime('%Y-%m-%d')
    except:
        return 'Unknown'

if __name__ == "__main__":
    search_keyword = "파이썬 웹 크롤링"
    blogs = crawl_naver_blog(search_keyword)
    for blog in blogs:
        print(blog)
