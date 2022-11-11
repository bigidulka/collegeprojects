var s: string;
begin
  write('Введите строку: '); readln(s);
  if s.Length > 10 then
    delete(s,7,s.Length+1)
  else for i:integer:=s.Length+11 to 12 do
    s:=s+'o';
  writeln(s);
end.