# 세팅
#python -m pip install PyMySQL / mySQL과 연동 할 수 있는 드라이버 설치
#pip install cryptography / 오류 메세지 방지 해주는

import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='app', charset='utf8')
cursor = conn.cursor(pymysql.cursors.DictCursor)
#cursor.execute("insert into tbl_member(member_id, member_password, member_name) values('hds1234', '1234', '한동석')")
#conn.commit()
# 드라이버는 열었으면 연 순서대로 꼭 닫아주어야 한다.
# TCL => 트랜젝션을 관리 할 수 있는
# 트랜젝션 = 하나의 서비스를 구현 하기 위해 사용한 쿼리들의 묶음
# commit 을 해주지 않으면 확정이 되지 않는다.
cursor.execute("select id, member_id, member_password, member_name from tbl_member")
rows = cursor.fetchall()
# fetchall은 결과가 여러 개 일 때 전체 행을 다 가져 온다.
#  결과가 한 개면 fetchone을 쓴다.
print(rows)

cursor.close()
conn.close()