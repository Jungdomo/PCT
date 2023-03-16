select
c.car_id,
if(sum(if(c.start_date <= '2022-10-16'and c.end_date >= '2022-10-16',1, 0)) = 1,
      "대여중", "대여 가능")
as availability
from car_rental_company_rental_history c
group by c.car_id
order by c.car_id desc