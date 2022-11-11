program bl_3_z4;//18
var i: integer;
begin
  write('Введите год: '); readln(i);
  if (i mod 4)<>0 then begin writeln('Обычный год'); end
  else begin
  if (i mod 100)=0 then begin
    if (i mod 400)=0 then begin writeln('Год высокосный'); end
    else writeln('Обычный год'); end
  else writeln('Год высокосный');
    end;
end.