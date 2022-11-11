var A: array[1..21] of integer;
n,i,j,p_ch_i,k_ch:integer;
begin
  writeln('Введите массив: '); n:=20;
  writeln('Массив: ');for i:=1 to n do write(a[i],' '); writeln;
for i:=1 to n do if a[i] mod 2 = 0 then inc(k_ch); // колво четных
for i:=1 to n do if a[i] mod 2 = 0 then begin p_ch_i:=i; break; end; // первый элемент
writeln('Колво четных: ', k_ch, ' Первый четный элемент индекс: ', p_ch_i);
For i:=n Downto p_ch_i+1 Do a[i+1]:= a[i];
   a[p_ch_i+1]:= k_ch; inc(n);
writeln('Массив: ');for i:=1 to n do write(a[i],' ');
end.