var A: array[1..20] of integer;
m_el, m_num:integer;
begin
for i:integer:=1 to 20 do a[i]:=random(-52,65);
write('Массив: '); for i:integer:=1 to 20 do write(a[i], ' ');
writeln();
m_el:=1;
m_num:=A[1];
for i:integer:=1 to 20 do 
  if A[i] > m_num then begin
    m_el:=i;
    m_num:=A[i];
  end;
writeln('Наибольший элемент массива: ', m_num, ' Индекс: ', m_el);
m_el:=1;
m_num:=A[1];
for i:integer:=1 to 20 do 
  if A[i] < m_num then begin
    m_el:=i;
    m_num:=A[i];
  end;
writeln('Наименьший элемент массива: ', m_num, ' Индекс: ', m_el);
for i:integer:=20 downto 1 do 
  if A[i] mod 5 = 0 then begin
    writeln('Число кратное 5: ', A[i], ' Индекс: ', i);
    break;
  end;
end.