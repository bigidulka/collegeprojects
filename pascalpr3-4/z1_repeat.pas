program z1_repeat;
var n,i,f:integer;
begin
  write('Введите число: '); read(n); f:=1;
  repeat
    i:=i+1;
    f:=f*i;
  until i=n;
  writeln($'{n}! = {f}');
end.
