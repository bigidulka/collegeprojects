program bl_3_z2;//14
var a, b, c, i: integer;
begin
  write('Введите любые 3 натуральных чисед: '); readln(a, b, c);
  if a>=0 then inc(i);
  if b>=0 then inc(i);
  if c>=0 then inc(i);
  writeln(i);
end.