var s: string;
    n,n0:integer;
begin
  write('Введите текст: '); readln(s);
  for i:integer:=1 to s.length do begin
    if((s[i]='+') or (s[i]='-')) then inc(n);
    if((s[i]<>s[s.Length])and(s[i+1]='0')and((s[i]='+')or(s[i]='-'))) then inc(n0);
  end;
  writeln($'Без нуля: {n}, С нулем: {n0}');
end.