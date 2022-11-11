program z5_while;
var a,b,sum, sum1, sum2, n,k:integer;
begin
  a:=100000;
  while a<>999999 do begin
    sum1:= 0; sum2:= 0;
    sum1:= (a div 100000)+((a div 10000)mod 10)+((a div 1000)mod 10);
    sum2:= (a mod 10)+((a mod 100)div 10)+((a mod 1000)div 100);
    if (sum1 = sum2) and (sum1 = 13) and (sum2 = 13) then
    begin
      //writeln(a, ' - "счастливый" билет');
      k := k + 1;
    end;
    a := a + 1;
  end;
  writeln('Всего счастливых билетов: ', k)
end.