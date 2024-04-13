# 从请求地址中提取出用户名和域名
#    http://www.163.com?userName=admin&pwd=123456

from urllib.parse import urlparse, parse_qs

def extract_username_and_domain(url):
    # 解析 URL
    parsed_url = urlparse(url)
    
    # 从解析后的结果中获取用户名
    query_params = parse_qs(parsed_url.query)
    username = query_params.get('userName', [''])[0]
    
    # 获取域名
    domain = parsed_url.netloc
    
    return username, domain

# 测试
url = "http://www.163.com?userName=admin&pwd=123456"
username, domain = extract_username_and_domain(url)
print("用户名：", username)
print("域名：", domain)
