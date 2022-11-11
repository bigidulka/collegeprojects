var n:integer;
A: array of integer;
begin
  write('Введите размер массива: '); readln(n);
  a:= new integer [n];
  writeln('Введите массив: ');
 for i:integer:=0 to n-1 do
  begin
   write('a[',i,']=');
   read(a[i]);
  end;
 for i:integer:=0 to n-2 do begin
   if a[i] < a[i+1] then 
     else begin writeln('Массив не отсортирован'); break; end;
   writeln('Массив отсортирован'); break;
   end;
 writeln('Массив: ');
 for i:integer:=0 to n-1 do
 write(a[i],' ');
end.