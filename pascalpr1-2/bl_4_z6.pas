program bl_4_z5; //26
var a,b,c: real;
begin
  print('Введите 3 стороны треугольника (a,b,c): '); readln(a, b, c);
  if (a+b>c) and (a+c>b) and (b+c>a) then writeln('Треугольник существует')
  else writeln('Треугольник несуществует');
end.