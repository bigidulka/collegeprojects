program bl_2_z3; //9
var i: integer;
begin
  write('Введите любое натуральное число (трёхзначное): '); readln(i);
  writeln(i mod 10, (i mod 100) div 10 ,i div 100);
end.