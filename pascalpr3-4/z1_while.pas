program z1_while;
var i,n,k:integer;
begin
  write('Напишите число: '); readln(n);
  i:=1;
  k:=1;
  while(i<>n) do begin
    if n mod i = 0 then inc(k); inc(i);
  end;
  writeln('Количество делителей: ', k);
end.