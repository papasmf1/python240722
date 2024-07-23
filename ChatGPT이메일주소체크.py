import re

def is_valid_email(email):
    # 이메일 주소를 검사하는 정규 표현식
    # ^ : 문자열의 시작을 의미합니다.
    # [a-zA-Z0-9._%+-]+ : 알파벳 대소문자, 숫자, 점(.), 밑줄(_), 퍼센트(%), 더하기(+), 하이픈(-)이 1회 이상 반복될 수 있습니다.
    # @ : 반드시 '@' 문자가 있어야 합니다.
    # [a-zA-Z0-9.-]+ : 알파벳 대소문자, 숫자, 점(.), 하이픈(-)이 1회 이상 반복될 수 있습니다.
    # \. : 반드시 점(.) 문자가 있어야 합니다.
    # [a-zA-Z]{2,} : 알파벳 대소문자가 2회 이상 반복되어야 합니다.
    # $ : 문자열의 끝을 의미합니다.
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
    
    # 주어진 이메일이 정규 표현식과 일치하는지 확인합니다.
    return re.match(email_regex, email) is not None

# 샘플 이메일 주소
emails = [
    "example@example.com",           # 유효한 이메일
    "user.name+tag+sorting@example.com", # 유효한 이메일
    "user.name@example.co.in",       # 유효한 이메일
    "user.name@sub.example.com",     # 유효한 이메일
    "user@123.123.123.123",          # 유효한 이메일
    "user@[IPv6:2001:db8::1]",       # 유효한 이메일
    "plainaddress",                  # 유효하지 않은 이메일
    "@missingusername.com",          # 유효하지 않은 이메일
    "username@.com.my",              # 유효하지 않은 이메일
    "username@.com",          # 유효하지 않은 이메일
]

# 이메일 주소 유효성 검사
for email in emails:
    print(f"{email}: {'Valid' if is_valid_email(email) else 'Invalid'}")
