program bl_2_z2; //8
var i: integer;
begin
  write('Введите любое натуральное число (трёхзначное или четырёхзначное): '); readln(i);
  if (i >= 100) and (i <= 999) then begin
    i:=i div 100;end
  else begin
  if (i>= 1000) and (i <=9999) then
    i:=i div 1000; end;
  writeln(i);
end.