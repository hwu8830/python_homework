# 有个字符串数组，存储了10个书名，书名有长有短，现
#    在将他们统一处理，若书名长度大于10，则截取长度8的
#    子串并且最后添加“...”，加一个竖线后输出作者的名字。
def process_book_names(book_names):
    for book_name in book_names:
        if len(book_name) > 10:
            processed_name = book_name[:8] + "..."
        else:
            processed_name = book_name
        author_name = input(f"书名:{book_name}请输入作者名字：")
        result = f"{processed_name} | {author_name}"
        print(result)

# 测试
book_names = ["old man and see", "how to make", "Machine", "Introduction to Algorithms", "Data Structures and Algorithms"]
process_book_names(book_names)
