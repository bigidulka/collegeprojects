program bl_4_z3;//21
var a, b, c, ch, nch: integer;
begin
  write('Введите три целых числа: '); readln(a, b, c);
  if (a mod 2)=0 then inc(ch)
  else inc(nch);
  if (b mod 2)=0 then inc(ch)
  else inc(nch);
  if (c mod 2)=0 then inc(ch)
  else inc(nch);
  writeln('Четных: ', ch, ' Нечетныйх: ', nch);
end.