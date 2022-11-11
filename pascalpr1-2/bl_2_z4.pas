program bl_2_z4; //12
var i: integer;
begin
  write('Введите любое натуральное число (четырёхзначное): '); readln(i);
  writeln('Сумма и произведение: ',
  (i div 1000)+((i div 100)mod 10)+((i mod 100)div 10)+(i mod 10), ' ', 
  (i div 1000)*((i div 100)mod 10)*((i mod 100)div 10)*(i mod 10));
end.