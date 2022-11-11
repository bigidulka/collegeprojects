program bl_4_z4; //24
var a, b, x: real;
begin
  write('Введите 2 целых числа: '); readln(a,b);
  x:=-b/a;
  if (a*x)=-b then writeln(x)
  else if b<>0 then writeln('Рещений нет')
  else begin print('x - любое'); 
  end;
end.