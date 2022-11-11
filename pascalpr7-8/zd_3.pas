var s: string;
    i:integer;
begin
  write('Введите текст: '); readln(s);
  if s.Length mod 2 = 0 then
    writeln($'Первый: {s[1]}, Последний: {s[s.Length]}')
  else if s.Length = 1 then
    writeln($'Первый: {s[1]}')
  else
    writeln($'Первый: {s[1]}, Средний: {s[Trunc(s.Length/2)+1]}, Последний: {s[s.Length]}')
end.