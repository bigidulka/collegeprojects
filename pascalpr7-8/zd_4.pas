var s: string;
    i:integer;
begin
  write('Введите текст: '); readln(s);
  i:=s.Length;
  for j:integer:=1 to i do
    if((s[i]=s[j]) and (i<>j)) then begin 
      writeln(pos(s[j],s));
      end;
end.