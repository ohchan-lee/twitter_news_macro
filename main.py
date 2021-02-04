
"""
Author : ohchan Lee
Last Modification : 2021.02.02
ohchan29286@gmail.com
https://github.com/ohchan-lee/twitter_news_macro
"""


import sys
import twitter_news_with_macro as tw

# 아이디를 입력받습니다.
id = sys.argv[1].strip()

# 패스워드를 입력받습니다.
ps = sys.argv[2].strip()

# 검색어를 입력받습니다.
keyword = sys.argv[3].strip()

# 클래스를 선언합니다.
BOT = tw.NewsBot()

# 로봇으로 뉴스를 스크랩합니다.
BOT.scrap_news(id, ps, keyword)





















