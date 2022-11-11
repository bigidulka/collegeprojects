program bl_4_z1;//19
var i: integer;
begin
  write('Введите любое четырёхзначное натуральное число: '); readln(i);
  if ((i mod 10) = (i div 1000)) and ((i mod 100 div 10) = (i div 100 mod 10)) then begin writeln('Палиндром'); end
  else writeln('Обычное число');
end.1