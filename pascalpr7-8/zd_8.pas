var s: string;
begin
  write('Введите текст: '); readln(s);
  for i:integer:=1 to s.length do begin
    if (s[i]='x') then begin writeln('x первый'); break; end;
    if (s[i]='w') then begin writeln('w первый'); break; end;
    writeln('Таких Символов нет');
  end;
end.