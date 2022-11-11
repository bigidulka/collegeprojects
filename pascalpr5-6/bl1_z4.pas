var A,B: array[1..30] of integer;
n:integer;
begin
for i:integer:=1 to 30 do a[i]:=random(-99,67);
write('Массив A: '); for i:integer:=1 to 30 do write(a[i], ' ');
writeln;
 n:=0;
  for i:integer:=1 to 30 do
    if  a[i] mod 2 = 0 then
      begin
        n:=n+1;
        b[n]:=a[i];
      end;
write('Массив B: '); for i:integer:=1 to n do write(b[i], ' ');
end.