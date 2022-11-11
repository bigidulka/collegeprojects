program bl_3_z1;//13
var a, b, c, min: integer;
begin
  write('Введите любые 3 натуральных чисед: '); readln(a, b, c);
  min:=a;
  if b < min then min:=b;
  if c < min then min:=c;
  writeln(min);
end.