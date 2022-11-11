var s: string;
begin
  write('Введите текст: '); readln(s);
  for i:integer:=3 to s.length step 3 do begin
       write(s[i]);
       end;
end.