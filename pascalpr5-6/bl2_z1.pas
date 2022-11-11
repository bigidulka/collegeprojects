var A: array[1..20] of integer;
pp_in,m_in,m_num, n:integer;
begin
  writeln('Введите массив: '); n:=20;
  for i:integer:=1 to n do readln(a[i]);
  
for i:integer:=1 to n do 
  if A[i] > 0 then begin
    pp_in:=i; break; end; // первый пол
    
    m_num:=A[1];
for i:integer:=1 to n do 
  if A[i] < m_num then begin
    m_num:=A[i];
    m_in:=i; end; // наименьший
    
    for i:integer := pp_in to n-1 do
        a[i] := a[i+1];
      n := n-1;
 for i:integer := m_in to n-1 do
        a[i] := a[i+1];
      n := n-1;
      
 writeln('Массив: ');
 for i:integer:=1 to n do
 write(a[i],' ');
end.