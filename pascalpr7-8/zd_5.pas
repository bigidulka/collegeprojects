var s: string;
begin
  write('Введите текст: '); readln(s);
  if s[1] = s[s.Length] then writeln(1);
   for i:integer:= 1 to s.length - 2 do
     if (s[i] = s[s.length - 1]) then
        writeln(i + 1, ' ');
        end.