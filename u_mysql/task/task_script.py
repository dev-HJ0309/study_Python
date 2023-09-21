from task_crud import save, find_all, update, delete, find_by_id
import hashlib

insert_query ="insert into tbl_papago(papago_kor, papago_eng) " \
                "values(%s, %s,)"
# papago_kor = papago.py의
#               encText = urllib.parse.quote("잘 지내니, 아프지 말고 건강해라") 소괄호 안
# papago_eng = papago.py의 result 값을 그대로 가져 와야 할것 같다.
insert_param = ['안녕하세요', 'hello!']
save(insert_query, insert_param)