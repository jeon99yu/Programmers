select member_id, member_name, gender, to_char(date_of_birth, 'yyyy-mm-dd') date_of_birth
from member_profile
where tlno is not null
and to_char(date_of_birth, 'mm') = 3
and gender = 'W'
order by member_id;