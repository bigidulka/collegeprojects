program z2_while;
var a,b,n, f,x:real;
begin
  write('Введите Отрезок(a, b): ');read(a,b);
  write('Введите Шаг(n): ');read(n);
  x:=a;
  while x<b do begin
    f:=3*power(x,2)-power(2,x);
    writeln('F = ', f);
    x:=x+n;
  end;
end.