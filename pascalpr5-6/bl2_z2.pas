var A: array[1..20] of integer;
n,i,j:integer;
begin
  writeln('Введите массив: '); n:=20;
  for i:integer:=1 to n do readln(a[i]);
  //for i:=1 to n do a[i]:=random(-50,50);
  writeln('Массив: ');for i:=1 to n do write(a[i],' '); writeln;
  
i:=1;
while i<=n do
if a[i]<0 then
 begin
  for j:=i to n-1 do
  a[j]:=a[j+1];
  n:=n-1;
 end
else i:=i+1;
      
 writeln('Массив: ');for i:=1 to n do write(a[i],' ');
end.