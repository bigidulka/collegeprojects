program bl_4_z3;//20
var x1, y1, x2, y2: integer;
begin
  write('Введите координаты 1 точки: '); readln(x1, y1);
  write('Введите координаты 2 точки: '); readln(x2, y2);
  print('Лежат в одной координатной четверти: ');
  if (x1>0) and (y1>0) and (x2>0) and (x2>0) then
    print('да')
  else if (x1<0) and (y1>0) and (x2<0) and (y2>0) then
    print('да')
  else if (x1>0) and (y1<0) and (x2>0) and (y2<0) then 
    print('да')
  else print('нет');
end.z