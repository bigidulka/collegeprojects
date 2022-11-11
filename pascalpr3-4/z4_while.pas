program z4_while;
var ot:real;
i, n:integer;
begin
  write('Введите N: ');read(n);
  i:=2;
  ot:=1;
  while n<>i-2 do begin
    ot:=ot*(1/i); inc(i);
  end;
  writeln(ot);
end.