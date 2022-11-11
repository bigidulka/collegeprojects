program bl_3_z3;//17
var a, b, c, D: real;
begin
  write('Введите любые 3 натуральных чисед: '); readln(a, b, c);
  D:=(b*b)-(4*a*c);
  if D<0 then writeln('Корней нет');
  if D=0 then writeln(-b/2*a);
  if D>0 then writeln('x1=',(((-b)+sqrt(D))/(2*a)),' x2=',(((-b)-sqrt(D))/(2*a)));
end.